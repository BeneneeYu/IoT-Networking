# Client-server Networking

## Requirements

### Client
- IoT artifact in the form of an edge-based smart refrigerator.
- Sends Grocery Orders and Health Status messages.
- Messages padded to create 1MB application-level packets (only for requests).
- Maximum Transfer Unit (MTU) imposed to 16 bytes.
- Implements different protocols for reliable transfer: GoBackN, SelectiveRepeat, and Alternating Bit.

### Servers
- Grocery Server:
  - Acknowledges with an "Order Placed" reply.
- Health Status Server:
  - Responds with a "You Are Healthy" reply.

### Network Layer
- Implements random number logic for packet forwarding:
  - (a) Send the chunk to the next hop.
  - (b) Delay the chunk.
  - (c) Drop the chunk.

### Flatbuffers
- Defines data structures using FlatBuffers.
- Extends message formats as required.
- Generates Flatbuffer schema and serialization code.
- Utilizes FlatBuffers API to manipulate data.

### Transport Layer
- Implements reliable transfer using different policies.
- Uses REQ socket at client and server, and DEALER-ROUTER socket at the router.
- Appends host name at the front for network and transport layers.

### ZMQ Packets
- Understands the structure of ZMQ packets: identity, null, and payload.
- Implements different behaviors for various ZMQ socket types (REQ, REP, ROUTER, DEALER).

### Testing
- Utilizes Mininet for setting up network topology.
- Executes test commands to deploy routers and servers.
- Starts a client on a specific node with given parameters (IP address and port).
- Tests the communication between client and servers.

