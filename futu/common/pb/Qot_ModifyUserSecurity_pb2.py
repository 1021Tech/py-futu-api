# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Qot_ModifyUserSecurity.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2
import Qot_Common_pb2 as Qot__Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Qot_ModifyUserSecurity.proto',
  package='Qot_ModifyUserSecurity',
  syntax='proto2',
  serialized_pb=_b('\n\x1cQot_ModifyUserSecurity.proto\x12\x16Qot_ModifyUserSecurity\x1a\x0c\x43ommon.proto\x1a\x10Qot_Common.proto\"P\n\x03\x43\x32S\x12\x11\n\tgroupName\x18\x01 \x02(\t\x12\n\n\x02op\x18\x02 \x02(\x05\x12*\n\x0csecurityList\x18\x03 \x03(\x0b\x32\x14.Qot_Common.Security\"\x05\n\x03S2C\"3\n\x07Request\x12(\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x1b.Qot_ModifyUserSecurity.C2S\"l\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12(\n\x03s2c\x18\x04 \x01(\x0b\x32\x1b.Qot_ModifyUserSecurity.S2C*t\n\x14ModifyUserSecurityOp\x12 \n\x1cModifyUserSecurityOp_Unknown\x10\x00\x12\x1c\n\x18ModifyUserSecurityOp_Add\x10\x01\x12\x1c\n\x18ModifyUserSecurityOp_Del\x10\x02\x42\x15\n\x13\x63om.futu.openapi.pb')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,Qot__Common__pb2.DESCRIPTOR,])

_MODIFYUSERSECURITYOP = _descriptor.EnumDescriptor(
  name='ModifyUserSecurityOp',
  full_name='Qot_ModifyUserSecurity.ModifyUserSecurityOp',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ModifyUserSecurityOp_Unknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ModifyUserSecurityOp_Add', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ModifyUserSecurityOp_Del', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=340,
  serialized_end=456,
)
_sym_db.RegisterEnumDescriptor(_MODIFYUSERSECURITYOP)

ModifyUserSecurityOp = enum_type_wrapper.EnumTypeWrapper(_MODIFYUSERSECURITYOP)
ModifyUserSecurityOp_Unknown = 0
ModifyUserSecurityOp_Add = 1
ModifyUserSecurityOp_Del = 2



_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Qot_ModifyUserSecurity.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='groupName', full_name='Qot_ModifyUserSecurity.C2S.groupName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op', full_name='Qot_ModifyUserSecurity.C2S.op', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='securityList', full_name='Qot_ModifyUserSecurity.C2S.securityList', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=168,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Qot_ModifyUserSecurity.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=175,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Qot_ModifyUserSecurity.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Qot_ModifyUserSecurity.Request.c2s', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=228,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Qot_ModifyUserSecurity.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Qot_ModifyUserSecurity.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Qot_ModifyUserSecurity.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Qot_ModifyUserSecurity.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Qot_ModifyUserSecurity.Response.s2c', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=338,
)

_C2S.fields_by_name['securityList'].message_type = Qot__Common__pb2._SECURITY
_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.enum_types_by_name['ModifyUserSecurityOp'] = _MODIFYUSERSECURITYOP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Qot_ModifyUserSecurity_pb2'
  # @@protoc_insertion_point(class_scope:Qot_ModifyUserSecurity.C2S)
  ))
_sym_db.RegisterMessage(C2S)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Qot_ModifyUserSecurity_pb2'
  # @@protoc_insertion_point(class_scope:Qot_ModifyUserSecurity.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Qot_ModifyUserSecurity_pb2'
  # @@protoc_insertion_point(class_scope:Qot_ModifyUserSecurity.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Qot_ModifyUserSecurity_pb2'
  # @@protoc_insertion_point(class_scope:Qot_ModifyUserSecurity.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.futu.openapi.pb'))
# @@protoc_insertion_point(module_scope)