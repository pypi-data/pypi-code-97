# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from github.com.metaprov.modelaapi.services.connection.v1 import connection_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2


class ConnectionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListConnections = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.connection.v1.ConnectionService/ListConnections',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.ListConnectionsRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.ListConnectionsResponse.FromString,
                )
        self.CreateConnection = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.connection.v1.ConnectionService/CreateConnection',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.CreateConnectionRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.CreateConnectionResponse.FromString,
                )
        self.GetConnection = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.connection.v1.ConnectionService/GetConnection',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.GetConnectionRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.GetConnectionResponse.FromString,
                )
        self.UpdateConnection = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.connection.v1.ConnectionService/UpdateConnection',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.UpdateConnectionRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.UpdateConnectionResponse.FromString,
                )
        self.DeleteConnection = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.connection.v1.ConnectionService/DeleteConnection',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.DeleteConnectionRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.DeleteConnectionResponse.FromString,
                )
        self.TestConnection = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.connection.v1.ConnectionService/TestConnection',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.TestConnectionRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.TestConnectionResponse.FromString,
                )


class ConnectionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListConnections(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateConnection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConnection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateConnection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteConnection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestConnection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConnectionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListConnections': grpc.unary_unary_rpc_method_handler(
                    servicer.ListConnections,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.ListConnectionsRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.ListConnectionsResponse.SerializeToString,
            ),
            'CreateConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateConnection,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.CreateConnectionRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.CreateConnectionResponse.SerializeToString,
            ),
            'GetConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConnection,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.GetConnectionRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.GetConnectionResponse.SerializeToString,
            ),
            'UpdateConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateConnection,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.UpdateConnectionRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.UpdateConnectionResponse.SerializeToString,
            ),
            'DeleteConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteConnection,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.DeleteConnectionRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.DeleteConnectionResponse.SerializeToString,
            ),
            'TestConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.TestConnection,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.TestConnectionRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.TestConnectionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'github.com.metaprov.modelaapi.services.connection.v1.ConnectionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ConnectionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListConnections(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.connection.v1.ConnectionService/ListConnections',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.ListConnectionsRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.ListConnectionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.connection.v1.ConnectionService/CreateConnection',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.CreateConnectionRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.CreateConnectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.connection.v1.ConnectionService/GetConnection',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.GetConnectionRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.GetConnectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.connection.v1.ConnectionService/UpdateConnection',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.UpdateConnectionRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.UpdateConnectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.connection.v1.ConnectionService/DeleteConnection',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.DeleteConnectionRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.DeleteConnectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.connection.v1.ConnectionService/TestConnection',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.TestConnectionRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_connection_dot_v1_dot_connection__pb2.TestConnectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
