# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: caffe2/proto/prof_dag.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='caffe2/proto/prof_dag.proto',
  package='caffe2',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1b\x63\x61\x66\x66\x65\x32/proto/prof_dag.proto\x12\x06\x63\x61\x66\x66\x65\x32\"B\n\x13TwoNumberStatsProto\x12\x0c\n\x04mean\x18\x01 \x01(\x02\x12\x0e\n\x06stddev\x18\x02 \x01(\x02\x12\r\n\x05\x63ount\x18\x03 \x01(\x03\"L\n\x0b\x42lobProfile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\nbytes_used\x18\x03 \x01(\x0b\x32\x1b.caffe2.TwoNumberStatsProto\"\xb0\x01\n\x0cProfDAGProto\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04mean\x18\x02 \x02(\x02\x12\x0e\n\x06stddev\x18\x03 \x02(\x02\x12\x33\n\x0e\x65xecution_time\x18\x04 \x01(\x0b\x32\x1b.caffe2.TwoNumberStatsProto\x12+\n\x0eoutput_profile\x18\x05 \x03(\x0b\x32\x13.caffe2.BlobProfile\x12\x12\n\nextra_info\x18\x07 \x03(\t\"F\n\rProfDAGProtos\x12#\n\x05stats\x18\x01 \x03(\x0b\x32\x14.caffe2.ProfDAGProto\x12\x10\n\x08net_name\x18\x02 \x01(\t')
)




_TWONUMBERSTATSPROTO = _descriptor.Descriptor(
  name='TwoNumberStatsProto',
  full_name='caffe2.TwoNumberStatsProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mean', full_name='caffe2.TwoNumberStatsProto.mean', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stddev', full_name='caffe2.TwoNumberStatsProto.stddev', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='caffe2.TwoNumberStatsProto.count', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=105,
)


_BLOBPROFILE = _descriptor.Descriptor(
  name='BlobProfile',
  full_name='caffe2.BlobProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='caffe2.BlobProfile.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_used', full_name='caffe2.BlobProfile.bytes_used', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=183,
)


_PROFDAGPROTO = _descriptor.Descriptor(
  name='ProfDAGProto',
  full_name='caffe2.ProfDAGProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='caffe2.ProfDAGProto.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean', full_name='caffe2.ProfDAGProto.mean', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stddev', full_name='caffe2.ProfDAGProto.stddev', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execution_time', full_name='caffe2.ProfDAGProto.execution_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_profile', full_name='caffe2.ProfDAGProto.output_profile', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extra_info', full_name='caffe2.ProfDAGProto.extra_info', index=5,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=362,
)


_PROFDAGPROTOS = _descriptor.Descriptor(
  name='ProfDAGProtos',
  full_name='caffe2.ProfDAGProtos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stats', full_name='caffe2.ProfDAGProtos.stats', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='net_name', full_name='caffe2.ProfDAGProtos.net_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=364,
  serialized_end=434,
)

_BLOBPROFILE.fields_by_name['bytes_used'].message_type = _TWONUMBERSTATSPROTO
_PROFDAGPROTO.fields_by_name['execution_time'].message_type = _TWONUMBERSTATSPROTO
_PROFDAGPROTO.fields_by_name['output_profile'].message_type = _BLOBPROFILE
_PROFDAGPROTOS.fields_by_name['stats'].message_type = _PROFDAGPROTO
DESCRIPTOR.message_types_by_name['TwoNumberStatsProto'] = _TWONUMBERSTATSPROTO
DESCRIPTOR.message_types_by_name['BlobProfile'] = _BLOBPROFILE
DESCRIPTOR.message_types_by_name['ProfDAGProto'] = _PROFDAGPROTO
DESCRIPTOR.message_types_by_name['ProfDAGProtos'] = _PROFDAGPROTOS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TwoNumberStatsProto = _reflection.GeneratedProtocolMessageType('TwoNumberStatsProto', (_message.Message,), dict(
  DESCRIPTOR = _TWONUMBERSTATSPROTO,
  __module__ = 'caffe2.proto.prof_dag_pb2'
  # @@protoc_insertion_point(class_scope:caffe2.TwoNumberStatsProto)
  ))
_sym_db.RegisterMessage(TwoNumberStatsProto)

BlobProfile = _reflection.GeneratedProtocolMessageType('BlobProfile', (_message.Message,), dict(
  DESCRIPTOR = _BLOBPROFILE,
  __module__ = 'caffe2.proto.prof_dag_pb2'
  # @@protoc_insertion_point(class_scope:caffe2.BlobProfile)
  ))
_sym_db.RegisterMessage(BlobProfile)

ProfDAGProto = _reflection.GeneratedProtocolMessageType('ProfDAGProto', (_message.Message,), dict(
  DESCRIPTOR = _PROFDAGPROTO,
  __module__ = 'caffe2.proto.prof_dag_pb2'
  # @@protoc_insertion_point(class_scope:caffe2.ProfDAGProto)
  ))
_sym_db.RegisterMessage(ProfDAGProto)

ProfDAGProtos = _reflection.GeneratedProtocolMessageType('ProfDAGProtos', (_message.Message,), dict(
  DESCRIPTOR = _PROFDAGPROTOS,
  __module__ = 'caffe2.proto.prof_dag_pb2'
  # @@protoc_insertion_point(class_scope:caffe2.ProfDAGProtos)
  ))
_sym_db.RegisterMessage(ProfDAGProtos)


# @@protoc_insertion_point(module_scope)
