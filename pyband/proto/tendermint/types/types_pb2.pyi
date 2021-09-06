"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import tendermint.crypto.proof_pb2
import tendermint.types.validator_pb2
import tendermint.version.types_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# BlockIdFlag indicates which BlcokID the signature is for
class BlockIDFlag(_BlockIDFlag, metaclass=_BlockIDFlagEnumTypeWrapper):
    pass
class _BlockIDFlag:
    V = typing.NewType('V', builtins.int)
class _BlockIDFlagEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_BlockIDFlag.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    BLOCK_ID_FLAG_UNKNOWN = BlockIDFlag.V(0)
    BLOCK_ID_FLAG_ABSENT = BlockIDFlag.V(1)
    BLOCK_ID_FLAG_COMMIT = BlockIDFlag.V(2)
    BLOCK_ID_FLAG_NIL = BlockIDFlag.V(3)

BLOCK_ID_FLAG_UNKNOWN = BlockIDFlag.V(0)
BLOCK_ID_FLAG_ABSENT = BlockIDFlag.V(1)
BLOCK_ID_FLAG_COMMIT = BlockIDFlag.V(2)
BLOCK_ID_FLAG_NIL = BlockIDFlag.V(3)
global___BlockIDFlag = BlockIDFlag


# SignedMsgType is a type of signed message in the consensus.
class SignedMsgType(_SignedMsgType, metaclass=_SignedMsgTypeEnumTypeWrapper):
    pass
class _SignedMsgType:
    V = typing.NewType('V', builtins.int)
class _SignedMsgTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SignedMsgType.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    SIGNED_MSG_TYPE_UNKNOWN = SignedMsgType.V(0)
    # Votes
    SIGNED_MSG_TYPE_PREVOTE = SignedMsgType.V(1)
    SIGNED_MSG_TYPE_PRECOMMIT = SignedMsgType.V(2)
    # Proposals
    SIGNED_MSG_TYPE_PROPOSAL = SignedMsgType.V(32)

SIGNED_MSG_TYPE_UNKNOWN = SignedMsgType.V(0)
# Votes
SIGNED_MSG_TYPE_PREVOTE = SignedMsgType.V(1)
SIGNED_MSG_TYPE_PRECOMMIT = SignedMsgType.V(2)
# Proposals
SIGNED_MSG_TYPE_PROPOSAL = SignedMsgType.V(32)
global___SignedMsgType = SignedMsgType


# PartsetHeader
class PartSetHeader(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOTAL_FIELD_NUMBER: builtins.int
    HASH_FIELD_NUMBER: builtins.int
    total: builtins.int = ...
    hash: builtins.bytes = ...
    def __init__(self,
        *,
        total : builtins.int = ...,
        hash : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"hash",b"hash",u"total",b"total"]) -> None: ...
global___PartSetHeader = PartSetHeader

class Part(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INDEX_FIELD_NUMBER: builtins.int
    BYTES_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    index: builtins.int = ...
    bytes: builtins.bytes = ...
    @property
    def proof(self) -> tendermint.crypto.proof_pb2.Proof: ...
    def __init__(self,
        *,
        index : builtins.int = ...,
        bytes : builtins.bytes = ...,
        proof : typing.Optional[tendermint.crypto.proof_pb2.Proof] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"proof",b"proof"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bytes",b"bytes",u"index",b"index",u"proof",b"proof"]) -> None: ...
global___Part = Part

# BlockID
class BlockID(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HASH_FIELD_NUMBER: builtins.int
    PART_SET_HEADER_FIELD_NUMBER: builtins.int
    hash: builtins.bytes = ...
    @property
    def part_set_header(self) -> global___PartSetHeader: ...
    def __init__(self,
        *,
        hash : builtins.bytes = ...,
        part_set_header : typing.Optional[global___PartSetHeader] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"part_set_header",b"part_set_header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"hash",b"hash",u"part_set_header",b"part_set_header"]) -> None: ...
global___BlockID = BlockID

# --------------------------------

# Header defines the structure of a Tendermint block header.
class Header(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VERSION_FIELD_NUMBER: builtins.int
    CHAIN_ID_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    LAST_BLOCK_ID_FIELD_NUMBER: builtins.int
    LAST_COMMIT_HASH_FIELD_NUMBER: builtins.int
    DATA_HASH_FIELD_NUMBER: builtins.int
    VALIDATORS_HASH_FIELD_NUMBER: builtins.int
    NEXT_VALIDATORS_HASH_FIELD_NUMBER: builtins.int
    CONSENSUS_HASH_FIELD_NUMBER: builtins.int
    APP_HASH_FIELD_NUMBER: builtins.int
    LAST_RESULTS_HASH_FIELD_NUMBER: builtins.int
    EVIDENCE_HASH_FIELD_NUMBER: builtins.int
    PROPOSER_ADDRESS_FIELD_NUMBER: builtins.int
    # basic block info
    @property
    def version(self) -> tendermint.version.types_pb2.Consensus: ...
    chain_id: typing.Text = ...
    height: builtins.int = ...
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # prev block info
    @property
    def last_block_id(self) -> global___BlockID: ...
    # hashes of block data
    # commit from validators from the last block
    last_commit_hash: builtins.bytes = ...
    # transactions
    data_hash: builtins.bytes = ...
    # hashes from the app output from the prev block
    # validators for the current block
    validators_hash: builtins.bytes = ...
    # validators for the next block
    next_validators_hash: builtins.bytes = ...
    # consensus params for current block
    consensus_hash: builtins.bytes = ...
    # state after txs from the previous block
    app_hash: builtins.bytes = ...
    # root hash of all results from the txs from the previous block
    last_results_hash: builtins.bytes = ...
    # consensus info
    # evidence included in the block
    evidence_hash: builtins.bytes = ...
    # original proposer of the block
    proposer_address: builtins.bytes = ...
    def __init__(self,
        *,
        version : typing.Optional[tendermint.version.types_pb2.Consensus] = ...,
        chain_id : typing.Text = ...,
        height : builtins.int = ...,
        time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        last_block_id : typing.Optional[global___BlockID] = ...,
        last_commit_hash : builtins.bytes = ...,
        data_hash : builtins.bytes = ...,
        validators_hash : builtins.bytes = ...,
        next_validators_hash : builtins.bytes = ...,
        consensus_hash : builtins.bytes = ...,
        app_hash : builtins.bytes = ...,
        last_results_hash : builtins.bytes = ...,
        evidence_hash : builtins.bytes = ...,
        proposer_address : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"last_block_id",b"last_block_id",u"time",b"time",u"version",b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"app_hash",b"app_hash",u"chain_id",b"chain_id",u"consensus_hash",b"consensus_hash",u"data_hash",b"data_hash",u"evidence_hash",b"evidence_hash",u"height",b"height",u"last_block_id",b"last_block_id",u"last_commit_hash",b"last_commit_hash",u"last_results_hash",b"last_results_hash",u"next_validators_hash",b"next_validators_hash",u"proposer_address",b"proposer_address",u"time",b"time",u"validators_hash",b"validators_hash",u"version",b"version"]) -> None: ...
global___Header = Header

# Data contains the set of transactions included in the block
class Data(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TXS_FIELD_NUMBER: builtins.int
    # Txs that will be applied by state @ block.Height+1.
    # NOTE: not all txs here are valid.  We're just agreeing on the order first.
    # This means that block.AppHash does not include these txs.
    @property
    def txs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    def __init__(self,
        *,
        txs : typing.Optional[typing.Iterable[builtins.bytes]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"txs",b"txs"]) -> None: ...
global___Data = Data

# Vote represents a prevote, precommit, or commit vote from validators for
# consensus.
class Vote(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TYPE_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    BLOCK_ID_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    VALIDATOR_INDEX_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    type: global___SignedMsgType.V = ...
    height: builtins.int = ...
    round: builtins.int = ...
    # zero if vote is nil.
    @property
    def block_id(self) -> global___BlockID: ...
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    validator_address: builtins.bytes = ...
    validator_index: builtins.int = ...
    signature: builtins.bytes = ...
    def __init__(self,
        *,
        type : global___SignedMsgType.V = ...,
        height : builtins.int = ...,
        round : builtins.int = ...,
        block_id : typing.Optional[global___BlockID] = ...,
        timestamp : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        validator_address : builtins.bytes = ...,
        validator_index : builtins.int = ...,
        signature : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"block_id",b"block_id",u"timestamp",b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"block_id",b"block_id",u"height",b"height",u"round",b"round",u"signature",b"signature",u"timestamp",b"timestamp",u"type",b"type",u"validator_address",b"validator_address",u"validator_index",b"validator_index"]) -> None: ...
global___Vote = Vote

# Commit contains the evidence that a block was committed by a set of validators.
class Commit(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HEIGHT_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    BLOCK_ID_FIELD_NUMBER: builtins.int
    SIGNATURES_FIELD_NUMBER: builtins.int
    height: builtins.int = ...
    round: builtins.int = ...
    @property
    def block_id(self) -> global___BlockID: ...
    @property
    def signatures(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CommitSig]: ...
    def __init__(self,
        *,
        height : builtins.int = ...,
        round : builtins.int = ...,
        block_id : typing.Optional[global___BlockID] = ...,
        signatures : typing.Optional[typing.Iterable[global___CommitSig]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"block_id",b"block_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"block_id",b"block_id",u"height",b"height",u"round",b"round",u"signatures",b"signatures"]) -> None: ...
global___Commit = Commit

# CommitSig is a part of the Vote included in a Commit.
class CommitSig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BLOCK_ID_FLAG_FIELD_NUMBER: builtins.int
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    block_id_flag: global___BlockIDFlag.V = ...
    validator_address: builtins.bytes = ...
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    signature: builtins.bytes = ...
    def __init__(self,
        *,
        block_id_flag : global___BlockIDFlag.V = ...,
        validator_address : builtins.bytes = ...,
        timestamp : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        signature : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"timestamp",b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"block_id_flag",b"block_id_flag",u"signature",b"signature",u"timestamp",b"timestamp",u"validator_address",b"validator_address"]) -> None: ...
global___CommitSig = CommitSig

class Proposal(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TYPE_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    POL_ROUND_FIELD_NUMBER: builtins.int
    BLOCK_ID_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    type: global___SignedMsgType.V = ...
    height: builtins.int = ...
    round: builtins.int = ...
    pol_round: builtins.int = ...
    @property
    def block_id(self) -> global___BlockID: ...
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    signature: builtins.bytes = ...
    def __init__(self,
        *,
        type : global___SignedMsgType.V = ...,
        height : builtins.int = ...,
        round : builtins.int = ...,
        pol_round : builtins.int = ...,
        block_id : typing.Optional[global___BlockID] = ...,
        timestamp : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        signature : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"block_id",b"block_id",u"timestamp",b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"block_id",b"block_id",u"height",b"height",u"pol_round",b"pol_round",u"round",b"round",u"signature",b"signature",u"timestamp",b"timestamp",u"type",b"type"]) -> None: ...
global___Proposal = Proposal

class SignedHeader(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HEADER_FIELD_NUMBER: builtins.int
    COMMIT_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> global___Header: ...
    @property
    def commit(self) -> global___Commit: ...
    def __init__(self,
        *,
        header : typing.Optional[global___Header] = ...,
        commit : typing.Optional[global___Commit] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"commit",b"commit",u"header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"commit",b"commit",u"header",b"header"]) -> None: ...
global___SignedHeader = SignedHeader

class LightBlock(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SIGNED_HEADER_FIELD_NUMBER: builtins.int
    VALIDATOR_SET_FIELD_NUMBER: builtins.int
    @property
    def signed_header(self) -> global___SignedHeader: ...
    @property
    def validator_set(self) -> tendermint.types.validator_pb2.ValidatorSet: ...
    def __init__(self,
        *,
        signed_header : typing.Optional[global___SignedHeader] = ...,
        validator_set : typing.Optional[tendermint.types.validator_pb2.ValidatorSet] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"signed_header",b"signed_header",u"validator_set",b"validator_set"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"signed_header",b"signed_header",u"validator_set",b"validator_set"]) -> None: ...
global___LightBlock = LightBlock

class BlockMeta(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BLOCK_ID_FIELD_NUMBER: builtins.int
    BLOCK_SIZE_FIELD_NUMBER: builtins.int
    HEADER_FIELD_NUMBER: builtins.int
    NUM_TXS_FIELD_NUMBER: builtins.int
    @property
    def block_id(self) -> global___BlockID: ...
    block_size: builtins.int = ...
    @property
    def header(self) -> global___Header: ...
    num_txs: builtins.int = ...
    def __init__(self,
        *,
        block_id : typing.Optional[global___BlockID] = ...,
        block_size : builtins.int = ...,
        header : typing.Optional[global___Header] = ...,
        num_txs : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"block_id",b"block_id",u"header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"block_id",b"block_id",u"block_size",b"block_size",u"header",b"header",u"num_txs",b"num_txs"]) -> None: ...
global___BlockMeta = BlockMeta

# TxProof represents a Merkle proof of the presence of a transaction in the Merkle tree.
class TxProof(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ROOT_HASH_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    root_hash: builtins.bytes = ...
    data: builtins.bytes = ...
    @property
    def proof(self) -> tendermint.crypto.proof_pb2.Proof: ...
    def __init__(self,
        *,
        root_hash : builtins.bytes = ...,
        data : builtins.bytes = ...,
        proof : typing.Optional[tendermint.crypto.proof_pb2.Proof] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"proof",b"proof"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"data",b"data",u"proof",b"proof",u"root_hash",b"root_hash"]) -> None: ...
global___TxProof = TxProof
