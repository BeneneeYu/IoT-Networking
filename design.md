# Client-Server Networking

## Overview
This project involves an edge-based smart refrigerator connected to two different servers for sending grocery orders and health status messages.

## Operation Details
- Serialized buffers are padded to create 1MB application-level packets (only for requests).
- Maximum Transfer Unit (MTU) is imposed to 16 bytes, dividing 1MB packets into 64 16-byte chunks with guaranteed order.
- Sliding window size for GoBackN and SelectiveRepeat is set to 8 chunks at a time, while for Alternating Bit, the window size is always 1 chunk.
- Integration of skeleton code with dealer-router scaffolding code.
- Artificial blocks are set to simulate packet delays and drops at the network layer.

## Strategy for Network Layer
Random number logic is used to decide whether to:
- Send the chunk to the next hop.
- Delay the chunk.
- Drop the chunk altogether.

## System Structure
The system consists of:
- Skeleton code.
- Refrigerator, grocery server, health server, client, and server components.
- Custom application and transport protocols for communication between components.

### Samples
- applnlayer/ApplnMessageTypes: define data classes and printing function.
- applnlayer/CustomApplnProtocol: base class of client/server, implements functions to send/receive application objects, send/receive request/response based on network layer.

### Refrigerator
- Generates requests and send to servers.
- Holds a grocery store server appln object and a health status center appln object (Instance of CustomApplnProtocol).
- Appln object holds an instance of CustomTransportProtocolObject, which holds a NWProtoObj, uses IP and Port passed from upper layer.
- To send appln message, use CustomTransportProtocolObject to send segement using networkObject to send packet.
- NetworkObj uses socket created when initialized to send.

```
GroceryOrderServer (say 10.0.0.5:5555)
- groc_obj (ApplnProtoObj)
-- xport_obj (XPortProtoObj)
--- nw_obj (NWProtoObj)
---- socket (zmq.DEALER) (should be 10.0.0.2:4444)

HealthStatusServer (say 10.0.0.6:5555)
- health_obj (ApplnProtoObj)
-- xport_obj (XPortProtoObj)
--- nw_obj (NWProtoObj)
---- socket (zmq.DEALER) (should be 10.0.0.2:4444)
```

```
send_grocery_order
- xport_obj.send_appln_msg
-- send_segment
--- nw_obj.send_packet
---- socket.send (say 10.0.0.5:5555)

Order server will respond and send response to 10.0.0.5:5555
recv_response
- xport_obj.recv_appln_msg
-- recv_segment
--- nw_obj.recv_packet
---- socket.recv (say 10.0.0.5:5555)
```

### Grocery Order

### grocery_server

- Instantiate a CustomApplnProtocol to act as server, continuously listening to requests and respond (needs IP and Port).

- Holds an instance of ApplnProtoObj, grocery_obj.

- To receiver, use method **recv_request** in ApplnProtoObj. 

- **Recv_request** will use **recv_appln_msg** in xport_obj, an instance of CustomTransportProtocol.
- **Recv_appln_msg** will use **recv_segment**, recv_segment will use recv_packet in nw_obj, an instance of CustomNetworkProtocol.

```
grocery_obj (ApplnProtoObj)
- xport_obj (XPortProtoObj)
-- nw_obj (NWProtoObj)
--- socket (zmq.REP)
```

## Data Flows

### **Client**

**appln_obj.send_order**=>**xport_obj.send_appln_smg**=>**send_segment**=>**nw_obj.send_packet**=>**socket.send**

### **Server**

**appln_obj.recv_request**=>**xport_obj.recv_appln_msg**=>**recv_segment**=>**nw_obj.recv_packet**=>**socket.recv**
## Unit Definitions
- Segments: A segment is the unit of end-to-end transmission in the TCP protocol. A segment consists of a TCP header followed by application data. A segment is transmitted by encapsulation inside an IP datagram.
- IP Datagram: The unit of end-to-end transmission in the IP protocol.
- Packet: The unit of data passed across the interface between the internet layer and the link layer.
- Frame: The unit of transmission in a link layer protocol.
- data=>segment=>packet=>frame

## Implementation Details
- Collection of end-to-end latency data.
- Usage of Flatbuffers for data structure definition, schema creation, and serialization code generation.
- Implementation of reliable transfer in the transport layer using different policies.
- No flow or congestion control mechanisms.
- Usage of REQ socket at the client, REQ socket at the server, and DEALER-ROUTER socket at the router for communication.
- Detailed explanation of the ZMQ packet structure and message passing mechanisms.

## How to Test Instructions
1. Deploy the network topology using Mininet with seven nodes.
2. Execute the deployment commands to set up routers and servers.
3. Open an xterm session for the client node.
4. Run the refrigerator.py script on the client node with appropriate parameters to simulate message transmission.

