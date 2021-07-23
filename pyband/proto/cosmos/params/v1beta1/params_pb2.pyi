"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ParameterChangeProposal(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CHANGES_FIELD_NUMBER: builtins.int
    title: typing.Text = ...
    description: typing.Text = ...

    @property
    def changes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ParamChange]: ...

    def __init__(self,
        *,
        title : typing.Text = ...,
        description : typing.Text = ...,
        changes : typing.Optional[typing.Iterable[global___ParamChange]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"changes",b"changes",u"description",b"description",u"title",b"title"]) -> None: ...
global___ParameterChangeProposal = ParameterChangeProposal

class ParamChange(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SUBSPACE_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    subspace: typing.Text = ...
    key: typing.Text = ...
    value: typing.Text = ...

    def __init__(self,
        *,
        subspace : typing.Text = ...,
        key : typing.Text = ...,
        value : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"subspace",b"subspace",u"value",b"value"]) -> None: ...
global___ParamChange = ParamChange