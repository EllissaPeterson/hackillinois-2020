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
        corona = corona.replace(to_replace='Mainland China', value='China')
        corona = corona.replace(to_replace='Taiwan', value='China')
        corona = corona.replace(to_replace='Hong Kong', value='China')
        corona = corona.replace(to_replace='Macau', value='China')
        corona = corona.replace(to_replace='US', 
                                value='United States of America')
        corona = corona.replace(to_replace='UK', 
                                value='United Kingdom of Great Britain and Northern Ireland')
        iso = iso.loc[:,['official_name_en','ISO3166-1-numeric']]
        iso = iso.replace(to_replace='Republic of Korea', 
                                value='South Korea')
        iso = iso.replace(to_replace='Iran (Islamic Republic of)', 
                                value='Iran')
        iso = iso.replace(to_replace='Viet Nam', value='Vietnam')
        iso = iso.replace(to_replace='Russian Federation', value='Russia')
        corona = corona.drop(index=10)
        corona = corona.drop(index=102)
        corona = corona.merge(right=iso, how='left', 
                              right_on='official_name_en', 
                              left_on='Country/Region')
        corona = corona.drop(columns='official_name_en')
        
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
