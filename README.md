
# gRPC Hello World Example (Python)

This project demonstrates a simple gRPC server and client in Python using Protocol Buffers.

## Structure

- `helloworld.proto`: Protocol Buffers definition for the Greeter service
- `server.py`: gRPC server implementation
- `client.py`: gRPC client implementation
- `helloworld_pb2.py`, `helloworld_pb2_grpc.py`: Auto-generated Python code from the proto file

## Setup Instructions

1. **Install dependencies**
   ```bash
   pip install grpcio grpcio-tools
   ```

2. **Generate Python code from the proto file**
   Run this command in the `hello_world` directory:
   ```bash
   python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. helloworld.proto
   ```

3. **Run the server**
   ```bash
   python3 server.py
   ```

4. **Run the client**
   ```bash
   python3 client.py
   ```

## How the Flow Works

1. The client sends a `SayHello` request to the server with a name.
2. The server receives the request, processes it, and responds with a greeting message.
3. The client prints the greeting received from the server.

## Key Files Explained

- **helloworld.proto**: Defines the Greeter service and messages (`HelloRequest`, `HelloReply`).
- **server.py**: Implements the Greeter service and starts the gRPC server.
- **client.py**: Connects to the server and calls the `SayHello` RPC.


## Regenerating Code After Proto Changes

If you modify `helloworld.proto`, re-run the code generation command to update the Python files.

## References

- [gRPC Python Documentation](https://grpc.io/docs/languages/python/)
