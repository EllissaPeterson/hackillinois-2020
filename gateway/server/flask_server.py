from flask import Flask
from flask_cors import CORS

import logging
from flask import request
import datapackage

import grpc
import json

import to_gateway_pb2
import to_gateway_pb2_grpc

app = Flask(__name__)
CORS(app)

@app.route("/getmessage",methods=['GET', 'POST'])
def hello():
    print("Recieved Request")
    if request.method == 'POST':
        content = request.get_json()
        print(content)
        year = content.get('time')
        with grpc.insecure_channel('localhost:50052') as channel:
            stub = to_gateway_pb2_grpc.GeoGraphicGraphStub(channel)
            response = stub.getGeoData(to_gateway_pb2.Date(
                year=2017,
                month=1,
                day=1
            ))
            lst = []
            for r in response:
                d = {}
                d['Country']=r.country
                d['Confirmed']=r.confirmed
                d['ISO3']=r.iso3
                lst.append(d)
            jsondata = json.dumps(lst, separators=(',',':'))
            
            return jsondata       
            

    else:
        return "Fuck you"

@app.route("/")
def default():
    return "Fuck you"



if __name__ == '__main__':
   app.run(port=3002,debug=True)
