"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import confio.proofs_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import ibc.core.client.v1.client_pb2
import ibc.core.commitment.v1.commitment_pb2
import tendermint.types.types_pb2
import tendermint.types.validator_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# ClientState from Tendermint tracks the current validator set, latest height,
# and a possible frozen height.
class ClientState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CHAIN_ID_FIELD_NUMBER: builtins.int
    TRUST_LEVEL_FIELD_NUMBER: builtins.int
    TRUSTING_PERIOD_FIELD_NUMBER: builtins.int
    UNBONDING_PERIOD_FIELD_NUMBER: builtins.int
    MAX_CLOCK_DRIFT_FIELD_NUMBER: builtins.int
    FROZEN_HEIGHT_FIELD_NUMBER: builtins.int
    LATEST_HEIGHT_FIELD_NUMBER: builtins.int
    PROOF_SPECS_FIELD_NUMBER: builtins.int
    UPGRADE_PATH_FIELD_NUMBER: builtins.int
    ALLOW_UPDATE_AFTER_EXPIRY_FIELD_NUMBER: builtins.int
    ALLOW_UPDATE_AFTER_MISBEHAVIOUR_FIELD_NUMBER: builtins.int
    chain_id: typing.Text = ...
    @property
    def trust_level(self) -> global___Fraction: ...
    # duration of the period since the LastestTimestamp during which the
    # submitted headers are valid for upgrade
    @property
    def trusting_period(self) -> google.protobuf.duration_pb2.Duration: ...
    # duration of the staking unbonding period
    @property
    def unbonding_period(self) -> google.protobuf.duration_pb2.Duration: ...
    # defines how much new (untrusted) header's Time can drift into the future.
    @property
    def max_clock_drift(self) -> google.protobuf.duration_pb2.Duration: ...
    # Block height when the client was frozen due to a misbehaviour
    @property
    def frozen_height(self) -> ibc.core.client.v1.client_pb2.Height: ...
    # Latest height the client was updated to
    @property
    def latest_height(self) -> ibc.core.client.v1.client_pb2.Height: ...
    # Proof specifications used in verifying counterparty state
    @property
    def proof_specs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[confio.proofs_pb2.ProofSpec]: ...
    # Path at which next upgraded client will be committed.
    # Each element corresponds to the key for a single CommitmentProof in the
    # chained proof. NOTE: ClientState must stored under
    # `{upgradePath}/{upgradeHeight}/clientState` ConsensusState must be stored
    # under `{upgradepath}/{upgradeHeight}/consensusState` For SDK chains using
    # the default upgrade module, upgrade_path should be []string{"upgrade",
    # "upgradedIBCState"}`
    @property
    def upgrade_path(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    # This flag, when set to true, will allow governance to recover a client
    # which has expired
    allow_update_after_expiry: builtins.bool = ...
    # This flag, when set to true, will allow governance to unfreeze a client
    # whose chain has experienced a misbehaviour event
    allow_update_after_misbehaviour: builtins.bool = ...
    def __init__(self,
        *,
        chain_id : typing.Text = ...,
        trust_level : typing.Optional[global___Fraction] = ...,
        trusting_period : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        unbonding_period : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        max_clock_drift : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        frozen_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        latest_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        proof_specs : typing.Optional[typing.Iterable[confio.proofs_pb2.ProofSpec]] = ...,
        upgrade_path : typing.Optional[typing.Iterable[typing.Text]] = ...,
        allow_update_after_expiry : builtins.bool = ...,
        allow_update_after_misbehaviour : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"frozen_height",b"frozen_height",u"latest_height",b"latest_height",u"max_clock_drift",b"max_clock_drift",u"trust_level",b"trust_level",u"trusting_period",b"trusting_period",u"unbonding_period",b"unbonding_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"allow_update_after_expiry",b"allow_update_after_expiry",u"allow_update_after_misbehaviour",b"allow_update_after_misbehaviour",u"chain_id",b"chain_id",u"frozen_height",b"frozen_height",u"latest_height",b"latest_height",u"max_clock_drift",b"max_clock_drift",u"proof_specs",b"proof_specs",u"trust_level",b"trust_level",u"trusting_period",b"trusting_period",u"unbonding_period",b"unbonding_period",u"upgrade_path",b"upgrade_path"]) -> None: ...
global___ClientState = ClientState

# ConsensusState defines the consensus state from Tendermint.
class ConsensusState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TIMESTAMP_FIELD_NUMBER: builtins.int
    ROOT_FIELD_NUMBER: builtins.int
    NEXT_VALIDATORS_HASH_FIELD_NUMBER: builtins.int
    # timestamp that corresponds to the block height in which the ConsensusState
    # was stored.
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # commitment root (i.e app hash)
    @property
    def root(self) -> ibc.core.commitment.v1.commitment_pb2.MerkleRoot: ...
    next_validators_hash: builtins.bytes = ...
    def __init__(self,
        *,
        timestamp : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        root : typing.Optional[ibc.core.commitment.v1.commitment_pb2.MerkleRoot] = ...,
        next_validators_hash : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"root",b"root",u"timestamp",b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"next_validators_hash",b"next_validators_hash",u"root",b"root",u"timestamp",b"timestamp"]) -> None: ...
global___ConsensusState = ConsensusState

# Misbehaviour is a wrapper over two conflicting Headers
# that implements Misbehaviour interface expected by ICS-02
class Misbehaviour(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CLIENT_ID_FIELD_NUMBER: builtins.int
    HEADER_1_FIELD_NUMBER: builtins.int
    HEADER_2_FIELD_NUMBER: builtins.int
    client_id: typing.Text = ...
    @property
    def header_1(self) -> global___Header: ...
    @property
    def header_2(self) -> global___Header: ...
    def __init__(self,
        *,
        client_id : typing.Text = ...,
        header_1 : typing.Optional[global___Header] = ...,
        header_2 : typing.Optional[global___Header] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"header_1",b"header_1",u"header_2",b"header_2"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"client_id",b"client_id",u"header_1",b"header_1",u"header_2",b"header_2"]) -> None: ...
global___Misbehaviour = Misbehaviour

# Header defines the Tendermint client consensus Header.
# It encapsulates all the information necessary to update from a trusted
# Tendermint ConsensusState. The inclusion of TrustedHeight and
# TrustedValidators allows this update to process correctly, so long as the
# ConsensusState for the TrustedHeight exists, this removes race conditions
# among relayers The SignedHeader and ValidatorSet are the new untrusted update
# fields for the client. The TrustedHeight is the height of a stored
# ConsensusState on the client that will be used to verify the new untrusted
# header. The Trusted ConsensusState must be within the unbonding period of
# current time in order to correctly verify, and the TrustedValidators must
# hash to TrustedConsensusState.NextValidatorsHash since that is the last
# trusted validator set at the TrustedHeight.
class Header(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SIGNED_HEADER_FIELD_NUMBER: builtins.int
    VALIDATOR_SET_FIELD_NUMBER: builtins.int
    TRUSTED_HEIGHT_FIELD_NUMBER: builtins.int
    TRUSTED_VALIDATORS_FIELD_NUMBER: builtins.int
    @property
    def signed_header(self) -> tendermint.types.types_pb2.SignedHeader: ...
    @property
    def validator_set(self) -> tendermint.types.validator_pb2.ValidatorSet: ...
    @property
    def trusted_height(self) -> ibc.core.client.v1.client_pb2.Height: ...
    @property
    def trusted_validators(self) -> tendermint.types.validator_pb2.ValidatorSet: ...
    def __init__(self,
        *,
        signed_header : typing.Optional[tendermint.types.types_pb2.SignedHeader] = ...,
        validator_set : typing.Optional[tendermint.types.validator_pb2.ValidatorSet] = ...,
        trusted_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        trusted_validators : typing.Optional[tendermint.types.validator_pb2.ValidatorSet] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"signed_header",b"signed_header",u"trusted_height",b"trusted_height",u"trusted_validators",b"trusted_validators",u"validator_set",b"validator_set"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"signed_header",b"signed_header",u"trusted_height",b"trusted_height",u"trusted_validators",b"trusted_validators",u"validator_set",b"validator_set"]) -> None: ...
global___Header = Header

# Fraction defines the protobuf message type for tmmath.Fraction that only
# supports positive values.
class Fraction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NUMERATOR_FIELD_NUMBER: builtins.int
    DENOMINATOR_FIELD_NUMBER: builtins.int
    numerator: builtins.int = ...
    denominator: builtins.int = ...
    def __init__(self,
        *,
        numerator : builtins.int = ...,
        denominator : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"denominator",b"denominator",u"numerator",b"numerator"]) -> None: ...
global___Fraction = Fraction
