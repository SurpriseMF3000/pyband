"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc

from .query_pb2 import *
# Query provides defines the gRPC querier service.
class QueryStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    # Params returns the total set of minting parameters.
    Params:grpc.UnaryUnaryMultiCallable[
        global___QueryParamsRequest,
        global___QueryParamsResponse] = ...

    # Inflation returns the current minting inflation value.
    Inflation:grpc.UnaryUnaryMultiCallable[
        global___QueryInflationRequest,
        global___QueryInflationResponse] = ...

    # AnnualProvisions current minting annual provisions value.
    AnnualProvisions:grpc.UnaryUnaryMultiCallable[
        global___QueryAnnualProvisionsRequest,
        global___QueryAnnualProvisionsResponse] = ...


# Query provides defines the gRPC querier service.
class QueryServicer(metaclass=abc.ABCMeta):
    # Params returns the total set of minting parameters.
    @abc.abstractmethod
    def Params(self,
        request: global___QueryParamsRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryParamsResponse: ...

    # Inflation returns the current minting inflation value.
    @abc.abstractmethod
    def Inflation(self,
        request: global___QueryInflationRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryInflationResponse: ...

    # AnnualProvisions current minting annual provisions value.
    @abc.abstractmethod
    def AnnualProvisions(self,
        request: global___QueryAnnualProvisionsRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryAnnualProvisionsResponse: ...


def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...
