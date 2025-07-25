import os
import zipfile
import base64
import json
import logging
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from openai import OpenAI
from typing import Dict, List, Tuple, Optional
from pathlib import Path
from dotenv import load_dotenv

# Configure Unicode-compatible logging
class UnicodeStreamHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            msg = self.format(record)
            stream = self.stream
            stream.write(msg.encode('utf-8').decode('utf-8') + self.terminator)
            self.flush()
        except Exception:
            self.handleError(record)

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('slide_processing.log', encoding='utf-8'),
            UnicodeStreamHandler()
        ]
    )

configure_logging()
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Constants
OCR_ROOT = Path("D:/OCR")
# ZIP_FILES = [
#     OCR_ROOT / f"unit{i}.zip" for i in range(1, 7)
# ]
ZIP_FILES = [
     OCR_ROOT / f"unit1.zip" 
 ]
EXTRACT_DIR = OCR_ROOT / "temp_extracted"
OUTPUT_DIR = OCR_ROOT / "output"
MAX_WORKERS = 5
MODEL_NAME = "gpt-4o"  # Using GPT-4 Omni model

# Ensure directories exist
EXTRACT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Initialize OpenAI client
try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    if not client.api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")
except Exception as e:
    logger.error(f"Failed to initialize OpenAI client: {str(e)}")
    raise

def encode_image(image_path: Path) -> str:
    """Encode image to base64 string with validation."""
    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    except Exception as e:
        logger.error(f"Failed to encode image {image_path}: {str(e)}")
        raise

def load_checkpoint(checkpoint_file: Path) -> Dict:
    """Load existing checkpoint data with validation."""
    try:
        if checkpoint_file.exists():
            with open(checkpoint_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}
    except json.JSONDecodeError:
        logger.warning(f"Invalid JSON in checkpoint: {checkpoint_file}")
        return {}
    except Exception as e:
        logger.error(f"Failed to load checkpoint {checkpoint_file}: {str(e)}")
        raise

def save_checkpoint(checkpoint_file: Path, data: Dict) -> None:
    """Atomic checkpoint save with tmp file rotation."""
    tmp_file = checkpoint_file.with_suffix('.tmp')
    try:
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        if checkpoint_file.exists():
            checkpoint_file.unlink()
        tmp_file.rename(checkpoint_file)
    except Exception as e:
        logger.error(f"Failed to save checkpoint {checkpoint_file}: {str(e)}")
        if tmp_file.exists():
            tmp_file.unlink()
        raise

def get_system_prompt() -> str:
    """Load the system prompt with validation."""
    try:
        # First try relative import
        try:
            from prompt import SYSTEM_PROMPT
        except ImportError:
            # Fallback to absolute path
            sys.path.append(str(OCR_ROOT))
            from prompt import SYSTEM_PROMPT
            
        if not SYSTEM_PROMPT.strip():
            raise ValueError("Empty system prompt")
        return SYSTEM_PROMPT
    except Exception as e:
        logger.error(f"Failed to load system prompt: {str(e)}")
        # Fallback prompt if loading fails
        return """Extract text from slides and convert to Markdown with:
- Accurate text extraction
- Proper hierarchy (# for titles, - for bullets)
- Diagram descriptions in blockquotes
- Tables in Markdown format
- Mathematical equations in LaTeX
- No added commentary"""

def process_slide(slide_info: Tuple[int, int, Path, Dict]) -> Tuple[int, str]:
    """Process single slide with error handling and retry logic."""
    unit_index, idx, image_path, checkpoint_data = slide_info
    
    # Return cached result if available
    if str(idx) in checkpoint_data:
        return idx, checkpoint_data[str(idx)]

    max_retries = 3
    for attempt in range(max_retries):
        try:
            base64_image = encode_image(image_path)
            
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": get_system_prompt()},
                            {
                                "type": "image_url",
                                "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                            },
                        ],
                    }
                ],
                temperature=0.1,
                max_tokens=2000,
            )

            slide_content = response.choices[0].message.content.strip()
            return idx, slide_content
        except Exception as e:
            if attempt == max_retries - 1:
                logger.error(f"Failed to process slide {idx} after {max_retries} attempts: {str(e)}")
                return idx, f"Error processing slide: {str(e)}"
            logger.warning(f"Retry {attempt + 1} for slide {idx}")
            continue

def extract_zip(zip_file: Path, extract_to: Path) -> None:
    """Safe zip extraction with validation."""
    if not zip_file.exists():
        raise FileNotFoundError(f"ZIP file not found: {zip_file}")
    
    try:
        with zipfile.ZipFile(zip_file, "r") as zip_ref:
            zip_ref.extractall(extract_to)
    except zipfile.BadZipFile:
        logger.error(f"Corrupted ZIP file: {zip_file}")
        raise
    except Exception as e:
        logger.error(f"Failed to extract {zip_file}: {str(e)}")
        raise

def get_sorted_images(folder: Path) -> List[Path]:
    """Get numerically sorted image files with validation."""
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")
    
    image_exts = (".jpg", ".jpeg", ".png", ".webp")
    images = []
    
    try:
        for ext in image_exts:
            images.extend(folder.glob(f"*{ext}"))
        
        # Sort by natural number in filename
        images.sort(key=lambda x: int(''.join(filter(str.isdigit, x.stem))))
        return images
    except Exception as e:
        logger.error(f"Failed to sort images in {folder}: {str(e)}")
        raise

def save_markdown(unit_index: int, results: Dict[int, str]) -> Path:
    """Atomic markdown file save with validation."""
    markdown_file = OUTPUT_DIR / f"Unit-{unit_index}.md"
    tmp_file = markdown_file.with_suffix('.tmp')
    
    try:
        with open(tmp_file, "w", encoding="utf-8") as md:
            md.write(f"# Unit {unit_index}\n\n")
            for idx, content in sorted(results.items()):
                md.write(f"## Slide {idx}\n\n{content}\n\n")
        
        if markdown_file.exists():
            markdown_file.unlink()
        tmp_file.rename(markdown_file)
        return markdown_file
    except Exception as e:
        logger.error(f"Failed to save markdown {markdown_file}: {str(e)}")
        if tmp_file.exists():
            tmp_file.unlink()
        raise

def process_unit(unit_index: int) -> None:
    """Complete unit processing pipeline."""
    logger.info(f"🚀 Processing Unit {unit_index}...")
    
    try:
        zip_file = ZIP_FILES[unit_index - 1]
        unit_folder = EXTRACT_DIR / f"unit_{unit_index}"
        checkpoint_file = OUTPUT_DIR / f"Unit-{unit_index}.json"
        
        # Extract ZIP
        unit_folder.mkdir(exist_ok=True)
        extract_zip(zip_file, unit_folder)
        
        # Get sorted images
        images = get_sorted_images(unit_folder)
        if not images:
            logger.warning(f"No images found in unit {unit_index}")
            return

        # Load checkpoint
        checkpoint_data = load_checkpoint(checkpoint_file)
        
        # Prepare slide info (only unprocessed slides)
        slide_infos = [
            (unit_index, idx, image_path, checkpoint_data) 
            for idx, image_path in enumerate(images, start=1)
            if str(idx) not in checkpoint_data
        ]

        # Process slides in parallel
        results = {}
        if slide_infos:  # Only process if there are unprocessed slides
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                futures = [executor.submit(process_slide, info) for info in slide_infos]
                for future in as_completed(futures):
                    idx, content = future.result()
                    results[idx] = content
                    
                    # Update checkpoint after each slide
                    checkpoint_data[str(idx)] = content
                    save_checkpoint(checkpoint_file, checkpoint_data)
        
        # Merge with previously processed slides
        results.update({int(k): v for k, v in checkpoint_data.items()})
        results = dict(sorted(results.items()))
        
        # Save final markdown
        markdown_file = save_markdown(unit_index, results)
        logger.info(f"✅ Completed Unit {unit_index}: {markdown_file}")
        
    except Exception as e:
        logger.error(f"Failed to process unit {unit_index}: {str(e)}")
        raise

def main():
    """Main processing loop with progress tracking."""
    try:
        logger.info("Starting slide processing pipeline")
        logger.info(f"Processing units from: {OCR_ROOT}")
        logger.info(f"Using model: {MODEL_NAME}")
        
        for unit_index in range(1, len(ZIP_FILES) + 1):
            try:
                process_unit(unit_index)
            except Exception as e:
                logger.error(f"Unit {unit_index} failed, continuing with next: {str(e)}")
                continue
        
        logger.info("All units processed successfully")
    except KeyboardInterrupt:
        logger.info("Processing interrupted by user")
    except Exception as e:
        logger.error(f"Fatal error in main processing: {str(e)}")
        raise
    finally:
        logger.info("Processing completed")

if __name__ == "__main__":
    main()