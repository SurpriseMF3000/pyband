"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class App(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROTOCOL_FIELD_NUMBER: builtins.int
    SOFTWARE_FIELD_NUMBER: builtins.int
    protocol: builtins.int = ...
    software: typing.Text = ...

    def __init__(self,
        *,
        protocol : builtins.int = ...,
        software : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"protocol",b"protocol",u"software",b"software"]) -> None: ...
global___App = App

class Consensus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BLOCK_FIELD_NUMBER: builtins.int
    APP_FIELD_NUMBER: builtins.int
    block: builtins.int = ...
    app: builtins.int = ...

    def __init__(self,
        *,
        block : builtins.int = ...,
        app : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"app",b"app",u"block",b"block"]) -> None: ...
global___Consensus = Consensus