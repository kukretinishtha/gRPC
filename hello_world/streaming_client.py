import grpc
import streaming_pb2
import streaming_pb2_grpc

def run_server_streaming():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = streaming_pb2_grpc.GreeterStub(channel)
        responses = stub.SayHelloStream(streaming_pb2.HelloRequest(name='World'))
        print('Server streaming responses:')
        for response in responses:
            print(response.message)

def run_bidirectional_streaming():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = streaming_pb2_grpc.GreeterStub(channel)
        def request_messages():
            for name in ['Alice', 'Bob', 'Charlie']:
                yield streaming_pb2.HelloRequest(name=name)
        responses = stub.Chat(request_messages())
        print('Bidirectional streaming responses:')
        for response in responses:
            print(response.message)

if __name__ == '__main__':
    run_server_streaming()
    run_bidirectional_streaming()
