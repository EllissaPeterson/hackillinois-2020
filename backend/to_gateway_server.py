from concurrent import futures
import logging

import grpc

import to_gateway_pb2
import to_gateway_pb2_grpc

import backend

class Greeter(frontend_pb2_grpc.GreeterServicer):

    def geos(self, request, context):
        print("Heard")
        return to_gateway_pb2.geo_out(message='Hello, %s!' % request.name)


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