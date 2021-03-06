# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rfid.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rfid.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\nrfid.proto\"R\n\x08RFID_MSG\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nname_login\x18\x02 \x01(\t\x12\x13\n\x0bname_logout\x18\x03 \x01(\t\x12\x11\n\tuser_list\x18\x04 \x01(\t\" \n\rRFID_RESPONSE\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32:\n\x0cRFID_SERVICE\x12*\n\x0bRFID_Change\x12\t.RFID_MSG\x1a\x0e.RFID_RESPONSE\"\x00\x62\x06proto3')
)




_RFID_MSG = _descriptor.Descriptor(
  name='RFID_MSG',
  full_name='RFID_MSG',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='RFID_MSG.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name_login', full_name='RFID_MSG.name_login', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name_logout', full_name='RFID_MSG.name_logout', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_list', full_name='RFID_MSG.user_list', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=96,
)


_RFID_RESPONSE = _descriptor.Descriptor(
  name='RFID_RESPONSE',
  full_name='RFID_RESPONSE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='RFID_RESPONSE.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=130,
)

DESCRIPTOR.message_types_by_name['RFID_MSG'] = _RFID_MSG
DESCRIPTOR.message_types_by_name['RFID_RESPONSE'] = _RFID_RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RFID_MSG = _reflection.GeneratedProtocolMessageType('RFID_MSG', (_message.Message,), dict(
  DESCRIPTOR = _RFID_MSG,
  __module__ = 'rfid_pb2'
  # @@protoc_insertion_point(class_scope:RFID_MSG)
  ))
_sym_db.RegisterMessage(RFID_MSG)

RFID_RESPONSE = _reflection.GeneratedProtocolMessageType('RFID_RESPONSE', (_message.Message,), dict(
  DESCRIPTOR = _RFID_RESPONSE,
  __module__ = 'rfid_pb2'
  # @@protoc_insertion_point(class_scope:RFID_RESPONSE)
  ))
_sym_db.RegisterMessage(RFID_RESPONSE)



_RFID_SERVICE = _descriptor.ServiceDescriptor(
  name='RFID_SERVICE',
  full_name='RFID_SERVICE',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=132,
  serialized_end=190,
  methods=[
  _descriptor.MethodDescriptor(
    name='RFID_Change',
    full_name='RFID_SERVICE.RFID_Change',
    index=0,
    containing_service=None,
    input_type=_RFID_MSG,
    output_type=_RFID_RESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RFID_SERVICE)

DESCRIPTOR.services_by_name['RFID_SERVICE'] = _RFID_SERVICE

# @@protoc_insertion_point(module_scope)
