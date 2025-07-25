# Unit 6

## Slide 1

```markdown
---
*Slide 1*
---

# Unit 6: Application Layer
```

## Slide 2

```markdown
---
*Slide 1*
---

# DNS (Domain Name Space)

- Client/server programs divided in two categories
    - Directly used by user (email)
    - DNS is supported program that used by the other programs like email
```

## Slide 3

```markdown
---
*Slide 1*
---

# Using the DNS service

- SMTP: Simple Mail Transfer Protocol (e-mail)
- DNS: Domain Name System

> *Process Flow:*
> 1. User sends email to aperson@wonderful.com
> 2. SMTP client queries DNS client for wonderful.com
> 3. DNS client resolves to IP 200.200.200.5
> 4. SMTP client communicates with DNS client using resolved IP

- Application layer: SMTP client
- Transport layer: IP 200.200.200.5
```

## Slide 4

```markdown
---
*Slide [N]*
---

# Cont...

- Example of how a DNS client/server program can support an e-mail program to find the IP address of an e-mail recipient.
- A user of an e-mail program may know the e-mail address of the recipient; however, the IP protocol needs the IP address.
- The DNS client program sends a request to a DNS server to map the e-mail address to the corresponding IP address.
- To identify an entity, TCP/IP protocols use the IP address. However, people prefer to use names instead of numeric addresses. Therefore, we need a system that can map a name to an address or an address to a name.
- Solutions:
    - Host file (name and address) on each host
    - Host file in single computer and allow to access centralized information to every computer that needs to mapping.
    - Divide this huge amount of information into smaller parts and store each part on a different computer.
        - Host that needs mapping can contact the closest computer holding the needed information. (Method used by DNS)
```

## Slide 5

```markdown
---
*Slide 1*
---

# Name Space

- To be unambiguous, the name must be unique because the addresses are unique.
- **Mapping name with address can be done using two ways**:
    - Flat Name Space
    - Hierarchical Name Space

## FLAT NAME SPACE
- A name is assigned to an address
- Disadvantage
    - It cannot be used in a large system such as the Internet because it must be centrally controlled to avoid ambiguity and duplication.
```

## Slide 6

```markdown
---
*Slide 1*
---

# Hierarchical Name Space

- Name is made of several parts
    - First part defines Nature of the organization, second part defines Name of an organization, third part defines Departments in the organization, and so on.

- Example:
    - Two colleges and one company call one computer *Challenger*
    - 1st college name vnsgu.edu
    - 2nd college name bmiit.edu
    - Company given name smart.com
        - challenger.vnsgu.edu
        - challenger.bmiit.edu
        - challenger.smart.com
```

## Slide 7

```markdown
---
*Slide 1*
---

# DOMAIN NAME SPACE

- To have a hierarchical name space, a domain name space was designed. In this design, the names are defined in an inverted-tree structure with the root at the top. The tree can have only 128 levels: level 0 (root) to level 127.

> *Visual Explanation:*
> - Diagram of an inverted-tree structure
> - Root at the top branching into various domains such as arpa, com, edu, org, ad, zw
> - Each branch further divides into subdomains
```

## Slide 8

```markdown
---
*Slide [N]*
---

# Cont...

- **Label**
    - Each node in the tree has a label, which is a string with a maximum of 63 characters. The root label is a null string. DNS requires that children of a node have different labels, which guarantees the uniqueness of the domain names.

- **Domain Name**
    - Each node in the tree has a domain name. A full domain name is a sequence of labels separated by dots (.). The domain names are always read from the node up to the root.
    - The last label is the label of the root (null). This means that a full domain name always ends in a null label, which means the last character is a dot because the null string is nothing.

- **Fully Qualified Domain Name**
    - If a label is terminated by a null string, it is called a fully qualified domain name (FQDN).
    - An FQDN is a domain name that contains the full name of a host. It contains all labels, from the most specific to the most general, that uniquely define the name of the host.

- **Partially Qualified Domain Name**
    - If a label is not terminated by a null string, it is called a partially qualified domain name (PQDN).
    - A PQDN starts from a node, but it does not reach the root.
    - It is used when the name to be resolved belongs to the same site as the client.
```

## Slide 9

```markdown
---
*Slide 1*
---

# Domain Name Structure

- Hierarchical Components:
    - Root
    - edu
    - fhda
    - atc
    - challenger

> *Domain Explanation:*
> 1. Root → edu
> 2. edu → fhda.edu. (Domain name)
> 3. fhda → atc.fhda.edu. (Domain name)
> 4. atc → challenger.atc.fhda.edu. (Domain name)

> *Visual Explanation:*
> - Labels indicate hierarchy
> - Arrows show direction from root to specific domain names
> - Each level adds specificity to the domain

---
*End of Document*
---
```

## Slide 10

```markdown
---
*Slide 1*
---

# Domain

- A domain is a subtree of the domain name space
    - The name of the domain is the domain name of the node at the top of the subtree.
    - Domain may itself divide into domains (subdomains as they are sometimes called).

> *Visual Explanation:*
> - Diagram shows hierarchical structure of domains and subdomains.
> - Arrows indicate the division into subdomains.
> - Example domains: .com, .edu

---
*End of Document*
---
```

## Slide 11

```markdown
---
*Slide 1*
---

# DISTRIBUTION OF NAME SPACE

- The information contained in the domain name space must be stored. However, it is very inefficient and also unreliable to have just one computer store such a huge amount of information.

> *Visual Explanation:*
> - Diagram of a hierarchical structure
> - Root server at the top
> - Branches to arpa server, edu server, com server, us server
> - Further branches to specific domains like fhda.edu, bk.edu, mcgraw.com, irwin.com
> - Flow is top-down from root to specific domains
```

## Slide 12

```markdown
---
*Slide [N]*
---

# Cont...

- Complete domain name hierarchy cannot be stored on a single server, it is divided among many servers. What a server is responsible for or has authority over is called a zone.
- If a server accepts responsibility for a domain and does not divide the domain into smaller domains, the *domain* and the *zone* refer to the same thing.

> *Visual Explanation:*
> - Diagram shows hierarchical structure
> - Root at the top, branching into zones and domains
> - Flow from root to domain and zone
```

## Slide 13

```markdown
---
*Slide 1*
---

# Primary and Secondary Servers

- A primary server is a server that stores a file about the zone for which it is an authority.
- A secondary server is a server that transfers the complete information about a zone from another server (primary or secondary).
- A primary server loads all information from the disk file; the secondary server loads all information from the primary server. When the secondary downloads information from the primary, it is called zone transfer.
```

## Slide 14

```markdown
---
*Slide 1*
---

# DNS IN THE INTERNET

- **Generic Domains**
  - The generic domains define registered hosts according to their generic behaviour.
- **Country Domains**
  - The country domains section uses two-character country abbreviations.
- **Inverse Domain**
  - The inverse domain is used to map an address to a name.
```

## Slide 15

```markdown
---
*Slide 1*
---

# Domain Hierarchy

> *Visual Explanation:*
> - Diagram shows a hierarchical structure.
> - Root node at the top connects to three main categories:
>   1. Inverse domain
>   2. Generic domains
>   3. Country domains
> - Each category contains sub-nodes.
> - Flow is top-down from the root to sub-nodes.

---
*End of Document*
---
```

## Slide 16

```markdown
---
*Slide 1*
---

# Generic Domain

> *Visual Explanation:*
> - Diagram of domain hierarchy
> - Root level connects to various top-level domains (e.g., aero, biz, com)
> - Specific path highlighted: edu → fhda → atc → chal
> - Final address: chal.atc.fhda.edu
> - Flow direction: top to bottom

*Generic domains*
```

## Slide 17

```markdown
---
*Slide 1*
---

# Generic Domain Labels

| Label   | Description                                      |
|---------|--------------------------------------------------|
| aero    | Airlines and aerospace companies                 |
| biz     | Businesses or firms (similar to “com”)           |
| com     | Commercial organizations                         |
| coop    | Cooperative business organizations               |
| edu     | Educational institutions                         |
| gov     | Government institutions                          |
| info    | Information service providers                    |
| int     | International organizations                      |
| mil     | Military groups                                  |
| museum  | Museums and other nonprofit organizations        |
| name    | Personal names (individuals)                     |
| net     | Network support centers                          |
| org     | Nonprofit organizations                          |
| pro     | Professional individual organizations            |

---
*End of Document*
---
```

## Slide 18

```markdown
---
*Slide 1*
---

# Country Domain

> *Visual Explanation:*
> - Root level connects to various country codes (e.g., ae, fr, us, zw).
> - Hierarchical structure:
>   - "us" leads to "ca", then "cup", and finally "anza".
> - Example domain: `anza.cup.ca.us`
> - Represents index to addresses within country domains.

---
*End of Document*
---
```

## Slide 19

```markdown
---
*Slide 1*
---

# Inverse domain

> *Visual Explanation:*
> - Diagram of inverse domain hierarchy
> - Root level at the top
> - Hierarchical structure:
>   - arpa
>   - in-addr
>   - 132
>   - 34
>   - 45
>   - 121
> - Final node: 121.45.34.132.in-addr.arpa
> - Represents index to names
```

## Slide 20

```markdown
---
*Slide 1*
---

# RESOLUTION

- Mapping a name to an address or an address to a name is called name-address resolution.

---
*End of Document*
---
```

## Slide 21

```markdown
---
*Slide 1*
---

# HTTP

- *The Hypertext Transfer Protocol (HTTP) is a protocol used mainly to access data on the World Wide Web. HTTP functions as a combination of FTP and SMTP.*
- **HTTP uses the services of TCP on well-known port 80.**

> *Visual Explanation:*
> - Diagram shows a client-server interaction.
> - Request and response flow from client to server and back.

---
*End of Document*
---
```

## Slide 22

```markdown
---
*Slide 1*
---

# Methods

| Method  | Action                                                                 |
|---------|------------------------------------------------------------------------|
| GET     | Requests a document from the server                                    |
| HEAD    | Requests information about a document but not the document itself      |
| POST    | Sends some information from the client to the server                   |
| PUT     | Sends a document from the server to the client                         |
| TRACE   | Echoes the incoming request                                            |
| CONNECT | Reserved                                                               |
| OPTION  | Inquires about available options                                       |

---
*End of Document*
---
```

## Slide 23

```markdown
---
*Slide 1*
---

# Status Codes

| Code | Phrase     | Description                                                                 |
|------|------------|-----------------------------------------------------------------------------|
| 100  | Continue   | The initial part of the request has been received, and the client may continue with its request. |
| 101  | Switching  | The server is complying with a client request to switch protocols defined in the upgrade header. |
| 200  | OK         | The request is successful.                                                   |
| 201  | Created    | A new URL is created.                                                        |
| 202  | Accepted   | The request is accepted, but it is not immediately acted upon.               |
| 204  | No content | There is no content in the body.                                             |

---
*End of Document*
---
```

## Slide 24

```markdown
---
*Slide [N]*
---

# Cont...

| Code | Phrase                | Description                                                      |
|------|-----------------------|------------------------------------------------------------------|
| 301  | Moved permanently     | The requested URL is no longer used by the server.               |
| 302  | Moved temporarily     | The requested URL has moved temporarily.                         |
| 304  | Not modified          | The document has not been modified.                              |

**Redirection**

| 400  | Bad request           | There is a syntax error in the request.                          |
| 401  | Unauthorized          | The request lacks proper authorization.                          |
| 403  | Forbidden             | Service is denied.                                               |
| 404  | Not found             | The document is not found.                                       |
| 405  | Method not allowed    | The method is not supported in this URL.                         |
| 406  | Not acceptable        | The format requested is not acceptable.                          |

**Client Error**

| 500  | Internal server error | There is an error, such as a crash, at the server site.          |
| 501  | Not implemented       | The action requested cannot be performed.                        |
| 503  | Service unavailable   | The service is temporarily unavailable, but may be requested in the future. |

**Server Error**
```

## Slide 25

```markdown
---
*Slide 1*
---

# REMOTE LOGGING

- *It would be impossible to write a specific client/server program for each demand. The better solution is a general-purpose client/server program that lets a user access any application program on a remote computer.*
- **TELNET is a general-purpose client/server application program.**

---
*End of Document*
---
```

## Slide 26

```markdown
---
*Slide 1*
---

# Local and Remote Login

> *Visual Explanation:*
> - **Diagram a: Local log-in**
>   - Terminal connects directly to the operating system.
>   - Terminal driver interfaces with application programs.
> - **Diagram b: Remote log-in**
>   - Terminal connects via TELNET client over the Internet.
>   - TELNET server interfaces with application programs.
>   - Uses TCP/IP protocol stack for communication.
```

## Slide 27

```markdown
---
*Slide 1*
---

# Electronic Mail

- *One of the most popular Internet services is electronic mail (e-mail). The designers of the Internet probably never imagined the popularity of this application program.*
```

## Slide 28

```markdown
---
*Slide 1*
---

# Format of Email

- **Postal Mail:**
  - Behrouz Forouzan
  - De Anza College
  - Cupertino, CA 96014
  - Sophia Fegan
  - Com-Net
  - Cupertino, CA 95014

- **Electronic Mail:**
  - Mail From: forouzan@deanza.edu
  - RCPT To: fegan@comnet.com

> *Visual Explanation:*
> - Diagram shows the structure of postal and electronic mail.
> - Postal mail includes sender and recipient addresses.
> - Electronic mail includes email addresses for sender and recipient.
> - Both formats include a header and message body.

> Note: The diagram illustrates the components of an envelope, header, and message in both postal and electronic formats.
```

## Slide 29

```markdown
---
*Slide 1*
---

# Email Address

- Components:
    - Local part
    - Domain name

> *Visual Explanation:*
> - The local part is the address of the mailbox on the mail server.
> - The domain name is the domain name of the mail server.

---
*End of Document*
---
```

