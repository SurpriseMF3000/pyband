"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# ConsensusParams contains consensus critical parameters that determine the
# validity of blocks.
class ConsensusParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BLOCK_FIELD_NUMBER: builtins.int
    EVIDENCE_FIELD_NUMBER: builtins.int
    VALIDATOR_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    @property
    def block(self) -> global___BlockParams: ...
    @property
    def evidence(self) -> global___EvidenceParams: ...
    @property
    def validator(self) -> global___ValidatorParams: ...
    @property
    def version(self) -> global___VersionParams: ...
    def __init__(self,
        *,
        block : typing.Optional[global___BlockParams] = ...,
        evidence : typing.Optional[global___EvidenceParams] = ...,
        validator : typing.Optional[global___ValidatorParams] = ...,
        version : typing.Optional[global___VersionParams] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"block",b"block",u"evidence",b"evidence",u"validator",b"validator",u"version",b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"block",b"block",u"evidence",b"evidence",u"validator",b"validator",u"version",b"version"]) -> None: ...
global___ConsensusParams = ConsensusParams

# BlockParams contains limits on the block size.
class BlockParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MAX_BYTES_FIELD_NUMBER: builtins.int
    MAX_GAS_FIELD_NUMBER: builtins.int
    TIME_IOTA_MS_FIELD_NUMBER: builtins.int
    # Max block size, in bytes.
    # Note: must be greater than 0
    max_bytes: builtins.int = ...
    # Max gas per block.
    # Note: must be greater or equal to -1
    max_gas: builtins.int = ...
    # Minimum time increment between consecutive blocks (in milliseconds) If the
    # block header timestamp is ahead of the system clock, decrease this value.
    #
    # Not exposed to the application.
    time_iota_ms: builtins.int = ...
    def __init__(self,
        *,
        max_bytes : builtins.int = ...,
        max_gas : builtins.int = ...,
        time_iota_ms : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"max_bytes",b"max_bytes",u"max_gas",b"max_gas",u"time_iota_ms",b"time_iota_ms"]) -> None: ...
global___BlockParams = BlockParams

# EvidenceParams determine how we handle evidence of malfeasance.
class EvidenceParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MAX_AGE_NUM_BLOCKS_FIELD_NUMBER: builtins.int
    MAX_AGE_DURATION_FIELD_NUMBER: builtins.int
    MAX_BYTES_FIELD_NUMBER: builtins.int
    # Max age of evidence, in blocks.
    #
    # The basic formula for calculating this is: MaxAgeDuration / {average block
    # time}.
    max_age_num_blocks: builtins.int = ...
    # Max age of evidence, in time.
    #
    # It should correspond with an app's "unbonding period" or other similar
    # mechanism for handling [Nothing-At-Stake
    # attacks](https://github.com/ethereum/wiki/wiki/Proof-of-Stake-FAQ#what-is-the-nothing-at-stake-problem-and-how-can-it-be-fixed).
    @property
    def max_age_duration(self) -> google.protobuf.duration_pb2.Duration: ...
    # This sets the maximum size of total evidence in bytes that can be committed in a single block.
    # and should fall comfortably under the max block bytes.
    # Default is 1048576 or 1MB
    max_bytes: builtins.int = ...
    def __init__(self,
        *,
        max_age_num_blocks : builtins.int = ...,
        max_age_duration : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        max_bytes : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"max_age_duration",b"max_age_duration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"max_age_duration",b"max_age_duration",u"max_age_num_blocks",b"max_age_num_blocks",u"max_bytes",b"max_bytes"]) -> None: ...
global___EvidenceParams = EvidenceParams

# ValidatorParams restrict the public key types validators can use.
# NOTE: uses ABCI pubkey naming, not Amino names.
class ValidatorParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PUB_KEY_TYPES_FIELD_NUMBER: builtins.int
    @property
    def pub_key_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        pub_key_types : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"pub_key_types",b"pub_key_types"]) -> None: ...
global___ValidatorParams = ValidatorParams

# VersionParams contains the ABCI application version.
class VersionParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    APP_VERSION_FIELD_NUMBER: builtins.int
    app_version: builtins.int = ...
    def __init__(self,
        *,
        app_version : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"app_version",b"app_version"]) -> None: ...
global___VersionParams = VersionParams

# HashedParams is a subset of ConsensusParams.
#
# It is hashed into the Header.ConsensusHash.
class HashedParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BLOCK_MAX_BYTES_FIELD_NUMBER: builtins.int
    BLOCK_MAX_GAS_FIELD_NUMBER: builtins.int
    block_max_bytes: builtins.int = ...
    block_max_gas: builtins.int = ...
    def __init__(self,
        *,
        block_max_bytes : builtins.int = ...,
        block_max_gas : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"block_max_bytes",b"block_max_bytes",u"block_max_gas",b"block_max_gas"]) -> None: ...
global___HashedParams = HashedParams
