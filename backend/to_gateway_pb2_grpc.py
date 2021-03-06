# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import to_gateway_pb2 as to__gateway__pb2


class GeoGraphicGraphStub(object):
  """geographic service definition
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getGeoData = channel.unary_stream(
        '/GeoGraphicGraph/getGeoData',
        request_serializer=to__gateway__pb2.Date.SerializeToString,
        response_deserializer=to__gateway__pb2.geoPoint.FromString,
        )


class GeoGraphicGraphServicer(object):
  """geographic service definition
  """

  def getGeoData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GeoGraphicGraphServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getGeoData': grpc.unary_stream_rpc_method_handler(
          servicer.getGeoData,
          request_deserializer=to__gateway__pb2.Date.FromString,
          response_serializer=to__gateway__pb2.geoPoint.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'GeoGraphicGraph', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
