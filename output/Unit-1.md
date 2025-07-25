# Unit 1

## Slide 1

```markdown
---
*Slide 1*
---

# Introduction
```

## Slide 2

```markdown
---
*Slide 1*
---

# Data Communication

- When we communicate, we are sharing information. That sharing can be local or remote. Local communication usually occurs face to face, while remote takes place over distance.
- Information is always in terms of **DATA**.
- **Data** refers to information presented in whatever form is agreed upon by parties creating and using the data.
- **Data communication** is the exchange of data between devices via some form of transmission medium such as a wire cable.
- Communication devices must be part of a communication system made up of a combination of hardware and software. Effectiveness of data communication depends upon four fundamental characteristics:
    - **Delivery**: The system must deliver data to the correct destination. Data must be received by the intended device or user.
    - **Accuracy**: The system must deliver data accurately. Data that have been altered in transmission and left uncorrected are unusable.
    - **Timeliness**: The system must deliver data in a timely manner. Data delivered late are unusable, in the same order that they are produced, and without significant delay. This kind of delivery is called **real-time transmission**.
    - **Jitter**: Jitter refers to the variation in the packet arrival time. It is the uneven delay in the delivery of audio and video packets.

---
*End of Document*
---
```

## Slide 3

```markdown
---
*Slide [N]*
---

# Component of Data Communication

- **Message**: The message is the information to be communicated. Popular forms of information include text, numbers, pictures, audio, and video.
- **Sender**: The sender is the device that sends the data message. It can be a computer, workstation, telephone handset, video camera, and so on.
- **Receiver**: The receiver is the device that receives the message. It can be a computer, workstation, telephone handset, video camera, and so on.
- **Transmission Medium**: The transmission is the physical path by which a message travels from sender to receiver. Ex: twisted pair, coaxial cable, fiber-optic cable, and radio waves.
- **Protocol**: A protocol is a set of rules that govern data communications. It represents an agreement between the communicating devices.

> *Visual Explanation:*
> - Diagram shows the flow from Sender to Receiver via a Medium.
> - Protocols are applied at both Sender and Receiver ends.
```

## Slide 4

```markdown
---
*Slide [N]*
---

# Cont...

- Data Representation
    - Text
        - Data are represented in form of bit. E.g. 0, 1.
        - Different bit pattern is known as code.
        - Today's coding system in Unicode 32 bit.
    - Number
        - Numbers are also represented in bit format.
        - Number is directly converted into binary number.
    - Images
        - It is represented in form of matrix of pixel.
    - Audio/Video
        - It is continuous data.
        - Used for recording or broadcasting of sound or music.
- Data Flow
    - Simplex
        - One way traffic only, one device transmits and one device receives.
        - Communication is unidirectional, as on a one-way street. Ex. Keyboard and traditional monitor.
        - E.g. keyboard -> monitor.

---
*End of Document*
---
```

## Slide 5

```markdown
---
*Slide [N]*
---

# Cont...

- Data Transmission Modes:
  - Simplex
  - Half-duplex
  - Full-duplex

> *Visual Explanation:*
> - **Simplex**: Data flows in one direction from Mainframe to Monitor.
> - **Half-duplex**: Data flows in both directions, but not simultaneously. Direction changes over time between Stations.
> - **Full-duplex**: Data flows in both directions simultaneously between Stations.

---
*End of Document*
---
```

## Slide 6

```markdown
---
*Slide [N]*
---

# Cont...

- Half-duplex
    - Each station can both transmit and receive, but not at the same time. When one device is sending, the other can only receive and vice versa.
    - E.g. walkie-talkies
- Full-duplex
    - Both stations can transmit and receive simultaneously.
    - E.g. Telephone
```

## Slide 7

```markdown
---
*Slide 1*
---

# Networks

- **Network**: a set of devices connected by communication link.
- **Node**: Computer, printer or any devices capable of sending or receiving data.
- **Computer Network**: collection of autonomous (work independent) computers that are interconnected with each other or exchanging information with each other.
- **Network Criteria**:
- **Distributed Processing**:
    - In which task is divided among multiple computers.
    - Instead of one single large machine is responsible for all, separate handle a subset.
- **Performance**:
    - Measure is two way transit time and response time.
    - Transit time: Amount of time required for a message to travel from one device to another.
    - Response time: Elapsed time between an inquiry and response.
    - It depends upon number of users, type of transmission medium, capacity of connected h/w, efficiency of s/w.
    - It is evaluated by throughput and delay.
- **Reliability measured by**:
    - Frequency of failure
    - Time it takes a link to recover from failure

---
*End of Document*
---
```

## Slide 8

```markdown
---
*Slide [N]*
---

# Cont...

- **Security**:
    - Protecting data from unauthorized access
    - Protecting data from damage and development
    - Implement procedures for recovery.
- **Types of connection**

> *Visual Explanation:*
> - **Diagram a: Point-to-point**
>   - Direct link between two stations.
> - **Diagram b: Multipoint**
>   - Mainframe connected to multiple stations via a single link.
```

## Slide 9

```markdown
---
*Slide [N]*
---

# Cont...

- Point-to-point
    - Provide dedicated link between two devices.
    - The entire capacity of channel is reserved for transmission between two devices.
    - Ex. TV remote control.
- Multipoint
    - More than two devices share a single link.
    - Capacity of the channel is either
        - Spatially shared connection: devices can use the link simultaneously
        - Timeshare connection: users must take turns.
```

## Slide 10

```markdown
---
*Slide 1*
---

# Topology

- **Topology**
    - The way in which the connections are made (shape of network) is called topology of network.
    - Geometric representation of the relationship of all the links and linking devices.
- **Network topology**
    - Refers to physical layout of the network, the location of the computer and how cable is run between them.
- **Physical topologies**: describe how the cables are run.
- **Logical topologies**: describe how the network messages travel.
- **Physical topology**

> *Visual Explanation:*
> - Diagram showing types of topology:
>   - Mesh
>   - Star
>   - Bus
>   - Ring
```

## Slide 11

```markdown
---
*Slide 1*
---

# Bus Topology

- It is a multipoint connection.
- One large cable acts as **backbone** to link all the devices in the network.
- Nodes are connected to cable by drop lines and taps.
- Drop line is a connection running between the device and the main cable and tap is connector.
- Signals travel through the backbone; some of its energy is transformed into heat, so it becomes weaker as it travels farther. There is a limit on the number of taps.
- It is implemented on limited distance between each node, such as LAN within a department or building.

> *Visual Explanation:*
> - Diagram shows a linear connection with stations connected via drop lines.
> - Terminators are present at both ends of the cable.
> - Flow of data is linear along the backbone.
```

## Slide 12

```markdown
---
*Slide [N]*
---

# Cont...

- **Advantages of bus topology**
    - Easy to install.
    - Connecting a computer to a linear bus is easy.
    - This topology requires the least amount of cabling to connect the computer, so it is less expensive than other cabling arrangements.
    - It is easy to extend a bus since two cables can be jointed into one larger cable with a connector.

- **Disadvantages of bus topology**
    - Entire network shuts down if there is a break in the main cable and it is difficult for reconnection.
    - Adding a new device is difficult because signal reflection at tap can cause degradation in quality, and it can be controlled by limiting the number and spacing of devices connected to a given length of cable.
    - Terminators are required at both ends of the backbone cable.
    - Difficult to identify the problem if the entire network shuts down.
    - Not meant to be used as a standalone solution in a large building.
```

## Slide 13

```markdown
---
*Slide 1*
---

# Ring Topology

- It is point-to-point connection with only the two devices on either side of it.
- Signal passed along the ring in one direction, from device to device until it reaches its destination.
- Each device in ring communicate with repeater (*repeater is an electronic device that receives a signal and retransmits it. Repeaters are used to extend transmissions so that the signal can cover longer distances*).
- The ring topology is a continuous path for data with no logical beginning or ending point and thus no terminators.
- Network may be either unidirectional or bidirectional.

> *Visual Explanation:*
> - Diagram shows a ring topology with stations and repeaters.
> - Data flows in a circular manner.
```

## Slide 14

```markdown
---
*Slide [N]*
---

# Cont...

- **Advantages of ring topology**
    - It is easy to install and configure.
    - Every computer is given equal access to the ring. No single computer can monopolize the network.
- **Disadvantage of ring topology**
    - Failure in any cable or node breaks the loop and can take down the entire network.
    - Maximum ring length and number of nodes are limited.
```

## Slide 15

```markdown
---
*Slide 1*
---

# Star Topology

- It is point-to-point connection only to a central controller, usually called hub (A **hub** is a common connection point for devices in a **network**. Hubs are commonly used to connect segments of a LAN. A hub contains multiple ports. When a packet arrives at one port, it is copied to the other ports so that all segments of the LAN can see all packets).
- It is the oldest communications design method.
- A network uses star topology if all computers are attached to a central point.
- If one device wants to send data to another device, it first has to send that data to a central device, then that central device will send that data to the other connected device.

> *Visual Explanation:*
> - Diagram shows a central hub connecting multiple stations.
> - Data flows from stations to the hub and then to other stations.
```

## Slide 16

```markdown
---
*Slide [N]*
---

# Cont...

- **Advantage of star topology**
    - It is easy to install and wire.
    - The network is not disturbed even if a node fails or is removed from the network.
    - Fault detection and removal of main parts are easier in star topology.
- **Disadvantages of star topology**
    - It requires longer length of cable.
    - If the hub fails, nodes are attached to it are disabled.
    - The cost of hub makes network expensive as compared to bus and ring topology.
```

## Slide 17

```markdown
---
*Slide 1*
---

# Mesh Topology

- It is point-to-point connection.
- The mesh topology has a direct connection between every pair of devices in the network.
- Communication becomes very simple because there is no competition for common line.
- If two devices want to communicate, they do so directly without involving other devices.

> *Visual Explanation:*
> - Diagram shows interconnected stations
> - Each station has a direct link to every other station
> - Ensures direct communication paths
```

## Slide 18

```markdown
---
*Slide [N]*
---

# Cont...

- Advantages of mesh topology
    - The use of large number of links eliminates network congestion.
    - If one link becomes unusable it does not disable the entire system.
- Disadvantages of mesh topology
    - The amount of required cabling is very high.
    - As every node is connected to the other, installation and reconfiguration is very difficult.
    - The amount of hardware required in this type of topology can make it expensive to implement.
```

## Slide 19

```markdown
---
*Slide 1*
---

# Hybrid topology

- Combination of various topologies.
- It has a common bus, sometimes called **backbone**, which allows users to access mainframe or computer and high volume accessed storage.

> *Visual Explanation:*
> - Diagram shows a combination of bus and star topologies.
> - Backbone connects multiple stations.
> - Hub connects to various stations, facilitating communication.
```

## Slide 20

```markdown
---
*Slide 1*
---

# Categories of Network

- Based on metrics
    - LAN (Local Area Network)
    - MAN (Metropolitan Area Network)
    - WAN (Wide Area Network)
- LAN
    - Refer as privately owned or private data networks.
    - It is used to link devices in a single office, building, or campus.
    - Limited to few kilometers.
    - Topology: Bus, Ring, Star

> *Visual Explanation:*
> - Diagram shows multiple-building LAN
> - Topologies include Bus, Ring, Star
> - Backbone connects different LAN segments
```

## Slide 21

```markdown
---
*Slide [N]*
---

# Cont...

- MAN
    - Bigger version of LAN and uses similar technology.
    - Owned and operated by private company.
    - Designed to extend over an entire city.
    - It may be connecting number of LANs into large networks.
    - It is linked using fiber optics connection.

> *Visual Explanation:*
> - Diagram shows a public city network.
> - Multiple LANs are connected to a central network.
> - Connections are depicted using lines, indicating fiber optics.
```

## Slide 22

```markdown
---
*Slide [N]*
---

# Cont...

- WAN
    - Provides long transmission of data, voice, image, and video information over large geographic areas that may comprise a country, a continent, or even the whole world.
    - It is connected across distances of more than 30 miles.

> *Visual Explanation:*
> - Diagram shows a network of computers connected globally, illustrating the concept of WAN.
> - Connections span across continents, emphasizing the extensive reach of WAN technology.
```

## Slide 23

```markdown
---
*Slide 1*
---

# The Internet

- The Internet has revolutionized many aspects of our daily lives.
- It has affected the way we do business as well as the way we spend our free time.
- The internet is a communication system that has brought a wealth of information to our fingertips and organized it for our use.
- **Internet Today**
  - ISP (Internet Service Provider)
  - NISP (National ISP)
  - NAP (Network Access Point)

> *Visual Explanation:*
> - Diagram a: Structure of a national ISP
>   - Regional ISPs connect to a National ISP
> - Diagram b: Interconnection of national ISPs
>   - Multiple National ISPs interconnected via NAP
```

## Slide 24

```markdown
---
*Slide 1*
---

# OSI Model

- ISO - International Standard Organization
- OSI - Open System Interconnection
- ISO is the organization while OSI is the model.
- ISO standard that covers all aspects of network communications is the OSI model.
- An open system is a set of protocols that allows any two different systems to communicate regardless of architecture (hardware/software).
- The purpose of the OSI model is to show how to facilitate communication between different systems without requiring changes to the logic of the underlying hardware and software.
- OSI model is a layered framework for the design of network systems that allows communication between all types of computer systems.
- It consists of 7 separate but related layers.

---
*End of Document*
---
```

## Slide 25

```markdown
---
*Slide [N]*
---

# Cont...

- OSI Model Layers:
  1. Physical
  2. Data Link
  3. Network
  4. Transport
  5. Session
  6. Presentation
  7. Application

> *Visual Explanation:*
> - Diagram showing hierarchical structure of OSI layers
> - Flow from Physical to Application layer
```

## Slide 26

```markdown
---
*Slide [N]*
---

# Cont...

- Layered Architecture
    - Message travels from A to B, it may pass through many intermediate nodes but these intermediate nodes usually involve only the first three layers of the OSI model.
    - Each layer calls upon the services of the layer just below it.
    - The processes on each machine that communicate at a given layer are called peer-to-peer processes.

- Peer-to-peer process
    - At the physical layer communication is direct, device A sends a stream of bits to device B through intermediate nodes.
    - Each layer in the sending device adds its own information to the message it receives from the layer just above it and passes the whole package to the layer just below it.
```

## Slide 27

```markdown
---
*Slide [N]*
---

# OSI Model Communication

- Devices: A and B
- Layers:
  - Application (Layer 7)
  - Presentation (Layer 6)
  - Session (Layer 5)
  - Transport (Layer 4)
  - Network (Layer 3)
  - Data Link (Layer 2)
  - Physical (Layer 1)

> *Visual Explanation:*
> - Communication between Device A and Device B
> - Intermediate nodes facilitate peer-to-peer protocol at each layer
> - Interfaces connect each layer (e.g., 7-6 interface)
> - Physical communication occurs at the bottom layer

---
*End of Document*
---
```

## Slide 28

```markdown
---
*Slide 1*
---

# Physical Layer

- The physical layer is responsible for movement of individual bits from one hop (node) to the next.
- It is concerned with the following (responsibilities):
    - Physical characteristics of interfaces and medium:
        - Define the characteristics of the interface between device and transmission medium.
        - Define type of transmission medium.
    - Representation of bits:
        - Data consist of a stream of bits (sequence 0 or 1)
        - Bit must be encoded into signal (electrical or optical)

> *Visual Explanation:*
> - Diagram shows data flow from data link layer to physical layer and through transmission medium.
> - Bits are represented in binary form (e.g., 110101000000010111).
> - Flow direction is indicated by arrows.
```

## Slide 29

```markdown
---
*Slide [N]*
---

# Cont...

- Data Rate:
    - Number of bits sent each second is called transmission rate
- Synchronization of bit:
    - Sender and receiver clock must be synchronized using the same bit rate.
- Line configuration:
    - Concerned with connection of device
        - Point-to-point: dedicated link
        - Multipoint: link is shared among several devices
- Physical topology:
    - Define how devices are connected in network
        - Bus, ring, mesh, star, hybrid
- Transmission mode:
    - Define the direction of transmission between two devices
        - Simplex, half duplex, and full duplex
```

## Slide 30

```markdown
---
*Slide 1*
---

# Data Link Layer

- It is responsible for moving frames from one hop to next hop.

> *Diagram Explanation:*
> - Data flow: From network layer → Data link layer → To physical layer
> - Frame components: H2, Data, T2
> - Direction: From network layer to physical layer and vice versa

- It is concerned with following responsibilities:
    - Framing:
        - Divides the stream of bits received from the network layer into manageable data units called Frame.
    - Physical addressing:
        - Adds header to frame to define the sender and/or receiver.
```

## Slide 31

```markdown
---
*Slide [N]*
---

# Cont...

- Flow control
    - Imposes a flow control mechanism to avoid overwhelming the receiver (rate at which data are absorbed by receiver is less than the rate of data produced in the sender).
- Error control
    - Adds reliability to the physical layer: by adding mechanism to detect and retransmit damage or lost frames.
    - Uses a mechanism to organize duplicate frames.
    - Achieve through a trailer added to the end of frame.
- Access control
    - Two or more devices are connected to the same link, data link layer protocol are necessary to determine which device has control over the link at time.
```

## Slide 32

```markdown
---
*Slide 1*
---

# Network Layer

- Network layer is responsible for the delivery of individual packets from the source to destination.
- The network layer is responsible for the delivery of packets from the source to destination.
- Data link layer oversees the delivery of the packet between two systems on the same network, the network layer ensures that each packet gets from its point of origin to its final destination.

> *Visual Explanation:*
> - Diagram shows packet flow from transport layer to data link layer.
> - H3 header and data are encapsulated in a packet.
> - Arrows indicate direction of data flow between layers.
```

## Slide 33

```markdown
---
*Slide [N]*
---

# Cont...

- Responsibility
    - Logical addressing
        - Adds a header to the packet coming from the upper layer, includes the logical addresses of the sender and receiver.
    - Routing
        - One of the functions of network layer provides the mechanism to route or switch the packets to their final destinations.
        - In internetwork or large network the connecting device is called router or switch.
```

## Slide 34

```markdown
---
*Slide 1*
---

# Transport Layer

- The transport layer is responsible for the delivery of a message from one process to another.
- Process-to-process delivery of entire message.
- Process is an application program running on a host machine.

- Responsibility
    - Service point addressing
        - Header includes service point address or port address.
        - Gets the entire message to the correct process to the computer.
    - Segmentation and reassembly
        - A message is divided into transmittable segments, with unique sequence numbers.

> *Visual Explanation:*
> - Diagram shows data flow from session layer to transport layer and then to network layer.
> - Segments are labeled with H4 and Data.
> - Arrows indicate the direction of data flow and segmentation process.
```

## Slide 35

```markdown
---
*Slide [N]*
---

# Cont...

- Connection control
    - Layer can be connectionless or connection oriented.
- Flow control
    - End to end rather than across a single link.
- Error control
    - Process to process rather than single link
    - Error correction is achieved through retransmission.
```

## Slide 36

```markdown
---
*Slide 1*
---

# Session Layer

- The session layer is responsible for dialog control and synchronization.
- The session layer is a network dialog controller: it establishes, maintains, and synchronizes the interaction among communicating systems.
- Responsibility
    - Dialog control
        - Allows two systems to enter into a dialog: allows the communication between two processes to take place in either half-duplex or full-duplex.

> *Visual Explanation:*
> - Diagram shows interaction from presentation layer to session layer and from session layer to transport layer.
> - Components labeled as "syn" indicate synchronization points.
> - Flow direction is indicated by arrows.
```

## Slide 37

```markdown
---
*Slide [N]*
---

# Cont...

- Synchronization
    - Allows a process to add checkpoints, or synchronization points to a stream of data.
```

## Slide 38

```markdown
---
*Slide 1*
---

# Presentation Layer

- The presentation layer is responsible for translation, compression, and encryption.
- Concerned with syntax and semantics of the information exchanged between two systems.
- Responsibility
    - Translation
        - Different computers use different encoding systems; the layer is responsible for interoperability between different encoding methods.

> *Visual Explanation:*
> - Diagram shows data flow from application layer to session layer and vice versa.
> - H6 and Data blocks represent the data being processed.
> - Arrows indicate the direction of data flow.
```

## Slide 39

```markdown
---
*Slide [N]*
---

# Cont...

- At sender changes information from its sender dependent format into common format, at receiver changes the common format into its receiver dependent format.
    - Encryption
        - A system must be able to ensure privacy to carry sensitive information.
        - Encryption: sender transforms the original information to another form and passes message over network.
        - Decryption: reverses the original process to transform the message back to its original form
    - Compression:
        - Data compression reduces the number of bits contained in the information.
        - Important in the transmission of multimedia such as text, audio, video.
```

## Slide 40

```markdown
---
*Slide 1*
---

# Application Layer

- The application layer is responsible for providing services to the user.

> *Diagram Explanation:*
> - Two diagrams showing data flow from user to application layer and vice versa.
> - Components: X.500, FTAM, X.400, H7, Data, Message.
> - Flow: User (human or program) → Application layer → Presentation layer and back.

- Responsibility
    - Network Virtual Terminal
        - Network virtual terminal is a software version of a physical terminal, and it allows users to log on to a remote host, for which the application creates a software emulation of a terminal at a remote host.

---
*End of Document*
---
```

## Slide 41

```markdown
---
*Slide [N]*
---

# Cont...

- Mail Services
    - Provides the basis for email forwarding and storage.
- File transfer, access and management
    - Allows a user to access file in remote host, to retrieve files from a remote computer for use in local computer, and to manage a control files in a remote computer locally.
- Directory services
    - Provides distributed database sources and access for global information about various objects and services.
```

## Slide 42

```markdown
---
*Slide 1*
---

# TCP/IP

- TCP/IP protocol suite was developed prior to the OSI model.
- It has 4 layers
    - Host-to-network
    - Internet
    - Transport
    - Application

> *Visual Explanation:*
> - Diagram comparing OSI and TCP/IP models
> - OSI has 7 layers; TCP/IP has 4 layers
> - Presentation and Session layers are not present in TCP/IP
```

## Slide 43

```markdown
---
*Slide [N]*
---

# Cont...

- Host-to-Network Layer
    - Combination of physical and data link layer
    - The network in TCP/IP can be local area network or a wide area network.
- Network Layer
    - It supports the internetworking protocol.
    - IP layer includes ARP, RARP, ICMP network layer physical link to media.
    - ARP: Address Resolution Protocol
        - Used to associate logical address with physical address.
    - RARP: Reverse Address Resolution Protocol
        - It allows a host to discover its internet address when it knows only its physical address.
    - ICMP: Internet Control Message Protocol
        - This mechanism used by hosts and gateway to send notification of datagram problem back to the sender.
- Transport Layer
    - It is represented by two protocols: TCP and UDP.
    - Delivery of message from one process to another process.
```

## Slide 44

```markdown
---
*Slide [N]*
---

# Cont...

- **UDP: User Datagram Protocol**
    - It adds only port address, checksum, error control and length information to data from upper layer.
- **TCP: Transmission Control Protocol**
    - Provide full transport layer service to application.
    - It divides stream of data into smaller unit called **Segment**.
    - Each segment includes a sequence number for recording after receipt, together with an acknowledgement number for segment received.
- **Application Layer**
    - Application layer of TCP/IP includes functionality of session and presentation layer of OSI model.
        - Like encoding, dialog control, compression.
    - Application layer includes file transfer, email, remote login, network management, name management.
```

## Slide 45

```markdown
---
*Slide [N]*
---

# Network Protocols

- OSI Model Layers:
    - Application
    - Transport
    - Internet
    - Network Access

> *Protocol Functions:*
> - **File Transfer:**
>   - TFTP
>   - FTP
>   - NFS
> - **E-mail:**
>   - SMTP
> - **Remote Login:**
>   - Telnet
>   - rlogin
> - **Network Management:**
>   - SNMP
> - **Name Management:**
>   - DNS
> - Note: Used by the router
```

## Slide 46

```markdown
---
*Slide 1*
---

# Network Protocols

- Layered Architecture:
    - Application
    - Transport
    - Internet
    - Network Access

> *Protocol Details:*
> - Transmission Control Protocol (TCP): Connection-Oriented
> - User Datagram Protocol (UDP): Connectionless

> *Visual Explanation:*
> - Diagram shows a layered model with protocols associated with the Transport layer.
> - TCP is connection-oriented, ensuring reliable communication.
> - UDP is connectionless, allowing faster data transmission without error checking.
```

## Slide 47

```markdown
---
*Slide 1*
---

# Network Protocols

- Layer Overview:
    - Application
    - Transport
    - Internet
    - Network Access

> *Protocol Details:*
> - Internet Protocol (IP)
> - Internet Control Message Protocol (ICMP)
> - Address Resolution Protocol (ARP)
> - Reverse Address Resolution Protocol (RARP)

> *Visual Explanation:*
> - Diagram shows hierarchical structure of network layers
> - Protocols associated with the Internet layer
```

## Slide 48

```markdown
---
*Slide 1*
---

# Network Layers and Protocols

- Layers:
  - Application
  - Transport
  - Internet
  - Network Access

> *Protocol Details:*
> - Ethernet
> - Fast Ethernet
> - SLIP and PPP
> - FDDI
> - ATM, Frame Relay, and SMDS
> - ARP
> - Proxy ARP
> - RARP

> *Visual Explanation:*
> - Diagram shows hierarchical network layers
> - Protocols associated with Network Access layer
```

## Slide 49

```markdown
---
*Slide 1*
---

# OSI vs TCP/IP

- Similarity:
    - Both have layers.
    - Both have application layer though they include very different services.
    - Both have comparable transport and network layers.
    - Both assume packets are switched. This means that individual packets may take different paths to reach the same destination.
- Difference:
    - TCP/IP combines the presentation and session layer issues into its application layer.
    - TCP/IP combines the OSI data link and physical layers into the network access layer.
    - TCP/IP appears simple because it has fewer layers.
    - TCP/IP protocols are the standards around which the internet developed, so the TCP/IP model gains credibility just because of its protocol.
```

## Slide 50

```markdown
---
*Slide 1*
---

# Protocols

- Protocol: Rules and Regulations
    - A set of rules that governs the Data Communication.
    - For communication to occur, entities must agree upon the protocol.
- Key elements of protocol:
    - Syntax: structure or format of data
    - Semantics: meaning of each section in the structure.
    - Timing: when and how fast data should be sent.
```

## Slide 51

```markdown
---
*Slide 1*
---

# Standards

- Standards is essential in
    - Creating/maintaining open and competitive markets
    - Guaranteeing national/international interoperability
- Two categories:
    - De Jure ("by law" or "by Regulation") standards
    - De Facto ("by fact" or "by convention") standards
        - Proprietary standards: Closed standards
        - Nonproprietary standards: Open standards
- Standard committees
    - ISO (international organization for standardization)
        - Voluntary international organization
    - ANSI (American National Standard Institute)
        - Private non-profit corporation in US.
    - IEEE (Institute of Electrical and Electronics Engineers)
        - The largest engineering society in the world.
    - EIA (Electrical Industries Alliance)
        - Non-Profit organization in US
```

## Slide 52

```markdown
---
*Slide 1*
---

# Standards

- ITU (International Telecommunication Union)
    - Formerly, CCITT formed by UN
- IETF (Internet Engineering Task Force)

---
*End of Document*
---
```

