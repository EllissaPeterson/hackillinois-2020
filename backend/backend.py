import clean
import datapackage
import pandas as pd

iso_url = 'https://datahub.io/core/country-codes/datapackage.json'

# to load data package into storage
package = datapackage.Package(iso_url)

# to load only tabular data
resources = package.resources
for resource in resources:
    if resource.tabular:
        iso = pd.read_csv(resource.descriptor['path'])
        corona = pd.read_csv('02-29-2020.csv')
        clean (corona, iso)
#
#from concurrent import futures
#from __future__ import print_function
#import logging
#import grpc
#
## for reading from database
#import filein_pb2
#import filein_pb2_grpc
#
## for writing to gateway
#import fileout_pb2
#import fileout_pb2_grpc
#
## get data from database
#def run():
#    
#    with grpc.insecure_channel('localhost:50051') as channel:
#        stub = filein_pb2_grpc.databaseStub(channel)
#        response = stub.readAll(filein_pb2.read(ready='yes'))
#    # add response to dataframe
#
## give data to gateway
#class out ():
#    
#    def temps (self, request, context):
#        return fileout_pb2.temp_pt()
#    
#    def geos (self, request, context):
#        return fileout_pb2.geo_pt()
#    
