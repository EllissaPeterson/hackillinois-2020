import Messages_pb2_grpc, Messages_pb2
import time
class parserClient():
    def __init__(self):
        self.lastUpdate = time.localtime()
    def getData(self):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = Messages_pb2_grpc.MessengerStub(channel)
            response = stub.getDump(Messages_pb2.Date(month=1,day=1,year=1))
            return response
    def checkUpdate(self):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = Messages_pb2_grpc.MessengerStub(channel)
            response = stub.getDump(Messages_pb2.Date(month=time.tm_mon,day=time.tm_mday,year=time.tm_year))
            return response
