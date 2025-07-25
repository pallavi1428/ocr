# Unit 5

## Slide 1

```markdown
---
*Slide 1*
---

# UNIT 5

Transport layer

---
*End of Document*
---
```

## Slide 2

```markdown
---
*Slide 1*
---

# Unit Covered

- Process to process delivery
- UDP – User datagram protocol
- TCP – Transmission Control protocol
```

## Slide 3

```markdown
---
*Slide 1*
---

# Process To Process Delivery

- Datalink Layer: node-to-node delivery (frame) (delivery of frame between two neighboring nodes over a link).
- Network Layer: host-to-host delivery (datagram)
- Transport Layer is responsible for process-to-process delivery (application Program)
    - The delivery of a packet, part of a message, from one process to another.
- Two processes communicate in a client/server relationship.
```

## Slide 4

```markdown
---
*Slide 1*
---

# Note

> The transport layer is responsible for process-to-process delivery.
```

## Slide 5

```markdown
---
*Slide 1*
---

# Types of Data Deliveries

- Node to node: Data link layer
- Host to host: Network layer
- Process to process: Transport layer

> *Visual Explanation:*
> - Diagram shows data delivery types across the internet.
> - Flow from node to node, host to host, and process to process.
> - Illustrates layers involved in data transmission.

---
*End of Document*
---
```

## Slide 6

```markdown
---
*Slide 1*
---

# Client/Server Paradigm

- To achieve process-to-process communication
    - Client/Server paradigm is used.
- Process on local host called **Client**, needs services from process usually on the remote host, called **Server**.
- Both processes have same name.
- Remote computer can run several server programs at the same time.
- Local host can run one or more client programs at the same time.
```

## Slide 7

```markdown
---
*Slide 1*
---

# Client/Server Paradigm

- For communication we must define following:
    - Local Host
    - Local Process
    - Remote Host
    - Remote Process
```

## Slide 8

```markdown
---
*Slide [N]*
---

# Addressing

- At data link layer we need MAC address.
- At network address we need IP address.
- Transport layer address is called **port number**, to choose among multiple processes running on the destination host.
- Port numbers are 16-bit integers between 0-65535.
- The client program defines itself with a port number, chosen randomly by the transport layer software running on the client host called **ephemeral port number**.
- The server port number is defined by itself and cannot be chosen randomly.
- The Internet has decided to use universal port numbers for servers; these are called **well-known port numbers**.
```

## Slide 9

```markdown
---
*Slide 1*
---

# Port numbers

> *Visual Explanation:*
> - Diagram shows communication between a daytime client and server.
> - Client uses port 52,000 and server uses port 13.
> - Data flows from client to server and back, indicating bidirectional communication.
> - Transport layer is responsible for managing port numbers and data flow.
```

## Slide 10

```markdown
---
*Slide 1*
---

# IANA Ranges

- The IANA (Internet Assigned Number Authority) has divided port numbers as below:
    - **Well-known ports**: the ports ranging from 0 to 1023 are assigned and controlled by IANA.
    - **Registered Ports**: the ports ranging from 1024 to 49,151 are not assigned or controlled by IANA. They can only be registered with IANA to prevent duplication.
    - **Dynamic ports**: the ports ranging from 49,152 to 65,535 are neither controlled nor registered. They can be used by any process. These are the ephemeral ports.
```

## Slide 11

```markdown
---
*Slide 1*
---

# IP addresses versus port numbers

> *Visual Explanation:*
> - Diagram showing the relationship between IP addresses and port numbers.
> - IP header contains the IP address (193.14.26.7) which selects the host.
> - Transport layer header contains the port number (13) which selects the process.
> - Flow from IP header to transport layer header, indicating data routing.

---
*End of Document*
---
```

## Slide 12

```markdown
---
*Slide 1*
---

# Socket addresses

- Process to process delivery needs two identifiers: IP address and Port number.
- The combination of an IP address and port number is called a **socket address**.
- Transport layer protocol needs a pair of socket addresses: the client socket address and server socket address.

> *Visual Explanation:*
> - Diagram shows the combination of IP address `200.23.56.8` and Port number `69` forming a socket address.
```

## Slide 13

```markdown
---
*Slide 1*
---

# Multiplexing and Demultiplexing

> *Process Flow:*
> 1. Multiple processes are combined using a Multiplexer.
> 2. The combined data is sent through IP.
> 3. At the destination, a Demultiplexer separates the data back into individual processes.
> 4. Data flows from left to right for multiplexing and right to left for demultiplexing.
```

## Slide 14

```markdown
---
*Slide 1*
---

# Multiplexing and Demultiplexing

- At sender site, there may be several processes that need to send packets and there is only one transport layer protocol at any time.
- This is many-to-one relationship and requires multiplexing.
- The protocol accepts messages from different processes, differentiated by their port numbers. After adding the header, the transport layer passes the packet to the network layer.
- **At receiver side, the relationship is one-to-many and requires demultiplexing.**
- **The transport layer receives datagrams from the network layer. After error checking and dropping of header, the transport layer delivers each message to appropriate process based on the port number.**

---
*End of Document*
---
```

## Slide 15

```markdown
---
*Slide 1*
---

# Connectionless vs. Connection-Oriented Service

- **Connectionless Service**
    - Packets are sent from one party to another with no need for connection establishment or connection release.
    - Packets are not numbered: they may be delayed or lost or may arrive out of sequence.
    - There is no acknowledgement either.
    - UDP is a connectionless protocol.
```

## Slide 16

```markdown
---
*Slide 1*
---

# Connectionless vs. Connection-Oriented Service

- **Connection-Oriented Service**
    - In this service, connection is first established between the sender and receiver.
    - Data are transferred.
    - At the end, the connection is released.
    - TCP and SCTP are connection-oriented protocols.

---
*End of Document*
---
```

## Slide 17

```markdown
---
*Slide 1*
---

# Reliable vs. Unreliable

- **Reliable**
    - If the application layer program needs reliability, reliable transport layer protocol is used by implementing flow and error control.
    - This is slower and more complex service.
    - TCP is connection oriented and reliable.
```

## Slide 18

```markdown
---
*Slide 1*
---

# Reliable vs. Unreliable

- **Unreliable**
    - If the application layer program does not need reliability, because it uses its own flow and error control mechanism.
    - It needs fast service or the nature of the service does not demand flow and error control, then unreliable service can be used.
    - UDP is connectionless and unreliable.
```

## Slide 19

```markdown
---
*Slide 1*
---

# Error control

- Error is checked in these paths by the data link layer
- Error is not checked in these paths by the data link layer

> *Visual Explanation:*
> - Diagram shows error control paths in a network.
> - Pink lines indicate paths where error is checked.
> - Black lines indicate paths where error is not checked.
> - Components include Transport, Network, Data link, and Physical layers.
> - Flow from LAN through WAN to another LAN.

---
*End of Document*
---
```

## Slide 20

```markdown
---
*Slide 1*
---

# Position of UDP, TCP, and SCTP in TCP/IP suite

- **Application layer**:
    - SMTP
    - FTP
    - TFTP
    - DNS
    - SNMP
    - BOOTP
- **Transport layer**:
    - SCTP
    - TCP
    - UDP
- **Network layer**:
    - IGMP
    - ICMP
    - IP
    - ARP
    - RARP
- **Data link layer**:
    - Underlying LAN or WAN technology
- **Physical layer**:
    - [Not specified]

> *Visual Explanation:*
> - Diagram shows the hierarchical structure of the TCP/IP suite.
> - Layers are organized from Application to Physical.
> - Each layer contains specific protocols relevant to its function.
```

## Slide 21

```markdown
---
*Slide 1*
---

# UDP: User Datagram Protocol

- UDP is called **connectionless** and **unreliable** transport protocol.
- It does not add anything to services of IP except to provide process-to-process communication instead of host-to-host communication.
- It performs very limited checking.

- **Disadvantage**:
    - UDP is so powerless.
```

## Slide 22

```markdown
---
*Slide 1*
---

# Advantages of UDP

## Why would a Process want to use UDP?

- UDP is a very simple protocol using very minimum overhead.
- If a process wants to send a very small message and does not care about reliability, it is better to use UDP.
- Sending a small message by using UDP takes less interaction between the sender and receiver than using TCP.

---
*End of Document*
---
```

## Slide 23

```markdown
---
*Slide 1*
---

# Well-Known Port for UDP

| Port | Protocol | Description                                           |
|------|----------|-------------------------------------------------------|
| 7    | Echo     | Echoes a received datagram back to the sender         |
| 9    | Discard  | Discards any datagram that is received                |
| 11   | Users    | Active users                                          |
| 13   | Daytime  | Returns the date and the time                         |
| 17   | Quote    | Returns a quote of the day                            |
| 19   | Chargen  | Returns a string of characters                        |
| 53   | Nameserver | Domain Name Service                                 |
| 67   | BOOTPs   | Server port to download bootstrap information         |
| 68   | BOOTPc   | Client port to download bootstrap information         |
| 69   | TFTP     | Trivial File Transfer Protocol                        |
| 111  | RPC      | Remote Procedure Call                                 |
| 123  | NTP      | Network Time Protocol                                 |
| 161  | SNMP     | Simple Network Management Protocol                    |
| 162  | SNMP     | Simple Network Management Protocol (trap)             |

---
*End of Document*
---
```

## Slide 24

```markdown
---
*Slide 1*
---

# Example

- In UNIX, the well-known ports are stored in a file called `/etc/services`.
- Each line in this file gives the name of the server and the well-known port number.
- We can use the grep utility to extract the line corresponding to the desired application.
- The example shows the port for FTP.
- Note that FTP can use port 21 with either UDP or TCP.

> *Visual Explanation:*
> - Command: `$ grep ftp /etc/services`
> - Output:
>   - `ftp 21/tcp`
>   - `ftp 21/udp`
```

## Slide 25

```markdown
---
*Slide 1*
---

# User Datagram

- UDP packet called User datagram, have a fixed size header of 8 bytes.
- Figure shows the format of user datagram.

> *Visual Explanation:*
> - Diagram shows a UDP packet structure.
> - Header: 8 bytes
> - Data follows the header.
> - Components:
>   - Source port number: 16 bits
>   - Destination port number: 16 bits
>   - Total length: 16 bits
>   - Checksum: 16 bits
```

## Slide 26

```markdown
---
*Slide 1*
---

# User Datagram Format

- **Source port number**:
    - Port number used by the process running on the source port.
    - Range: 0 to 65535.
    - Source is client: ephemeral port, source host: well-known port.
- **Destination port number**:
    - Port number used by the process running on the destination port.
    - If server: client sending request.
    - If client: server sending a response.
- **Length**:
    - 16 bit length: total length of user datagram, header + Data.

$$
\text{UDP length} = \text{IP length} - \text{IP header's length}
$$

- **Checksum**:
    - This field used to detect error.
```

## Slide 27

```markdown
---
*Slide 1*
---

# Pseudoheader for checksum calculation

- Pseudoheader Components:
  - 32-bit source IP address
  - 32-bit destination IP address
  - All 0s
  - 8-bit protocol
  - 16-bit UDP total length

- Header Components:
  - Source port address: 16 bits
  - Destination port address: 16 bits
  - UDP total length: 16 bits
  - Checksum: 16 bits

- Data:
  - Padding must be added to make the data a multiple of 16 bits
```

## Slide 28

```markdown
---
*Slide 1*
---

# UDP Operation

- **Connectionless service**
    - Each user datagram sent by UDP is an independent datagram.
    - No connection established.
- **Flow control and Error control.**
    - No error and flow control mechanism except checksum.
    - Sender does not know if a message has been lost or duplicated. When receiver detects the error using checksum, user datagram discarded.
- **Encapsulation and Decapsulation**
    - To send a message from one process to another, the UDP encapsulates and decapsulates message in IP.
- **Queuing**
    - If a process wants to communicate with multiple processes, it obtains only one port number, one outgoing and one incoming queue.
```

## Slide 29

```markdown
---
*Slide [N]*
---

# Use of UDP

- UDP suitable for process that required simple request-response communication.
- UDP suitable for process with internal flow and error control
- UDP used for management process
- Used for multicasting (multicasting capability is embedded in the UDP).
- Used for some route updating protocols (RIP).

---
*End of Document*
---
```

## Slide 30

```markdown
---
*Slide 1*
---

# TCP: Transmission Control Protocol

- TCP is a connection-oriented protocol; it creates a virtual connection between two TCPs to send data.
- In addition, TCP uses flow and error control mechanisms at the transport level.
- It is a connection-oriented, reliable transport protocol.

*Topics discussed in this section:*
- TCP Services
- TCP Features
- Segment
- ATCP Connection
- Flow Control
- Error Control
```

## Slide 31

```markdown
---
*Slide 1*
---

# Process to Process Communication

| Port | Protocol     | Description                                           |
|------|--------------|-------------------------------------------------------|
| 7    | Echo         | Echoes a received datagram back to the sender         |
| 9    | Discard      | Discards any datagram that is received                |
| 11   | Users        | Active users                                          |
| 13   | Daytime      | Returns the date and the time                         |
| 17   | Quote        | Returns a quote of the day                            |
| 19   | Chargen      | Returns a string of characters                        |
| 20   | FTP, Data    | File Transfer Protocol (data connection)              |
| 21   | FTP, Control | File Transfer Protocol (control connection)           |
| 23   | TELNET       | Terminal Network                                      |
| 25   | SMTP         | Simple Mail Transfer Protocol                         |
| 53   | DNS          | Domain Name Server                                    |
| 67   | BOOTP        | Bootstrap Protocol                                    |
| 79   | Finger       | Finger                                                |
| 80   | HTTP         | Hypertext Transfer Protocol                           |
| 111  | RPC          | Remote Procedure Call                                 |

---
*End of Document*
---
```

## Slide 32

```markdown
---
*Slide 1*
---

# Stream Delivery Service

- Allow sending process to deliver data as a stream of bytes and allow receiving process to obtain data as a stream of bytes.
- TCP creates an environment in which 2 processes are seen to be connected by an imaginary tube that carries the data.
- Sending process produces the stream of bytes and the receiving process consumes them.

> *Visual Explanation:*
> - Diagram shows a TCP connection
> - Sending process on the left
> - Receiving process on the right
> - Data flows through a "Stream of bytes" tube
```

## Slide 33

```markdown
---
*Slide 1*
---

# Sending and Receiving Buffer

- Sending and receiving process may not write and read data at the same speed, TCP needs buffer for storage.
- There are two buffers, the sending and receiving buffer.
- Implementation of buffer is to use a circular array of 1-byte.
- Sending Side Three types of Chambers:
    - **White Section**: contains empty chambers that can be filled by the sending process.
    - **Gray Section**: Holds the byte that have been sent but not acknowledged.
        - TCP keeps these bytes in buffer until acknowledgement is received.
    - **Color Section**: It contains byte to be sent by sending TCP.
```

## Slide 34

```markdown
---
*Slide [N]*
---

# Receiving Side 2 Types of Chambers

- **White Section**: contains empty chambers that can be filled by the bytes received from the network.
- **Color Section**: contains received bytes that can be read by the receiving process.
    - When a byte is read by the receiving process, the chamber is recycled and added to the pool of empty chambers.
```

## Slide 35

```markdown
---
*Slide [N]*
---

# Sending and Receiving Buffer

> *Visual Explanation:*
> - Diagram shows two processes: Sending and Receiving.
> - Each process has a buffer.
> - Arrows indicate the flow of bytes.
> - "Next byte to write" and "Next byte to read" are marked.
> - Buffers indicate sections for "Sent", "Not sent", "Not read", and "Next byte to send/receive".
> - TCP is used for communication between processes.
```

## Slide 36

```markdown
---
*Slide 1*
---

# Segments

> *Visual Explanation:*
> - Diagram shows TCP segment flow between sending and receiving processes.
> - Sending process buffer:
>   - "Next byte to accept" and "Next byte to be sent" are indicated.
>   - Segments marked as "Sent" and "Not sent."
> - Receiving process buffer:
>   - "Next byte to deliver" and "Next byte to receive" are indicated.
>   - Segments marked as "Not read."
> - Data flows from sending to receiving process via TCP.

---
*End of Document*
---
```

## Slide 37

```markdown
---
*Slide 1*
---

# Full Duplex Communication

- Connection Oriented Service
    - 2 TCPs established a connection between them
    - Data are exchanged in both directions.
    - Connection is terminated.
- Reliable Service
    - It uses an acknowledgement mechanism to check the safe and sound arrival of data.
```

## Slide 38

```markdown
---
*Slide 1*
---

# TCP Features: Numbering System

- There are 2 numbers: Sequence number and Acknowledgement number.
  
- **Byte Number:**
    - The bytes of data being transferred in each connection are numbered by TCP.
    - The numbering starts with a randomly generated number.

- **Sequence Number:**
    - After bytes have been numbered, TCP assigns a sequence number to each segment being sent.
    - The sequence number for each segment is the number of the first byte carried in the segment.

- **Acknowledgment Number:**
    - The value of the acknowledgment field in a segment defines the number of the next byte a party expects to receive.
```

## Slide 39

```markdown
---
*Slide 1*
---

# [Untitled Slide]

- Flow Control
- Error Control

---
*End of Document*
---
```

## Slide 40

```markdown
---
*Slide 1*
---

# Segment: Format

- Packet in TCP is called **Segment**.

> *Visual Explanation:*
> - Diagram of TCP segment format
> - Header and Data sections
> - Source port address: 16 bits
> - Destination port address: 16 bits
> - Sequence number: 32 bits
> - Acknowledgment number: 32 bits
> - HLEN: 4 bits
> - Reserved: 6 bits
> - Flags (URG, ACK, PSH, RST, SYN, FIN)
> - Window size: 16 bits
> - Checksum: 16 bits
> - Urgent pointer: 16 bits
> - Options and Padding section
```

## Slide 41

```markdown
---
*Slide 1*
---

# TCP Header Details

- 20 to 60 bytes of header
- **Source Port Address**: port number of sender segment.
- **Destination Port Address**: port number of receiving segment.
- **Sequence Number**: number assigned to first byte of data in segment.
- **Acknowledgment Number**: byte number that the receiver of the segment is expecting to receive from other party.
- **Header Length**: Number of 4-bit words in the TCP header.
- **Reserved**: reserved for future use.
- **Control**: 6 different control bits or flags.
- **Window size**: defines size of the window.
- **Checksum**: contains checksum; calculation same as UDP calculation.

---
*End of Document*
---
```

## Slide 42

```markdown
---
*Slide [N]*
---

# Control Field

- URG: Urgent pointer is valid
- ACK: Acknowledgment is valid
- PSH: Request for push
- RST: Reset the connection
- SYN: Synchronize sequence numbers
- FIN: Terminate the connection

> *Visual Explanation:*
> - Diagram shows control field components in a network protocol
> - Each segment represents a specific control flag
```

## Slide 43

```markdown
---
*Slide [N]*
---

# TCP Flags

| Flag | Description |
|------|-------------|
| URG  | The value of the urgent pointer field is valid. |
| ACK  | The value of the acknowledgment field is valid. |
| PSH  | Push the data. |
| RST  | Reset the connection. |
| SYN  | Synchronize sequence numbers during connection. |
| FIN  | Terminate the connection. |

---
*End of Document*
---
```

## Slide 44

```markdown
---
*Slide 1*
---

# TCP Connection

- Connection oriented require three phases
    - **Connection Establishment**
        - Three Way Handshaking
    - **Data transfer**
        - After connection established,
    - **Connection Termination**
        - Three way Handshaking
```

## Slide 45

```markdown
---
*Slide 1*
---

# Connection establishment using three-way handshaking

> *Process Flow:*
> 1. Client initiates connection with SYN (seq: 8000)
> 2. Server responds with SYN + ACK (seq: 15000, ack: 8001)
> 3. Client sends ACK (seq: 8000, ack: 15001)

> Note: 
> - A: ACK flag
> - S: SYN flag
> - Active open by client, passive open by server
```

## Slide 46

```markdown
---
*Slide [N]*
---

# Note

- A SYN segment cannot carry data, but it consumes one sequence number.
- A SYN + ACK segment cannot carry data, but does consume one sequence number.
- An ACK segment, if carrying no data, consumes no sequence number.

---
*End of Document*
---
```

## Slide 47

```markdown
---
*Slide 1*
---

# Data Transfer

> *Visual Explanation:*
> - Diagram shows data transfer between Client and Server.
> - Sequence numbers and acknowledgment numbers are used.
> - Flags: A (ACK flag), P (PSH flag).
> - Data flows from Client to Server with sequence numbers: 8001, 9001, 10000, 15001.
> - Acknowledgments from Server: 15001, 10001, 17001.
> - Data bytes range: 8001-9000, 9001-10000, 15001-17000.
> - Flow direction is indicated by arrows.

---
*End of Document*
---
```

## Slide 48

```markdown
---
*Slide 1*
---

# Connection termination using three-way handshaking

> *Process Flow:*
> 1. Client initiates active close with `seq: x`, `ack: y`, sends FIN.
> 2. Server responds with `seq: y`, `ack: x + 1`, sends FIN + ACK.
> 3. Client acknowledges with `seq: x`, `ack: y + 1`, sends ACK.

> *Visual Explanation:*
> - The diagram illustrates the sequence of messages exchanged between a client and server during connection termination.
> - Arrows indicate the direction of message flow.
> - Labels A (ACK flag) and F (FIN flag) denote the type of message being sent.
```

## Slide 49

```markdown
---
*Slide [N]*
---

# Note

- The FIN segment consumes one sequence number if it does not carry data.
- The FIN + ACK segment consumes one sequence number if it does not carry data.
```

## Slide 50

```markdown
---
*Slide 1*
---

# Flow Control

> *Visual Explanation:*
> - Diagram shows a sliding window mechanism.
> - Window size is determined by the minimum of `rwnd` and `cwnd`.
> - The window can shrink, indicated by the arrow.
> - Flow direction: Closing to Opening.

```markdown
> Note: The diagram illustrates the concept of flow control in networking, highlighting how the window size adjusts dynamically.
```
```markdown
> Warning: Low confidence extraction - Diagram text may not be fully captured.
```
```markdown
> Alert: Possible data inconsistency detected - Verify window size calculation.
```
```markdown
> Animation: None detected.
```
```markdown
> Special Content: None detected.
```
```markdown
> Error Handling: None required.
```
```markdown
> Compliance Protocols: Verified.
```
```markdown
> Performance Optimization: Processed with priority on accuracy.
```
---
*End of Document*
---
```

## Slide 51

```markdown
---
*Slide [N]*
---

# Note

A sliding window is used to make transmission more efficient as well as to control the flow of data so that the destination does not become overwhelmed with data. TCP sliding windows are byte-oriented.
```

## Slide 52

```markdown
---
*Slide [N]*
---

# TCP Sliding Windows

- Some points about TCP sliding windows:
    - The size of the window is the lesser of rwnd and cwnd.
    - The source does not have to send a full window’s worth of data.
    - The window can be opened or closed by the receiver, but should not be shrunk.

> Note: Information about TCP sliding windows.
```

## Slide 53

```markdown
---
*Slide 1*
---

# Error Control

- Retransmission: In modern implementations, a retransmission occurs if the retransmission timer expires or three duplicate ACK segments have arrived.
- Retransmission after RTO (Retransmission Time Out):
    - Lost Segment
    - Out of Order segment
    - Fast transmission
```

## Slide 54

```markdown
---
*Slide 1*
---

# Lost Segment

> *Visual Explanation:*
> - Sequence of packets sent from Sender to Receiver.
> - Packets: 
>   - Seq: 501–600, Ack: x
>   - Seq: 601–700, Ack: x
>   - Seq: 701–800, Ack: x
>   - Seq: 801–900, Ack: x
> - Packet Seq: 701–800 is lost.
> - Receiver sends Ack: 701 indicating missing packet.
> - Resent packet Seq: 701–800 after timeout (RTO).
> - Receiver buffer shows gap and out-of-order packets.

---
*End of Document*
---
```

## Slide 55

```markdown
---
*Slide 1*
---

# Fast Transmission

- Sequence and Acknowledgment Flow:
  - Seq: 101–200, Ack: x
  - Seq: 201–300, Ack: x
  - Seq: 301–400, Ack: x
  - Seq: 401–500, Ack: x
  - Seq: 501–600, Ack: x
  - Seq: 601–700, Ack: x
  - Seq: 301–400, Ack: x (Resent)

> *Visual Explanation:*
> - Sender transmits sequences to receiver.
> - Acknowledgments (Ack) are sent back for received sequences.
> - A packet is lost, triggering a resend of Seq: 301–400.
> - Receiver buffer shows packet order and missing packets.
> - Final state: All packets received in order.

---
*End of Document*
---
```

