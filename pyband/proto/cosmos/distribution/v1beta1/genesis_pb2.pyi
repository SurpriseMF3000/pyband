"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.base.v1beta1.coin_pb2
import cosmos.distribution.v1beta1.distribution_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class DelegatorWithdrawInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DELEGATOR_ADDRESS_FIELD_NUMBER: builtins.int
    WITHDRAW_ADDRESS_FIELD_NUMBER: builtins.int
    delegator_address: typing.Text = ...
    withdraw_address: typing.Text = ...

    def __init__(self,
        *,
        delegator_address : typing.Text = ...,
        withdraw_address : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"delegator_address",b"delegator_address",u"withdraw_address",b"withdraw_address"]) -> None: ...
global___DelegatorWithdrawInfo = DelegatorWithdrawInfo

class ValidatorOutstandingRewardsRecord(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    OUTSTANDING_REWARDS_FIELD_NUMBER: builtins.int
    validator_address: typing.Text = ...

    @property
    def outstanding_rewards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.DecCoin]: ...

    def __init__(self,
        *,
        validator_address : typing.Text = ...,
        outstanding_rewards : typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.DecCoin]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"outstanding_rewards",b"outstanding_rewards",u"validator_address",b"validator_address"]) -> None: ...
global___ValidatorOutstandingRewardsRecord = ValidatorOutstandingRewardsRecord

class ValidatorAccumulatedCommissionRecord(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    ACCUMULATED_FIELD_NUMBER: builtins.int
    validator_address: typing.Text = ...

    @property
    def accumulated(self) -> cosmos.distribution.v1beta1.distribution_pb2.ValidatorAccumulatedCommission: ...

    def __init__(self,
        *,
        validator_address : typing.Text = ...,
        accumulated : typing.Optional[cosmos.distribution.v1beta1.distribution_pb2.ValidatorAccumulatedCommission] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"accumulated",b"accumulated"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"accumulated",b"accumulated",u"validator_address",b"validator_address"]) -> None: ...
global___ValidatorAccumulatedCommissionRecord = ValidatorAccumulatedCommissionRecord

class ValidatorHistoricalRewardsRecord(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    PERIOD_FIELD_NUMBER: builtins.int
    REWARDS_FIELD_NUMBER: builtins.int
    validator_address: typing.Text = ...
    period: builtins.int = ...

    @property
    def rewards(self) -> cosmos.distribution.v1beta1.distribution_pb2.ValidatorHistoricalRewards: ...

    def __init__(self,
        *,
        validator_address : typing.Text = ...,
        period : builtins.int = ...,
        rewards : typing.Optional[cosmos.distribution.v1beta1.distribution_pb2.ValidatorHistoricalRewards] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"rewards",b"rewards"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"period",b"period",u"rewards",b"rewards",u"validator_address",b"validator_address"]) -> None: ...
global___ValidatorHistoricalRewardsRecord = ValidatorHistoricalRewardsRecord

class ValidatorCurrentRewardsRecord(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    REWARDS_FIELD_NUMBER: builtins.int
    validator_address: typing.Text = ...

    @property
    def rewards(self) -> cosmos.distribution.v1beta1.distribution_pb2.ValidatorCurrentRewards: ...

    def __init__(self,
        *,
        validator_address : typing.Text = ...,
        rewards : typing.Optional[cosmos.distribution.v1beta1.distribution_pb2.ValidatorCurrentRewards] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"rewards",b"rewards"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"rewards",b"rewards",u"validator_address",b"validator_address"]) -> None: ...
global___ValidatorCurrentRewardsRecord = ValidatorCurrentRewardsRecord

class DelegatorStartingInfoRecord(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DELEGATOR_ADDRESS_FIELD_NUMBER: builtins.int
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    STARTING_INFO_FIELD_NUMBER: builtins.int
    delegator_address: typing.Text = ...
    validator_address: typing.Text = ...

    @property
    def starting_info(self) -> cosmos.distribution.v1beta1.distribution_pb2.DelegatorStartingInfo: ...

    def __init__(self,
        *,
        delegator_address : typing.Text = ...,
        validator_address : typing.Text = ...,
        starting_info : typing.Optional[cosmos.distribution.v1beta1.distribution_pb2.DelegatorStartingInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"starting_info",b"starting_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"delegator_address",b"delegator_address",u"starting_info",b"starting_info",u"validator_address",b"validator_address"]) -> None: ...
global___DelegatorStartingInfoRecord = DelegatorStartingInfoRecord

class ValidatorSlashEventRecord(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    PERIOD_FIELD_NUMBER: builtins.int
    VALIDATOR_SLASH_EVENT_FIELD_NUMBER: builtins.int
    validator_address: typing.Text = ...
    height: builtins.int = ...
    period: builtins.int = ...

    @property
    def validator_slash_event(self) -> cosmos.distribution.v1beta1.distribution_pb2.ValidatorSlashEvent: ...

    def __init__(self,
        *,
        validator_address : typing.Text = ...,
        height : builtins.int = ...,
        period : builtins.int = ...,
        validator_slash_event : typing.Optional[cosmos.distribution.v1beta1.distribution_pb2.ValidatorSlashEvent] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"validator_slash_event",b"validator_slash_event"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"height",b"height",u"period",b"period",u"validator_address",b"validator_address",u"validator_slash_event",b"validator_slash_event"]) -> None: ...
global___ValidatorSlashEventRecord = ValidatorSlashEventRecord

class GenesisState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARAMS_FIELD_NUMBER: builtins.int
    FEE_POOL_FIELD_NUMBER: builtins.int
    DELEGATOR_WITHDRAW_INFOS_FIELD_NUMBER: builtins.int
    PREVIOUS_PROPOSER_FIELD_NUMBER: builtins.int
    OUTSTANDING_REWARDS_FIELD_NUMBER: builtins.int
    VALIDATOR_ACCUMULATED_COMMISSIONS_FIELD_NUMBER: builtins.int
    VALIDATOR_HISTORICAL_REWARDS_FIELD_NUMBER: builtins.int
    VALIDATOR_CURRENT_REWARDS_FIELD_NUMBER: builtins.int
    DELEGATOR_STARTING_INFOS_FIELD_NUMBER: builtins.int
    VALIDATOR_SLASH_EVENTS_FIELD_NUMBER: builtins.int
    previous_proposer: typing.Text = ...

    @property
    def params(self) -> cosmos.distribution.v1beta1.distribution_pb2.Params: ...

    @property
    def fee_pool(self) -> cosmos.distribution.v1beta1.distribution_pb2.FeePool: ...

    @property
    def delegator_withdraw_infos(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DelegatorWithdrawInfo]: ...

    @property
    def outstanding_rewards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ValidatorOutstandingRewardsRecord]: ...

    @property
    def validator_accumulated_commissions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ValidatorAccumulatedCommissionRecord]: ...

    @property
    def validator_historical_rewards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ValidatorHistoricalRewardsRecord]: ...

    @property
    def validator_current_rewards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ValidatorCurrentRewardsRecord]: ...

    @property
    def delegator_starting_infos(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DelegatorStartingInfoRecord]: ...

    @property
    def validator_slash_events(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ValidatorSlashEventRecord]: ...

    def __init__(self,
        *,
        params : typing.Optional[cosmos.distribution.v1beta1.distribution_pb2.Params] = ...,
        fee_pool : typing.Optional[cosmos.distribution.v1beta1.distribution_pb2.FeePool] = ...,
        delegator_withdraw_infos : typing.Optional[typing.Iterable[global___DelegatorWithdrawInfo]] = ...,
        previous_proposer : typing.Text = ...,
        outstanding_rewards : typing.Optional[typing.Iterable[global___ValidatorOutstandingRewardsRecord]] = ...,
        validator_accumulated_commissions : typing.Optional[typing.Iterable[global___ValidatorAccumulatedCommissionRecord]] = ...,
        validator_historical_rewards : typing.Optional[typing.Iterable[global___ValidatorHistoricalRewardsRecord]] = ...,
        validator_current_rewards : typing.Optional[typing.Iterable[global___ValidatorCurrentRewardsRecord]] = ...,
        delegator_starting_infos : typing.Optional[typing.Iterable[global___DelegatorStartingInfoRecord]] = ...,
        validator_slash_events : typing.Optional[typing.Iterable[global___ValidatorSlashEventRecord]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"fee_pool",b"fee_pool",u"params",b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"delegator_starting_infos",b"delegator_starting_infos",u"delegator_withdraw_infos",b"delegator_withdraw_infos",u"fee_pool",b"fee_pool",u"outstanding_rewards",b"outstanding_rewards",u"params",b"params",u"previous_proposer",b"previous_proposer",u"validator_accumulated_commissions",b"validator_accumulated_commissions",u"validator_current_rewards",b"validator_current_rewards",u"validator_historical_rewards",b"validator_historical_rewards",u"validator_slash_events",b"validator_slash_events"]) -> None: ...
global___GenesisState = GenesisState