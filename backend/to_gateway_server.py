from concurrent import futures
import logging

import grpc

import to_gateway_pb2
import to_gateway_pb2_grpc
import datapackage

import clean
import pandas as pd

class gatewayServer():
    
    class GeoGraphicGraph(to_gateway_pb2_grpc.GeoGraphicGraphServicer):
        def getGeoData(self, request, context):          
            d = data.getData()
            for index, r in d.iterrows(): 
                row = to_gateway_pb2.geoPoint(
                    country = r["Country/Region"],
                    confirmed = r["Confirmed"],
                    iso3 = r["ISO3166-1-Alpha-3"]
                )
                yield row
    def __init__(self,d):
        self.data = d
    def start(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        to_gateway_pb2_grpc.add_GeoGraphicGraphServicer_to_server(self.GeoGraphicGraph(), server)
        server.add_insecure_port('[::]:50052')
        server.start()
        server.wait_for_termination()
    
