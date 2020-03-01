from concurrent import futures
import logging

import grpc

import frontend_pb2
import frontend_pb2_grpc


class Greeter(frontend_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print("Heard")
        return frontend_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    frontend_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Started")

    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()