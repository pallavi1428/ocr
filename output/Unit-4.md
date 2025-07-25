# Unit 4

## Slide 1

```markdown
---
*Slide 1*
---

# UNIT 4

## Network Layer

---
*End of Document*
---
```

## Slide 2

```markdown
---
*Slide 2*
---

# Unit Covered

1. **Internetworking**
    - Need of Network Layer
    - Internet as datagram n/w
    - Internet as Connectionless n/w

2. **Delivery**
    - Direct
    - Indirect

3. **Forwarding**
    - Forwarding Techniques
    - Forwarding Process
    - Routing table

4. **Routing protocols**
    - Distance vector routing
    - Link state routing
    - Path vector routing
```

## Slide 3

```markdown
---
*Slide 1*
---

# Internetworking

---
*End of Document*
---
```

## Slide 4

```markdown
---
*Slide 4*
---

# Internetworking

*In this section, we discuss internetworking, connecting networks together to make an internetwork or an internet.*

- Topics discussed in this section:
    - Need for Network Layer
    - Internet as a datagram Network
    - Internet as a Connectionless Network
```

## Slide 5

```markdown
---
*Slide 5*
---

# Internetworking

- Physical and Datalink layer of a network operate locally.
- These two layers are jointly responsible for data delivery on the network from one node to next.

> *Visual Explanation:*
> - Diagram shows the flow from node A to node D.
> - Each node consists of Data link and Physical layers.
> - Data is delivered hop-to-hop through nodes S1 and S3.
```

## Slide 6

```markdown
---
*Slide 6*
---

# Internetwork

- Internetwork made up of 5 networks:
    - 4 LAN and 1 WAN
- If one host A needs to send data packet to D:
    - Packet goes 1st from A to R1 (Switch or Router)
    - R1 to R3
    - R3 to Host D.
- Data packet passes through 3 links, in each 2 physical and 2 Datalink layers are involved.
```

## Slide 7

```markdown
---
*Slide 7*
---

# Internetworking

> *Network Diagram:*
> - Components:
>   - Multiple LANs connected via WAN
>   - Routers (S1, S2, S3) facilitating connections
> - Flow:
>   - Data flows from computer A through Link 1 to LAN
>   - Router S1 connects to WAN via f1, f2, f3
>   - WAN connects to other LANs through S2 and S3
>   - Link 2 and Link 3 connect to computer D
```

## Slide 8

```markdown
---
*Slide 8*
---

# Problem with Delivery through Several Links

- When data arrive at interface f1 of R1, how does R1 know that interface f3 is the outgoing interface?
- There is no provision in the data link (or physical) layer to help R1 to make the right decision.
- The frame does not carry any routing information.
- Frame contains MAC address of A as a source and R1 as Destination.
- For a LAN or MAN, delivery means carrying the frame through one link not beyond.
```

## Slide 9

```markdown
---
*Slide 9*
---

# Need of Network Layer

*To solve the problem of delivery through several link, the Network layer (internetwork layer) was designed.*

The network layer is responsible for

- Host-to-host delivery
- Routing packets through the router or switches.
```

## Slide 10

```markdown
---
*Slide 10*
---

# Network layer in an Internetwork

> *Visual Explanation:*
> - Diagram shows network layers: Network, Data link, Physical
> - Flow from A to D through S1, S3
> - Host-to-host path via WAN and LANs
> - Components: Computers, LANs, WAN, switches (S1, S2, S3)
> - Data flow: A → S1 → S3 → D
> - Path: f1, f2, f3 connections

---
*End of Document*
---
```

## Slide 11

```markdown
---
*Slide 11*
---

# Network Layer Functionality

- General Functionality of network layer at a
    - Source
    - Router
    - Destination

---
*End of Document*
---
```

## Slide 12

```markdown
---
*Slide 12*
---

# Network Layer at Source

1. Creating packet from data coming from another protocol
    - Such as transport layer protocol or routing protocol.
2. Header of packet contains information:
    - Logical address of source and destination.
3. Checking its routing table to find out routing information
    - Such as outgoing interface of packet
    - Physical address of next node.
4. If packet is too large, the packet is fragmented.
```

## Slide 13

```markdown
---
*Slide 13*
---

# Network Layer at Source

> *Process Flow:*
> 1. Data from another protocol → Processing
> 2. Processing → Routing table
> 3. Routing table → IP packet and routing information
> 4. IP packet and routing information → Network layer
> 5. Network layer → To data link layer

> *Visual Explanation:*
> - The diagram illustrates the flow of data from the source through the network layer.
> - Data is processed and routed using a routing table.
> - The final output is directed to the data link layer.

*Note: a. Network layer at source*
```

## Slide 14

```markdown
---
*Slide 14*
---

# Network Layer At Switch or Router

1. Responsibility for routing a packet.
2. When packet is arrive, router and switch consults it routing table
    - Find interface from which the packet must be sent.
3. After some changes in header, with routing information
    - The packet is passed to the data link layer.
```

## Slide 15

```markdown
---
*Slide 15*
---

# Network Layer At Destination

1. Responsible for address verification
    - Make sure that the destination address on the packet is same as address of the Host
2. If packet is fragmented
    - The network layer waits until all fragments have arrived.
    - Then reassembles them
    - Deliver reassembled packet to transport layer.
```

## Slide 16

```markdown
---
*Slide 16*
---

# Network Layer At Destination

> *Visual Explanation:*
> - Diagram shows the flow of data at the network layer at the destination.
> - Components:
>   - IP packet received from data link layer.
>   - Processing occurs at the network layer.
>   - Data is then sent to another protocol.
> - Flow direction:
>   - From data link layer to processing.
>   - Processing to another protocol.
```

## Slide 17

```markdown
---
*Slide 17*
---

# Internet as a Datagram Network

- The internet has chosen the datagram approach to switching in the network layer.
- It uses universal addresses defined in the network to route packets from the source to destination.

> *Visual Explanation:*
> Switching at the network layer in the Internet uses the datagram approach to packet switching
```

## Slide 18

```markdown
---
*Slide 1*
---

# Datagram Approach

- In a packet-switched network, there is no resource reservation; resources are allocated on demand.

> *Visual Explanation:*
> - Diagram of a datagram network
> - Packets labeled 1 to 4 are sent from computer A to computer X
> - Packets take different paths through the network
> - No fixed path; packets are routed independently

---
*End of Document*
---
```

## Slide 19

```markdown
---
*Slide 19*
---

# Internet as a Datagram Network

- The internet, at network layer, is a packet-switched network.
- Switching can be divided into 3 categories:
    - Circuit Switching
    - Packet Switching
        - Virtual circuit
        - Datagram
    - Message Switching
```

## Slide 20

```markdown
---
*Slide 20*
---

# Internet as a Connectionless Network

- Delivery can be done by either connection oriented or connectionless network service.
- **Connection – Oriented Service:**
    - Source must make connection with destination before sending packet.
    - And then sequence of packet from same source to destination one after another.
    - Packet is logically connected with each other.
    - When all packets of message have been delivered, the connection is terminated.
    - Decision about route made only once, when connection is established.
    - Switch do not recalculate route.
```

## Slide 21

```markdown
---
*Slide 21*
---

# Connectionless service

- In this, Network layer treats each packet independently, with each packet having no relationship to any other packet.
- Packet may not travel the same path to their destination.
- This type of service is used in datagram approach.
- Reason:
    - Internet is made up of so many heterogeneous networks.
    - Impossible to create connection from source to destination.

> *Visual Explanation:*
> Communication at the network layer in the Internet is connectionless.
```

## Slide 22

```markdown
---
*Slide 22*
---

# Delivery

- The network layer supervises the handling of the packet by the underlying physical network.
- We define this handling as the delivery of a packet.
    - Direct Delivery
    - Indirect Delivery
```

## Slide 23

```markdown
---
*Slide 23*
---

# Direct Delivery

- In direct delivery, the final destination of a packet is a host connected to the same physical network as the deliverer.

- **Direct delivery occurs when**
    - The source and destination of packet are located on the same physical network or
    - Delivery is between the last router and destination host.

- **The sender can easily determine if the delivery is direct.**
    - Compare N/W address of destination and address of N/W to which it is connected.
    - If Match is found, the delivery is Direct.
```

## Slide 24

```markdown
---
*Slide 24*
---

# Direct Delivery

> *Visual Explanation:*
> - Diagram shows a network with two hosts.
> - Direct delivery occurs between hosts through the network.
> - Connection extends to the rest of the Internet.
> - Flow direction is indicated by arrows.

*Note: a. Direct delivery*
```

## Slide 25

```markdown
---
*Slide 25*
---

# Indirect Delivery

- If the destination host is not on the same network as the deliverer, the packet is delivered indirectly.
- In indirect Delivery:
    - The packet goes from router to router until it reaches the one connected to the same physical network as its final destination.

> *Note:*
> Delivery always involves one direct delivery but zero or more indirect deliveries. Last delivery is always as Direct delivery.
```

## Slide 26

```markdown
---
*Slide 26*
---

# Indirect Delivery

> *Visual Explanation:*
> - Diagram shows network communication
> - Host (source) sends data via network
> - Indirect delivery through a router
> - Direct delivery to Host (destination)
> - Flow: Source → Network → Router → Network → Destination

*Note: b. Indirect and direct delivery*
```

## Slide 27

```markdown
---
*Slide 27*
---

# Forwarding

- Forwarding means to place the packet in its route to its destination.
- Forwarding requires a host or a router to have a routing table.
- When a host has a packet to send or when a router has received a packet to be forwarded, it looks at this table to find the route to the final destination.
- **Forwarding Include**:
    - Forwarding Techniques
    - Forwarding Process
    - Routing Table
```

## Slide 28

```markdown
---
*Slide 28*
---

# Forwarding Technique

- Several techniques can make the size of the routing table manageable and also handle issues such as security.
    - **Next-hop method** versus **Route Method**
    - **Network-specific method** versus **Host-Specific Method**
```

## Slide 29

```markdown
---
*Slide 29*
---

# Next-hop method versus Route Method

- One technique to reduce the content of a routing table is called the **Next-hop-method**.
- The routing table holds only the address of the next hop instead of information about the complete route (**route method**).
- The entry of routing table must be consistent with one another.
```

## Slide 30

```markdown
---
*Slide 30*
---

# Route method versus next-hop method

- Routing tables based on route:
  - Routing table for host A:
    - Destination: Host B
    - Route: R1, R2, host B
  - Routing table for R1:
    - Destination: Host B
    - Route: R2, host B
  - Routing table for R2:
    - Destination: Host B
    - Route: Host B

- Routing tables based on next hop:
  - Routing table for host A:
    - Destination: Host B
    - Next hop: R1
  - Routing table for R1:
    - Destination: Host B
    - Next hop: R2
  - Routing table for R2:
    - Destination: Host B
    - Next hop: ---

> *Visual Explanation:*
> - Host A connects to Host B through networks R1 and R2.
> - The diagram illustrates the flow from Host A to Host B via network routers.

---
*End of Document*
---
```

## Slide 31

```markdown
---
*Slide 31*
---

# Network-specific Method versus Host-specific Method

- A second technique to reduce the routing table and simplify the searching process is called the Network-specific method.
- Here, instead of having an entry for every destination host connected to the same physical network (host-specific)
    - **We have only one entry that defines the address of the destination network itself.**
- We treat all hosts connected to the same network as one single entry.
- Example:
    - If 1000 hosts are attached to the same network, only one entry exists in the routing table.
```

## Slide 32

```markdown
---
*Slide 32*
---

# Host-specific versus network-specific method

- Routing table for host S based on host-specific method:
  - Destination: A, B, C, D
  - Next hop: R1

- Routing table for host S based on network-specific method:
  - Destination: N2
  - Next hop: R1

> *Visual Explanation:*
> - Diagram shows two routing methods.
> - Host-specific method directs all destinations (A, B, C, D) to R1.
> - Network-specific method directs traffic to N2 via R1.
> - Flow: S → N1 → R1 → N2 → A/B/C/D
```

## Slide 33

```markdown
---
*Slide 33*
---

# Default Method

- Another technique to simplify routing is called **default method**.
- Host A is connected to a network with two routers.
- Router R1 routes the packet to hosts connected to network N2.
- However, for the rest of the network, R2 is used.

> Note: Instead of listing all networks in the entire Internet, Host A can just have one entry called Default (0.0.0.0 = network address)
```

## Slide 34

```markdown
---
*Slide 34*
---

# Default Method

- Routing Table for Host A:
  - Destination: N2
    - Next hop: R1
  - Destination: Any other
    - Next hop: R2

> *Visual Explanation:*
> - Host A connects to network N1.
> - Default router R2 connects to the rest of the Internet.
> - Router R1 connects to network N2.
> - Data flow:
>   1. Host A → N1
>   2. N1 → R1 or R2 based on destination
>   3. R2 → Rest of the Internet
```

## Slide 35

```markdown
---
*Slide 35*
---

# Forwarding Process

- Host and routers use classless addressing
    - Because classful addressing is a special case of classless addressing.
- In classless addressing, the routing table needs to have one row of information for each block involved.
- The table needs to be searched based on the network address.
- Destination address in the packet gives no clue about the network address.
- To solve the problem, we need to include the mask(/n) in the table.
    - Extra column that includes the mask for the corresponding block.
```

## Slide 36

```markdown
---
*Slide 36*
---

# Simplified forwarding module in classless address

- In classless addressing, we need at least four columns in a routing table.

> *Visual Explanation:*
> - Diagram of a forwarding module
> - Process Flow:
>   1. Packet → Extract destination address
>   2. Extract destination address → Search table
>   3. Search table → Next-hop address and interface number
>   4. Next-hop address and interface number → To ARP
> - Table Columns:
>   - Mask (/n)
>   - Network address
>   - Next-hop address
>   - Interface
```

## Slide 37

```markdown
---
*Slide 37*
---

# Example 22.1

- Make a routing table for router R1, using the configuration in Figure 22.6.

---
*End of Document*
---
```

## Slide 38

```markdown
---
*Slide 38*
---

# Configuration of Example 22.1

> *Network Diagram:*
> - Central router R1 with interfaces m0, m1, m2
> - Connections:
>   - m0: 180.70.65.128/25, 180.70.65.135/25
>   - m1: 201.4.16.0/22, 201.4.16.2/22
>   - m2: 201.4.22.0/24, 201.4.22.3/24
> - Additional routes:
>   - 180.70.65.192/26, 180.70.65.194/26
>   - Connection to the rest of the Internet via 180.70.65.200/26
```

## Slide 39

```markdown
---
*Slide 39*
---

# Solution

- Table 22.1 shows the corresponding table.

## Routing table for Router R1.

| Mask | Network Address | Next Hop       | Interface |
|------|-----------------|----------------|-----------|
| /26  | 180.70.65.192   | —              | m2        |
| /25  | 180.70.65.128   | —              | m0        |
| /24  | 201.4.22.0      | —              | m3        |
| /22  | 201.4.16.0      | ....           | m1        |
| Any  | Any             | 180.70.65.200  | m2        |

---
*End of Document*
---
```

## Slide 40

```markdown
---
*Slide 40*
---

# Example 22.2

_Show the forwarding process if a packet arrives at R1 in Figure 22.6 with the destination address 180.70.65.140._

**Solution**

- The router performs the following steps:
    1. The first mask (/26) is applied to the destination address. The result is 180.70.65.192, which does not match the corresponding network address.
    2. The second mask (/25) is applied to the destination address. The result is 180.70.65.128, which matches the corresponding network address. **The next-hop address** and the interface number m0 are passed to ARP for further processing.
```

## Slide 41

```markdown
---
*Slide 41*
---

# Routing Table

- Host and router have routing tables with entries for each destination, or combination of destinations, to route IP packets.
- The routing table can be either
    - Static
    - Dynamic
```

## Slide 42

```markdown
---
*Slide 42*
---

# Static

- Static routing table contains information entered manually.
- The administrator enters the route for each destination into routing table.
- When table is created, it cannot update automatically when there is change in Internet.
- The table must be manually altered.
- It can be used in small internet that does not change.
- It is poor strategy to use a static routing table in a big internet as the Internet.
```

## Slide 43

```markdown
---
*Slide 43*
---

# Dynamic Routing Table

- It is updated periodically by using one of the dynamic routing protocols.
- Whenever there is a change in the Internet, it updates all the tables in the router or host automatically.
- Routers in the Internet need to be updated dynamically for efficient delivery of IP packets.
```

## Slide 44

```markdown
---
*Slide 44*
---

# Format of Routing Table

| Mask      | Network address | Next-hop address | Interface | Flags | Reference count | Use |
|-----------|-----------------|------------------|-----------|-------|-----------------|-----|
| ..........| .................| ..................| ...........| .......| ..................| .......|

- **Mask**: Mask apply for entry.
- **Network Address**: Network address to which the packet is finally delivered.
- **Next-Hop-Address**: Address of next hop router to which the packet is delivered.
- **Interface**: Name of the interface.
```

## Slide 45

```markdown
---
*Slide 45*
---

# Intra and Interdomain Routing

- **Autonomous System**:
    - Group of network and router under the authority of single administrator.
- **Intradomain Routing**:
    - Routing inside autonomous system.
- **Interdomain Routing**:
    - Routing between autonomous system.

> *Visual Explanation:*
> - Diagram shows multiple autonomous systems.
> - R1, R2, R3, R4 represent routers connecting different systems.
> - Solid lines indicate intradomain connections.
> - Dashed lines indicate interdomain connections.
```

## Slide 46

```markdown
---
*Slide [N]*
---

# Cont...

A routing protocol is a combination of rules and procedures that lets routers in the Internet inform each other for changes.

> *Visual Explanation:*
> - **Routing protocols**
>   - **Intradomain**
>     - Distance vector (e.g., RIP)
>     - Link state (e.g., OSPF)
>   - **Interdomain**
>     - Path vector (e.g., BGP)

---
*End of Document*
---
```

## Slide 47

```markdown
---
*Slide 47*
---

# Optimization

- When router receives a packet, to which network should it pass the packet?
- The decision is based on optimization:
    - Which of the available pathways is the optimal pathway?
    - Optimality depends on various factors:
        - Cost metrics (RIP)
        - Shortest path (OSPF)
        - Policy (BGP)
```

## Slide 48

```markdown
---
*Slide 48*
---

# Optimization Protocol

- **RIP: Routing information protocol**
    - Treat all networks as equal and the cost of passing through the network is the same.
    - It is an intradomain routing protocol used inside an autonomous system.
    - RIP uses **Hop Count metrics**.
        - The number of links to reach each destination is called hop count.
```

## Slide 49

```markdown
---
*Slide 49*
---

# Optimization Protocol

- **OSPF: Open Shortest Path First**
    - Assign cost based on types of service required.
    - Example: Link state protocol.

- **BGP: Border Gateway Protocol**
    - It is based on policy set by administrator.
    - Policy defines what paths should be chosen.
    - Example: Path vector protocol.
```

## Slide 50

```markdown
---
*Slide 50*
---

# Distance Vector Routing

- The least cost route between any two nodes is the route with minimum distance.
- In this protocol, as the name implies, each node maintains a vector (table) of minimum distance to every node.
- The table at each node also guides the packet to the desired node by showing the next stop in the route.
```

## Slide 51

```markdown
---
*Slide 51*
---

# Distance Vector Routing Table

> *Visual Explanation:*
> - Diagram shows a network with nodes A, B, C, D, and E.
> - Each node has a routing table indicating the cost to reach other nodes and the next hop.
> - Connections between nodes have specific costs:
>   - A to B: 5
>   - A to C: 2
>   - B to C: 4
>   - B to E: 3
>   - C to D: 3
>   - C to E: 4
> - Routing tables:
>   - **A's table**:
>     | To | Cost | Next |
>     |----|------|------|
>     | A  | 0    | —    |
>     | B  | 5    | —    |
>     | C  | 2    | —    |
>     | D  | 3    | —    |
>     | E  | 6    | C    |
>   - **B's table**:
>     | To | Cost | Next |
>     |----|------|------|
>     | A  | 5    | —    |
>     | B  | 0    | —    |
>     | C  | 4    | —    |
>     | D  | 8    | A    |
>     | E  | 3    | —    |
>   - **C's table**:
>     | To | Cost | Next |
>     |----|------|------|
>     | A  | 2    | —    |
>     | B  | 4    | —    |
>     | C  | 0    | —    |
>     | D  | 5    | A    |
>     | E  | 4    | —    |
>   - **D's table**:
>     | To | Cost | Next |
>     |----|------|------|
>     | A  | 3    | —    |
>     | B  | 8    | A    |
>     | C  | 5    | A    |
>     | D  | 0    | —    |
>     | E  | 9    | A    |
>   - **E's table**:
>     | To | Cost | Next |
>     |----|------|------|
>     | A  | 6    | C    |
>     | B  | 3    | —    |
>     | C  | 4    | —    |
>     | D  | 9    | C    |
>     | E  | 0    | —    |
```

## Slide 52

```markdown
---
*Slide 52*
---

# Dynamic Routing Table

- The tables (Vectors) are stable.
- Each node knows how to reach any other node and the cost.
- 3 steps for dynamic routing table:
    - **Initialization**
        - Each node can know only the distance between itself and its immediate neighbor.
        - The distance for any entry that is not a neighbor is marked as infinite.
    - **Sharing**
        - Sharing of information between neighbors.
    - **Updating**
        - When a node receives a two-column routing table from a neighbor, it needs its routing table.
```

## Slide 53

```markdown
---
*Slide 53*
---

# Initialization of tables in distance vector routing

> *Visual Explanation:*
> - Diagram of network nodes A, B, C, D, E
> - Connections with costs: A-B (5), A-C (2), A-D (3), B-C (4), B-E (3), C-E (4)
> - Each node has a table showing initial costs to other nodes:
>   - **A's table**:
>     | To | Cost | Next |
>     |----|------|------|
>     | A  | 0    | —    |
>     | B  | 5    | —    |
>     | C  | 2    | —    |
>     | D  | 3    | —    |
>     | E  | ∞    | —    |
>   - **B's table**:
>     | To | Cost | Next |
>     |----|------|------|
>     | A  | 5    | —    |
>     | B  | 0    | —    |
>     | C  | 4    | —    |
>     | D  | ∞    | —    |
>     | E  | 3    | —    |
>   - **C's table**:
>     | To | Cost | Next |
>     |----|------|------|
>     | A  | 2    | —    |
>     | B  | 4    | —    |
>     | C  | 0    | —    |
>     | D  | ∞    | —    |
>     | E  | 4    | —    |
>   - **D's table**:
>     | To | Cost | Next |
>     |----|------|------|
>     | A  | 3    | —    |
>     | B  | ∞    | —    |
>     | C  | ∞    | —    |
>     | D  | 0    | —    |
>     | E  | ∞    | —    |
>   - **E's table**:
>     | To | Cost | Next |
>     |----|------|------|
>     | A  | ∞    | —    |
>     | B  | 3    | B    |
>     | C  | 4    | C    |
>     | D  | ∞    | —    |
>     | E  | 0    | D    |
```

## Slide 54

```markdown
---
*Slide 54*
---

# Distance Vector Routing

> Note: In distance vector routing, each node shares its routing table with its immediate neighbors periodically and when there is a change.
```

## Slide 55

```markdown
---
*Slide 55*
---

# Updating in Distance Vector Routing

> *Process Flow:*
> 1. Received from C:
>    - | To | Cost |
>    - |----|------|
>    - | A  | 2    |
>    - | B  | 4    |
>    - | C  | 0    |
>    - | D  | ∞    |
>    - | E  | 4    |
> 2. A's modified table:
>    - | To | Cost | Next |
>    - |----|------|------|
>    - | A  | 4    | C    |
>    - | B  | 6    | C    |
>    - | C  | 2    | C    |
>    - | D  | ∞    | C    |
>    - | E  | 6    | C    |
> 3. Compare with A's old table:
>    - | To | Cost | Next |
>    - |----|------|------|
>    - | A  | 0    | —    |
>    - | B  | 5    | —    |
>    - | C  | 2    | —    |
>    - | D  | 3    | —    |
>    - | E  | ∞    | —    |
> 4. A's new table:
>    - | To | Cost | Next |
>    - |----|------|------|
>    - | A  | 0    | —    |
>    - | B  | 5    | —    |
>    - | C  | 2    | —    |
>    - | D  | 3    | —    |
>    - | E  | 6    | C    |
```

## Slide 56

```markdown
---
*Slide 56*
---

# When to share

- When node share its routing table to other?
    - Periodic Update
        - Sends its routing table, normally every 30 seconds.
    - Triggered Update
        - Node sends its two column routing table to its neighbor when there is change in routing table.
```

## Slide 57

```markdown
---
*Slide 57*
---

# Link State Routing

- It has different philosophy than distance vector routing.
- In link state routing
    - If each node in the domains has entire topology of domain (list of node and links), how they are connected including the type, cost and condition (UP or Down).
    - Node can use Dijkstra’s algorithm to build routing table.

*Note: A group of computers and devices on a network that are administered as a unit with common rules and procedures. Within the Internet, all devices sharing a common part of the IP address are said to be in the same domain.*
```

## Slide 58

```markdown
---
*Slide 58*
---

# Concept of Link State Routing

> *Visual Explanation:*
> - Central diagram shows a network with nodes A, B, C, D, E.
> - Connections between nodes have weights: A-B (5), A-C (2), A-D (3), B-C (4), B-E (3), C-E (4).
> - Smaller diagrams illustrate individual node perspectives with routing tables.
> - Flow direction indicated by arrows from network diagrams to routing tables.

---
*End of Document*
---
```

## Slide 59

```markdown
---
*Slide 59*
---

# Routing Table and Topology

- Each node uses the same topology to create a routing table.
- But routing table for each node is unique.
    - Because the calculation is based on different interpretation of topology.
- It is similar to a city map in which each person may have the same map.
    - Each needs to take a different route to reach their specific destination.
- Topology must be dynamic.
    - Representing the latest state of each node and each link.
    - If there are changes in any point in the network, topology must be updated for each node.
```

## Slide 60

```markdown
---
*Slide 60*
---

# Link state knowledge

- Whole topology can be compiled from the partial knowledge of each node.
  Figure indicating part of knowledge belonging to each node.

> *Visual Explanation:*
> - Diagram shows nodes A, B, C, D, and E with their respective states of links.
> - Node A is connected to nodes B, C, and D.
> - Node B is connected to nodes A, C, and E.
> - Node C is connected to nodes A, B, and E.
> - Node D is connected to node A.
> - Node E is connected to nodes B and C.
> - Link weights are indicated on the connections between nodes.
```

## Slide 61

```markdown
---
*Slide 61*
---

# Building Routing Table

1. Creation of state of links by each node – **link state packet (LSP)**
2. Dissemination of LSPs to every other router, called flooding.
3. Formulation of a shortest path tree for each node.
4. Calculation of routing table based on the shortest path tree.
```

## Slide 62

```markdown
---
*Slide 62*
---

# Step 1

- **Creation of Link State Packet (LSP)**
    - It carries a minimum amount of data like:
        - Node Identity and List of links: To make the topology.
        - Sequence Number: Facilitates flooding and distinguishes new LSP from old ones.
        - Age: Prevents old LSP from remaining in the domain for a long time.
    - **LSP Generated on 2 occasions**
        - When there is a change in the topology of the domain.
        - On the Periodic Update (60 min or 2 h).
```

## Slide 63

```markdown
---
*Slide 63*
---

# Step 2

- **Flooding of LSPs**
    - After a node has prepared an LSP, it must be disseminated to all other nodes. This process is called flooding.
    - Flooding based on the following:
        - Creating node sends a copy of LSP out of each interface.
        - Receiving node compares LSP with the copy they already have.
            - If old one, then discard LSP.
            - If newer, discard old LSP and keep new one.
                - Sends copy to each interface except the one from which the packet has arrived.
```

## Slide 64

```markdown
---
*Slide 64*
---

# Step 3

- **Formulation of Shortest Path**
    - Tree is a graph of nodes and links: one node is called Root.
    - Dijkstra algorithm creates shortest path.
    - It divides node into 2 parts.
        - Permanent
        - Tentative
    - It finds the neighbor of current node, makes them tentative, examines them and if they pass the criteria, makes them permanent.
```

## Slide 65

```markdown
---
*Slide 1*
---

# Example of Formulation of Shortest Path Tree

- Topology Diagram:
  - Nodes: A, B, C, D, E
  - Edges with weights: 
    - A to B: 5
    - A to C: 3
    - C to B: 2
    - C to E: 4
    - D to C: 3
    - D to E: 4

> *Process Flow:*
> 1. Set root to A and move A to tentative list.
> 2. Move A to permanent list and add B, C, and D to tentative list.
> 3. Move C to permanent and add E to tentative list.
> 4. Move D to permanent list.
> 5. Move B to permanent list.
> 6. Move E to permanent list (tentative list is empty).

---
*End of Document*
---
```

## Slide 66

```markdown
---
*Slide 66*
---

# Tracing

| Permanent List                        | Tentative List               |
|---------------------------------------|------------------------------|
| Permanent list: empty                 | Tentative List A(0)          |
| Permanent list: A(0)                  | Tentative List B(5), C(2), D(3) |
| Permanent list: A(0), C(2)            | Tentative List B(5), D(3), E(6) |
| Permanent list: A(0), C(2), D(3)      | Tentative List B(5), E(6)    |
| Permanent list: A(0), B(5), C(2), D(3)| Tentative List E(6)          |
| Permanent list: A(0), B(5), C(2), D(3), E(6) | Tentative List Empty     |

---
*End of Document*
---
```

## Slide 67

```markdown
---
*Slide 67*
---

# Routing Table for node A

| Node | Cost | Next Router |
|------|------|-------------|
| A    | 0    | —           |
| B    | 5    | —           |
| C    | 2    | —           |
| D    | 3    | —           |
| E    | 6    | C           |

---
*End of Document*
---
```

## Slide 68

```markdown
---
*Slide 68*
---

# OSPF

- Intradomain routing protocol.
- Its Domain is also autonomous.
- To handle routing efficiently and timely manner.
    - OSPF divides the system into areas.
- Area is a collection of network, host, and router all contained within an autonomous system.
- Router inside an area floods the area with routing information.
- At the border of an area, a special router called **area border router**.
    - It summarizes the information about the area and sends it to another area.
```

## Slide 69

```markdown
---
*Slide 69*
---

# Areas in an autonomous system

> *Visual Explanation:*
> - **Diagram Overview**:
>   - **Area 1**: Contains multiple networks connected through an area border router.
>   - **Area 2**: Similar structure with networks linked to an area border router.
>   - **Area 0 (Backbone)**: Central backbone router connecting to other areas.
>   - **AS Boundary Router**: Connects the autonomous system to other ASs.
> - **Flow**:
>   - Networks (net) are interconnected within areas.
>   - Backbone router facilitates communication between areas.
>   - AS boundary router links to external autonomous systems.
```

## Slide 70

```markdown
---
*Slide 70*
---

# Path Vector Routing

- Distance vector and link state routing are both Intradomain routing protocols.
    - They can be used inside an autonomous system, but not between autonomous systems.
- **Path vector routing** is useful for Interdomain routing.

> *Principle: We assume that there is one node in each autonomous system that acts on behalf of the entire autonomous system. That node is called a Speaker Node.*
```

## Slide 71

```markdown
---
*Slide 71*
---

# Speaker Node in AS

- Speaker node in an AS creates the routing table and advertises it to speaker node in neighboring ASs.
- Idea is same as distance vector
    - But only speaker node in each AS can communicate with each other.
    - Speaker node advertises the path, not the metric of each node.
- Three steps to follow
    - Initialization
    - Sharing
    - Updating
```

## Slide 72

```markdown
---
*Slide 72*
---

# Initialization

- At the beginning, each node can know only the reachability of nodes inside its autonomous system.
- Initial table for each speaker node.
- Node A1 is a speaker of AS1, B1 for AS2, C1 for AS3, and D1 for AS4.
- Node A1 creates an initial table that shows A1 to A5 are located in AS1 and can be reached through it. And so on.
```

## Slide 73

```markdown
---
*Slide 73*
---

# Initial routing table in path vector routing

- **A1 Table:**
  - Dest. Path
    - A1 AS1
    - A2 AS1
    - A3 AS1
    - A4 AS1
    - A5 AS1

- **C1 Table:**
  - Dest. Path
    - C1 AS3
    - C2 AS3
    - C3 AS3

- **B1 Table:**
  - Dest. Path
    - B1 AS2
    - B2 AS2
    - B3 AS2
    - B4 AS2

- **D1 Table:**
  - Dest. Path
    - D1 AS4
    - D2 AS4
    - D3 AS4
    - D4 AS4

> *Visual Explanation:*
> - Diagram shows network topology with Autonomous Systems (AS) 1, 2, 3, and 4.
> - Nodes A1, B1, C1, and D1 represent routers within each AS.
> - Solid lines indicate direct connections between routers.
> - Dashed lines within AS blocks show internal routing paths.
```

## Slide 74

```markdown
---
*Slide 74*
---

# Sharing

- Speaker in an Autonomous system shares its table with immediate neighbors.
    - A1 shares its table with node B1 and C1.
    - C1 shares its table with node D1, B1, A1.
    - B1 shares its table with node C1 and A1.
    - D1 shares its table with C1.
```

## Slide 75

```markdown
---
*Slide 75*
---

# Updating

- When speaker receives 2-column table from neighbor, it updates its own table by adding the nodes that are not in a routing table.
    - Adding its own AS and AS that sent the system.
- That table gives information about how to reach each node in other AS.

- **Example:**
    - If node A1 receives a packet for D1, it knows that packet should go from AS1 to AS2 and then AS4.
    - D1 receives packet for Node A2, it knows it should go through AS4 to AS3 and AS1.
```

## Slide 76

```markdown
---
*Slide 76*
---

# Stabilized tables for three autonomous systems

| Dest. | Path     |       | Dest. | Path     |       | Dest. | Path     |
|-------|----------|-------|-------|----------|-------|-------|----------|
| A1    | AS1      |       | A1    | AS2-AS1  |       | A1    | AS4-AS3-AS1 |
| ...   |          |       | ...   |          |       | ...   |          |
| A5    | AS1      |       | A5    | AS2-AS1  |       | A5    | AS4-AS3-AS1 |
| B1    | AS1-AS2  |       | B1    | AS1-AS2  |       | B1    | AS4-AS3-AS2 |
| ...   | AS1-AS2  |       | ...   | AS2      |       | ...   | AS4-AS3-AS2 |
| B4    | AS1-AS2  |       | B4    | AS2      |       | B4    | AS4-AS3-AS2 |
| C1    | AS1-AS3  |       | C1    | AS2-AS3  |       | C1    | AS4-AS3    |
| ...   | AS1-AS3  |       | ...   | AS2-AS3  |       | ...   | AS4-AS3    |
| C3    | AS1-AS3  |       | C3    | AS2-AS3  |       | C3    | AS4-AS3    |
| D1    | AS1-AS2-AS4 |    | D1    | AS2-AS3-AS4 |    | D1    | AS4       |
| ...   | AS1-AS2-AS4 |    | ...   | AS2-AS3-AS4 |    | ...   | AS4       |
| D4    | AS1-AS2-AS4 |    | D4    | AS2-AS3-AS4 |    | D4    | AS4       |

- A1 Table
- B1 Table
- C1 Table
- D1 Table
```

## Slide 77

```markdown
---
*Slide 77*
---

# Loop Preservation

- Instability of distance vector routing and creation of loop can be avoided in path vector routing.
- When router receives a message, it checks to see if its autonomous system is in the path to its destination.
- If it is, looping is involved and message is ignored.
```

## Slide 78

```markdown
---
*Slide 78*
---

# Policy Routing

- Policy routing can be easily implemented through path vector routing.
- When a router receives a message, it can check the path.
- If one of the AS listed in the path is against its policy, it can ignore that path and that destination.
- It does not update its routing table with this path, and it does not send this message to its neighbor.
```

## Slide 79

```markdown
---
*Slide 79*
---

# Optimal Path

- What is optimal path in path vector routing?
    - Looking for best path
- It is based on different criteria.
    - RIP uses hop count metric.
    - OSPF uses minimum delay as the metric.
- In previous organization each AS may have more than one path to a destination.
    - Path from AS1 to AS4 can be AS4-AS3-AS3-AS1, AS4-AS3-AS1.
    - Choose the one that had the smaller number of AS.
    - Other criteria: security, safety, and reliability.
```

## Slide 80

```markdown
---
*Slide 80*
---

# BGP

- Border Gateway Protocol is an Intradomain routing protocol.
- Types of AS: AS is divided into 3 categories.
    - **Stub AS:**
        - Has only one connection to another AS.
        - Data traffic cannot pass through a stub AS.
    - **Multihomed AS:**
        - Has more than one connection to other AS.
        - It can send data traffic to more than one AS, but there is no temporary traffic.
    - **Transit AS:**
        - A transit AS is a Multihomed AS that also allows transient traffic.
```

## Slide 81

```markdown
---
*Slide 81*
---

# Internal and external BGP sessions

> *Visual Explanation:*
> - Diagram shows two Autonomous Systems (AS 1 and AS 2).
> - AS 1 contains nodes A1, A2, A3, A4, A5.
> - AS 2 contains nodes B1, B2, B3, B4.
> - Solid line represents E-BGP session between A1 and B1.
> - Dashed lines represent I-BGP sessions within each AS.

---
*End of Document*
---
```

