# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: oracle/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from oracle.v1 import oracle_pb2 as oracle_dot_v1_dot_oracle__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='oracle/v1/genesis.proto',
  package='oracle.v1',
  syntax='proto3',
  serialized_options=b'Z,github.com/bandprotocol/chain/x/oracle/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17oracle/v1/genesis.proto\x12\toracle.v1\x1a\x14gogoproto/gogo.proto\x1a\x16oracle/v1/oracle.proto\"\xa1\x01\n\x0cGenesisState\x12\'\n\x06params\x18\x01 \x01(\x0b\x32\x11.oracle.v1.ParamsB\x04\xc8\xde\x1f\x00\x12\x31\n\x0c\x64\x61ta_sources\x18\x02 \x03(\x0b\x32\x15.oracle.v1.DataSourceB\x04\xc8\xde\x1f\x00\x12\x35\n\x0eoracle_scripts\x18\x03 \x03(\x0b\x32\x17.oracle.v1.OracleScriptB\x04\xc8\xde\x1f\x00\x42.Z,github.com/bandprotocol/chain/x/oracle/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,oracle_dot_v1_dot_oracle__pb2.DESCRIPTOR,])




_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='oracle.v1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='oracle.v1.GenesisState.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_sources', full_name='oracle.v1.GenesisState.data_sources', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='oracle_scripts', full_name='oracle.v1.GenesisState.oracle_scripts', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=246,
)

_GENESISSTATE.fields_by_name['params'].message_type = oracle_dot_v1_dot_oracle__pb2._PARAMS
_GENESISSTATE.fields_by_name['data_sources'].message_type = oracle_dot_v1_dot_oracle__pb2._DATASOURCE
_GENESISSTATE.fields_by_name['oracle_scripts'].message_type = oracle_dot_v1_dot_oracle__pb2._ORACLESCRIPT
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'oracle.v1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:oracle.v1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR._options = None
_GENESISSTATE.fields_by_name['params']._options = None
_GENESISSTATE.fields_by_name['data_sources']._options = None
_GENESISSTATE.fields_by_name['oracle_scripts']._options = None
# @@protoc_insertion_point(module_scope)
