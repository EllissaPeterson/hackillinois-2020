from concurrent import futures
import logging

import grpc

import to_gateway_pb2
import to_gateway_pb2_grpc
import datapackage

import clean
import pandas as pd

class GeoGraphicGraph(to_gateway_pb2_grpc.GeoGraphicGraphServicer):
    def getGeoData(self, request, context):    
        print("Received Geo Request")   
        iso_url = 'https://datahub.io/core/country-codes/datapackage.json'

        # to load data package into storage
        package = datapackage.Package(iso_url)

        # to load only tabular data
        resources = package.resources
        corona = None
        for resource in resources:
            if resource.tabular:
                iso = pd.read_csv(resource.descriptor['path'])
                corona = pd.read_csv('02-29-2020.csv')
                corona = clean.cl(corona, iso)
            
        for index, r in corona.iterrows(): 
            row = to_gateway_pb2.geoPoint(
                country = r["Country/Region"],
                confirmed = r["Confirmed"],
                iso3 = r["ISO3166-1-Alpha-3"]
            )
            yield row

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    to_gateway_pb2_grpc.add_GeoGraphicGraphServicer_to_server(GeoGraphicGraph(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Started")

    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()