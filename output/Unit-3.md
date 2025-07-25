# Unit 3

## Slide 1

```markdown
---
*Slide 3*
---

# Ethernet

---
*End of Document*
---
```

## Slide 2

```markdown
---
*Slide 1*
---

# IEEE Standard

- IEEE started a project, called **Project 802** to set standard to enable intercommunication among equipment from variety of manufacturers.
- IEEE has subdivided the data link layer into two sublayers: Logical Link Control (LLC) and Media Access Control (MAC).
- IEEE has also created several physical layer standards for different LAN protocols.

> *Visual Explanation:*
> - Diagram shows the subdivision of layers:
>   - Upper layers
>   - Data link layer (LLC)
>   - Physical layer
> - Media Access Control (MAC) includes:
>   - Ethernet MAC
>   - Token Ring MAC
>   - Token Bus MAC
> - Physical layer includes:
>   - Ethernet physical layers
>   - Token Ring physical layer
>   - Token Bus physical layer
> - Transmission medium connects all layers
```

## Slide 3

```markdown
---
*Slide 1*
---

# IEEE Standard

- Data link layer includes:
    - Two sublayers: LLC, MAC
    - Framing
    - Needs for LLC
- LLC - Logical Link Control
    - Data link control handles framing, flow control, and error control.
    - In IEEE project 802, flow control, error control, and part of the framing duties are collected into one sublayer called LLC.
    - *Framing is handled by both LLC and MAC.*

> *Note:*
> LLC provides one single data link control protocol for all IEEE LANs. MAC provides different protocols for different LANs.

- A single LLC protocol can provide interconnectivity between different LANs because it makes the MAC sublayer transparent.
```

## Slide 4

```markdown
---
*Slide 1*
---

# IEEE Standard

- Framing
    - LLC define PDU (Protocol Data Unit), somewhat similar to HDLC.
    - Header contain control field like HDLC, which is used for flow and error control.
    - The two header fields define the upper layer protocol at the source and destination that uses LLC. These fields are called **Destination Service Access Point (DSAP)** and **Source Service Access Point (SSAP)**.
    - A frame defined in HDLC is divide into PDU at the LLC sublayer and a frame at MAC sublayer.
    - HDLC (High Level Data Link Control)
    - FCS (Frame Check Sequence)

> *Visual Explanation:*
> - Diagram shows the structure of HDLC and MAC frames.
> - DSAP and SSAP are part of the LLC PDU.
> - Flow: Address → Control → Upper-layer data → FCS

> Note: DSAP: Destination service access point, SSAP: Source service access point
```

## Slide 5

```markdown
---
*Slide 1*
---

# IEEE Standard

- Need for LLC
    - The purpose of the LLC is to provide flow and error for the upper layer protocol.
    - Example: If a LAN or several LANs are used in isolated system.
        - LLC may be needed to provide flow and error control for the application layer protocols.

> *Visual Explanation:*
> - Diagram of Multiple-access protocols
> - Categories:
>   - Random access protocols: ALOHA, CSMA, CSMA/CD, CSMA/CA
>   - Controlled-access protocols: Reservation, Polling, Token passing
>   - Channelization protocols: FDMA, TDMA, CDMA
> - Flow from Multiple-access protocols to specific types
```

## Slide 6

```markdown
---
*Slide 1*
---

# IEEE Standard

- Media Access Control
    - It defines the specific access method for each LAN.
    - Part of framing function is also handled by the MAC layer.
- Physical layer
    - It is dependent on the implementation and type of physical media used.
    - IEEE defines detailed specification for each LAN implementation.
- Summary
    - Ethernet is a most widely used local area network.
    - The data link layer of Ethernet consists of LLC sub layer and MAC sublayer.
    - MAC sublayer is responsible for the operation of CSMA/CD access method and framing.

---
*End of Document*
---
```

## Slide 7

```markdown
---
*Slide 1*
---

# Standard Ethernet

- Ethernet evolution through four generations

> *Ethernet Evolution Diagram:*
> - Standard Ethernet: 10 Mbps
> - Fast Ethernet: 100 Mbps
> - Gigabit Ethernet: 1 Gbps
> - Ten-Gigabit Ethernet: 10 Gbps

- The original Ethernet was created in 1976 at Xerox’s Palo Alto Research Center (PARC).
- From that time it has gone through four generations: Standard Ethernet (10Mbps), Fast Ethernet (100Mbps), Gigabit Ethernet (1Gbps), and Ten-Gigabit Ethernet (10Gbps).
- Topics discussed in this section are:
    - MAC sublayer
    - Physical Layer
```

## Slide 8

```markdown
---
*Slide 1*
---

# Standard Ethernet

- **MAC sub layer**
  - MAC sublayer governs the operation of the access method.
  - It also frames data received from the upper layer and passes them to the physical layer.
  - **Frame Format**:
    - It contains 7 fields.
    - Ethernet does not provide any mechanism for acknowledging receiving frames, so it is unreliable.
    - Acknowledgement must be implemented at the higher layers.

> *Visual Explanation:*
> - **Preamble**: 56 bits of alternating 1s and 0s.
> - **SFD**: Start frame delimiter, flag (10101011)
> - Diagram shows the structure of an Ethernet frame with fields:
>   - Preamble: 7 bytes
>   - SFD: 1 byte
>   - Destination address: 6 bytes
>   - Source address: 6 bytes
>   - Length or type: 2 bytes
>   - Data and padding
>   - CRC: 4 bytes
> - Flow direction indicated by arrow pointing left
```

## Slide 9

```markdown
---
*Slide 1*
---

# Standard Ethernet

## MAC Frame (802.3)

- **Preamble**: 56 bits of alternating 0s and 1s.
    - 56 bits alerts receiving system to the coming frame and enables it to synchronizing its input timing.
    - Pattern provides only an alert and a timing pulse.
    - Preamble is actually added at the physical layer and is not (formally) part of the frame.
- **SFD (Start Frame Delimiter)**
    - Signals beginning of the frame.
    - It warns station that this is last chance for synchronization.
    - Last bit is 11 and alerts the receiver that the next field is the destination address.
- **DA (Destination Address)**
    - 6 byte field and contains the physical address of the destination stations to receive the packet.
- **SA (Source Address)**
    - 6 byte field and contains the physical address of the sender of the packet.
```

## Slide 10

```markdown
---
*Slide [N]*
---

# Standard Ethernet

- MAC Frame (802.3) (Cont...)
    - Length or type
        - The original Ethernet used this field as the type field that define the upper-layer protocol using the MAC frame.
        - IEEE standard used it as the length field to define the number of bytes in the data field.
    - Data:
        - Data encapsulated from the upper-layer protocol.
        - Minimum 46 and maximum 1500 bytes.
    - CRC:
        - Carries error detection information.
```

## Slide 11

```markdown
---
*Slide 1*
---

# Standard Ethernet

- Frame Length:
  - Minimum payload length: 46 bytes
  - Maximum payload length: 1500 bytes

| Destination address | Source address | Length PDU | Data and padding | CRC |
|---------------------|----------------|------------|------------------|-----|
| 6 bytes             | 6 bytes        | 2 bytes    |                  | 4 bytes |

- Minimum frame length: 512 bits or 64 bytes
- Maximum frame length: 12,144 bits or 1518 bytes

> *Visual Explanation:*
> - Frame length ranges from 64 bytes to 1518 bytes
> - Includes destination and source addresses, length PDU, data, padding, and CRC
```

## Slide 12

```markdown
---
*Slide 1*
---

# Standard Ethernet

- Addressing
    - Each station on an Ethernet network has its own Network Interface Card (NIC).
    - NIC fits inside the station and provides the station with a 6-byte physical address which is normally written in hexadecimal notation with colon between bytes.

> *Visual Explanation:*
> - Example Address: `06:01:02:01:2C:4B`
> - 6 bytes = 12 hex digits = 48 bits

- Unicast and Multicast addresses
    - Unicast: 0; multicast: 1

> *Diagram Description:*
> - Byte 1 shows the distinction between unicast and multicast.
> - Byte 2 to Byte 6 follow.

---
*End of Document*
---
```

## Slide 13

```markdown
---
*Slide 1*
---

# Standard Ethernet

## Addressing (Cont...)

- A source address is always a unicast address because frame comes only from one station.
- The destination address can be unicast, multicast or broadcast.
- **If least significant bit of the first byte in destination address is 0 then it is unicast otherwise multicast.**
- **The broadcast address is a special case of the multicast address, the recipients are all the station on the LAN. A broadcast destination address is forty-eight 1s.**
- unicast :- one – to one
- Broadcast :- one – to many
```

## Slide 14

```markdown
---
*Slide 1*
---

# Standard Ethernet

**Que**: Define the type of the following destination addresses:
- a. 4A:30:10:21:10:1A
- b. 47:20:1B:2E:08:EE
- c. FF:FF:FF:FF:FF:FF

*Solution*

- To find the type of the address, we need to look at the second hexadecimal digit from the left.
    - If it is even, the address is unicast.
    - If it is odd, the address is multicast.
    - If all digits are F’s, the address is broadcast.

a. This is a unicast address because A in binary is 1010 (Even).

b. This is a multicast address because 7 in binary is 0111 (Odd).

c. This is a broadcast address because all digits are F’s.
```

## Slide 15

```markdown
---
*Slide 1*
---

# Standard Ethernet

- *Show how the address* 47:20:1B:2E:08:EE *is sent out on line.*

**Solution**

- The address is sent left-to-right, byte by byte; for each byte, it is sent right-to-left, bit by bit, as shown below:

> *Visual Explanation:*
> - The binary sequence is displayed with an arrow indicating the direction of bit transmission.
> - Sequence: 11100010 00000100 11011000 01110100 00010000 01110111

---
*End of Document*
---
```

## Slide 16

```markdown
---
*Slide 1*
---

# Standard Ethernet

- **Physical layer:**
  - It defines several physical layer implementations.

> *Diagram Explanation:*
> - Standard Ethernet common implementations
>   - 10Base5: Bus, thick coaxial
>   - 10Base2: Bus, thin coaxial
>   - 10Base-T: Star, UTP
>   - 10Base-F: Star, fiber

- **Encoding and Decoding:**
    - All implementations use digital signaling at 10 Mbps.
    - At the sender, data are converted to a digital signal using Manchester Scheme.
    - At the receiver, the received signal is interpreted as Manchester and decoded onto data.
    - *(Manchester encoding is self-synchronous, providing a transition at each bit interval.)*
```

## Slide 17

```markdown
---
*Slide 1*
---

# Standard Ethernet

- **10Base5: Thick Ethernet**
    - 1st implementation is called **10Base5 Thick Ethernet** or Thicknet.
    - The name derives from size of the cable.
    - It is too hard to bend with your hand.

> *Visual Explanation:*
> - Diagram shows data flow from Station to Manchester encoder and decoder.
> - Data rate: 10 Mbps.
> - Connection via twisted pairs or fibers.
```

## Slide 18

```markdown
---
*Slide 1*
---

# Standard Ethernet

- Characteristics:
    - It uses bus topology with external transceiver connected via a tap to a thick coaxial cable.
- **The transceiver is responsible for transmitting, receiving, and detecting collision.**
- Connected to a station via transceiver cable that provides separate path for sending and receiving.
- This means collision can only occur in coaxial cable.

> *Visual Explanation:*
> - Diagram shows a 10Base5 Ethernet setup.
> - Baseband (digital) with 10 Mbps over 500 m.
> - Transceiver cable maximum 50 m.
> - Thick coaxial cable maximum 500 m.
```

## Slide 19

```markdown
---
*Slide 1*
---

# Standard Ethernet

- **10Base2: Thin Ethernet**
    - 2nd implementation is called 10Base2, Thin Ethernet or Chepernet.
    - It also uses bus topology, but cable is much thinner and more flexible.

> *Visual Explanation:*
> - Diagram shows a network setup using 10Base2.
> - Data rate: 10 Mbps
> - Maximum cable length: 185 m
> - Uses thin coaxial cable with baseband (digital) signaling.
> - Cable ends are marked and connected to devices.

---
*End of Document*
---
```

## Slide 20

```markdown
---
*Slide 1*
---

# Standard Ethernet

- Characteristics:
    - The cable can be bent to pass very close to the station.
    - In this case, the transceiver is normally part of the NIC, which is installed inside the station.
    - The collision occurs in thin Ethernet.
    - Its implementation is more cost-effective than 10Base5.
    - Installation is simpler because the thin coaxial cable is very flexible.
- 10BaseT: Twisted Pair Ethernet
    - 3rd implementation is called 10BaseT or twisted-pair Ethernet.

> *Visual Explanation:*
> - Diagram shows a 10Base-T setup with twisted pair cables.
> - Baseband (digital) connection at 10 Mbps.
> - Two pairs of UTP cable connect to a 10Base-T hub.
```

## Slide 21

```markdown
---
*Slide 1*
---

# Standard Ethernet

- Characteristics:
    - It uses physical star topology, stations are connected with hub via 2 pairs of twisted cable.
    - Two pairs of twisted pair cable create two paths (one for sending and one for receiving) between the station and the hub.
    - Collision happens in HUB.
    - Compared to 10Base5 and 10Base2, hub actually replaces the coaxial cable as far as collision concern.
    - Maximum length of the twisted cable is 100m.

- 10BaseF: Fiber Ethernet
    - 4th implementation is called **10BaseF or Fiber Ethernet**.

> *Visual Explanation:*
> - Diagram shows a 10Base-F setup with fiber-optic cables connecting to a hub.
> - Data rate: 10 Mbps
> - Baseband (digital) transmission
> - Two fiber-optic cables connect to the 10Base-F hub
```

## Slide 22

```markdown
---
*Slide 1*
---

# Standard Ethernet

- Characteristics:
    - It is a type of optical fiber 10-Mbps Ethernet.
    - It uses star topology to connect station to hub.
    - Stations are connected to hub using 2 fiber-optic cables.
    - Maximum length of the Fiber cable is 2000m.

| Characteristics   | 10Base5            | 10Base2           | 10Base-T | 10Base-F |
|-------------------|--------------------|-------------------|----------|----------|
| Media             | Thick coaxial cable| Thin coaxial cable| 2 UTP    | 2 Fiber  |
| Maximum length    | 500 m              | 185 m             | 100 m    | 2000 m   |
| Line encoding     | Manchester         | Manchester        | Manchester| Manchester|

---
*End of Document*
---
```

## Slide 23

```markdown
---
*Slide 1*
---

# Fast Ethernet

- Fast Ethernet was designed to compete with LAN protocols.
- It is also known as 802.3u.
- It can transmit data 10 times faster at a rate of 100Mbps.
- Goals of Fast Ethernet
    - Upgrade the data rate to 100 Mbps.
    - Make it compatible with standard Ethernet.
    - Keep the same 48-bit address.
    - Keep the same frame format.
    - Keep the same minimum and maximum lengths.
- **MAC sub layer**
    - It uses star topology.
    - For star topology there are 2 choices: Half-Duplex and Full-Duplex.
```

## Slide 24

```markdown
---
*Slide 1*
---

# Fast Ethernet

| Half Duplex                                      | Full Duplex                                           |
|--------------------------------------------------|-------------------------------------------------------|
| Stations are connected via hub.                  | The connection is made via switch with buffers at each port. |
| The access method is same (CSMA/CD) for half duplex approach. | For full duplex fast Ethernet, there is no need for CSMA/Cd. |

- **Autonegotiation**
    - It allows two devices to negotiate the mode or data rate of operation. It was designed particularly for the following purposes:
        - To allow incompatible devices to connect one another.
        - To allow one device to have multiple capabilities.
        - To allow a station to check a hub’s capabilities.
- **Physical Layer**
    - Physical layer in Fast Ethernet is more compatible than standard Ethernet.
    - **Fast Ethernet Topology**
        - Fast Ethernet is designed to connect two or more stations together.
        - If there are only two stations, they can be connected by point-to-point network.
        - Three or more stations need to be connected in a star topology with a hub or a switch at the center.

---
*End of Document*
---
```

## Slide 25

```markdown
---
*Slide 1*
---

# Fast Ethernet

- **Implementation**
    - It implementation at physical layer can be categorized as either two-wire or four-wire.
    - 2 wire implementation can be
        - Category-5 UTP (100Base-TX)
        - Fiber-optic cable (100Base-FX)
    - 4 wire implementation is designed for
        - Category-3 UTP (100Base-T4)

> *Visual Explanation:*
> - Diagram a: Point-to-point connection between two computers.
> - Diagram b: Star topology with a switch connecting multiple computers.
```

## Slide 26

```markdown
---
*Slide 1*
---

# Fast Ethernet

- 100Base-TX
    - It uses 2 twisted pair cable (Either category 5 UTP or STP).
- 100Base-FX
    - It uses two pairs of fiber optic cable.
    - Optical fiber can easily meet high bandwidth requirements by using a simple encoding scheme.
- 100Base-T4
    - 100Base-T4 uses category-3 or higher UTP.
    - It uses 4 cables of UTP for transmitting 100Mbps.

> *Visual Explanation:*
> - Diagram shows common Fast Ethernet implementations.
> - 100Base-TX: Two wires, category 5 UTP
> - 100Base-FX: Two wires, fiber
> - 100Base-T4: Four wires, category 3 UTP
```

## Slide 27

```markdown
---
*Slide 1*
---

# Gigabit Ethernet

- The need for an even higher data rate resulted in the design of the Gigabit Ethernet protocol (1000 Mbps).
- The IEEE committee calls the standard **802.3z**.
- Goal:
    - Upgrade data rate to 1 Gbps.
    - Make it compatible with standard or Fast Ethernet.
    - Use same 48 bit address.
    - Use same frame format.
    - Keep same maximum and minimum frame length.
    - To support Autonegotiation as defined in Fast Ethernet.
- **MAC Sublayer**
- Gigabit Ethernet has 2 distinctive approaches for medium access:
    - Half duplex
    - Full duplex.
- Almost all implementation of gigabit follows full duplex mode.
- Half duplex approach to show that gigabit Ethernet can be compatible with the previous generation
```

## Slide 28

```markdown
---
*Slide 1*
---

# Gigabit Ethernet

- **Full Duplex**
    - In this, central switch connected to all computer or other switch.
    - In this mode, each switch has buffers for each input port in which data are stored until they are transmitted.
    - So there is no collision, it means that there is no CSMA/CD is used.

> *Note:*
> In the full duplex mode of gigabit Ethernet, there is no collision; the maximum length of cable is determined by the signal attenuation in the cable.

- **Half Duplex**
    - In this mode switch can be replaced by hub, which acts as the common cable in which collision might occur.
    - It used CSMA/CD protocol.
    - Maximum length of network is dependent on the minimum frame size.
    - Three methods:
        - Traditional
        - Carrier Extension
        - Frame Bursting

---
*End of Document*
---
```

## Slide 29

```markdown
---
*Slide 1*
---

# Gigabit Ethernet

- Traditional
    - We keep the minimum length of the frame as in traditional Ethernet (512 bits).
    - Maximum length of the network is 25m.
    - It is suitable if all stations are in one room.
    - It may not even be long enough to connect the computer in one office.
- Carrier Extension
    - To allow long network, we increase minimum frame length.
    > Note: The carrier Extension approach defines the minimum length of a frame as 512 bytes. This means that the minimum length is 8 times longer.
    - This method forces a station to add extension bits to any frame that is less than 4096 bits.
    - This allows a length of 100m from the hub to the station.

---
*End of Document*
---
```

## Slide 30

```markdown
---
*Slide 1*
---

# Gigabit Ethernet

- Frame Bursting
    - Carrier extension is very inefficient if we have a series of short frames to send, each frame carries redundant bit.
    - **Instead of adding an extension to each frame, multiple frames are sent.**
    - To make these multiple frames look like one frame, extra bit is added between the frames so that channel is not idle.
    - In other words, the method deceives other stations into thinking that a very large frame has been transmitted.

- Physical layer topology
    - 2 Stations
        - Point to point
    - 3 or more:
        - Star topology with hub or switch
    - 2 or more star topology
```

## Slide 31

```markdown
---
*Slide 1*
---

# Gigabit Ethernet

- Network Topologies:
  - a. Point-to-point
  - b. Star
  - c. Two stars
  - d. Hierarchy of stars

> *Visual Explanation:*
> - Diagram a: Direct connection between two devices.
> - Diagram b: Central switch connects multiple devices.
> - Diagram c: Two switches each connecting multiple devices.
> - Diagram d: Hierarchical structure with a main switch connecting to other switches.
```

## Slide 32

```markdown
---
*Slide 1*
---

# Gigabit Ethernet

- Implementation
- It does not use Manchester encoding scheme because it involves a very high bandwidth

> *Diagram Explanation:*
> - Gigabit Ethernet implementations:
>   - 1000Base-SX: Two-wire short-wave fiber
>   - 1000Base-LX: Two-wire long-wave fiber
>   - 1000Base-CX: Two-wire copper (STP)
>   - 1000Base-T: Four-wire UTP

| Characteristics   | 1000Base-SX | 1000Base-LX | 1000Base-CX | 1000Base-T |
|-------------------|-------------|-------------|-------------|------------|
| Media             | Fiber short-wave | Fiber long-wave | STP         | Cat 5 UTP |
| Number of wires   | 2           | 2           | 2           | 4          |
| Maximum length    | 550 m       | 5000 m      | 25 m        | 100 m      |
| Block encoding    | 8B/10B      | 8B/10B      | 8B/10B      | 4D-PAM5    |
| Line encoding     | NRZ         | NRZ         | NRZ         | 4D-PAM5    |

---
*End of Document*
---
```

