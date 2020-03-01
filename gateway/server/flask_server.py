from flask import Flask
from flask_cors import CORS

import logging

import grpc

import to_gateway_pb2
import to_gateway_pb2_grpc

app = Flask(__name__)
CORS(app)

@app.route("/getmessage")
def hello():
    print("Recieved Request")
    print(request.form['time'])
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = to_gateway_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(to_gateway_pb2.geo_in(date=request.form['time']))
    return response.message

@app.route("/")
def default():
    return "Fuck you"



if __name__ == '__main__':
   app.run(port=3001)
