import grpc
from concurrent import futures
import time
import streaming_pb2
import streaming_pb2_grpc

class Greeter(streaming_pb2_grpc.GreeterServicer):
    def SayHelloStream(self, request, context):
        for i in range(5):
            yield streaming_pb2.HelloReply(message=f'Hello {request.name}, message {i+1}')
            time.sleep(1)

    def Chat(self, request_iterator, context):
        for req in request_iterator:
            yield streaming_pb2.HelloReply(message=f'Hello {req.name} (bidirectional)')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    streaming_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print('Streaming server started on port 50052')
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
