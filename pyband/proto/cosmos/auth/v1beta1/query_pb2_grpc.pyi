"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc

from .query_pb2 import *
class QueryStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Account:grpc.UnaryUnaryMultiCallable[
        global___QueryAccountRequest,
        global___QueryAccountResponse] = ...

    Params:grpc.UnaryUnaryMultiCallable[
        global___QueryParamsRequest,
        global___QueryParamsResponse] = ...


class QueryServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Account(self,
        request: global___QueryAccountRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryAccountResponse: ...

    @abc.abstractmethod
    def Params(self,
        request: global___QueryParamsRequest,
        context: grpc.ServicerContext,
    ) -> global___QueryParamsResponse: ...


def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...