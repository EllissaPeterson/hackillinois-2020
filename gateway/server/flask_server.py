from flask import Flask
from flask_cors import CORS

import logging

import grpc

import frontend_pb2
import frontend_pb2_grpc

app = Flask(__name__)
CORS(app)

@app.route("/getmessage")
def hello():
    print("Recieved Request")
    print(request.form['time'])
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = frontend_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(frontend_pb2.HelloRequest(time=request.form['time']))
    return response.message

@app.route("/")
def default():
    return "Fuck you"

def rpc():
   
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = frontend_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(frontend_pb2.HelloRequest(name='you'))

    return response


if __name__ == '__main__':
   app.run(port=3001)
