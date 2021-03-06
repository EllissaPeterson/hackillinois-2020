# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Messages.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Messages.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0eMessages.proto\"/\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x02\x12\x11\n\tlongitude\x18\x02 \x01(\x02\"1\n\x05\x44\x61te2\x12\r\n\x05month\x18\x01 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x02 \x01(\x05\x12\x0c\n\x04year\x18\x03 \x01(\x05\"\x88\x01\n\x03Row\x12\x1b\n\x08location\x18\x01 \x01(\x0b\x32\t.Location\x12\x14\n\x04\x64\x61te\x18\x02 \x01(\x0b\x32\x06.Date2\x12\x17\n\x0f\x63onfirmed_cases\x18\x03 \x01(\x05\x12\x18\n\x10\x63onfirmed_deaths\x18\x04 \x01(\x05\x12\x1b\n\x13\x63onfirmed_recovered\x18\x05 \x01(\x05\"\x1a\n\x04\x44ump\x12\x12\n\x04rows\x18\x01 \x03(\x0b\x32\x04.Row\"\x1c\n\x0cUpdateStatus\x12\x0c\n\x04pull\x18\x01 \x01(\x08\x32M\n\tMessenger\x12\x1a\n\x07GetDump\x12\x06.Date2\x1a\x05.Dump\"\x00\x12$\n\tHasUpdate\x12\x06.Date2\x1a\r.UpdateStatus\"\x00\x62\x06proto3'
)




_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Location.latitude', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Location.longitude', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=65,
)


_DATE2 = _descriptor.Descriptor(
  name='Date2',
  full_name='Date2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='month', full_name='Date2.month', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day', full_name='Date2.day', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='Date2.year', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=116,
)


_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='Row.location', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='Row.date', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirmed_cases', full_name='Row.confirmed_cases', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirmed_deaths', full_name='Row.confirmed_deaths', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirmed_recovered', full_name='Row.confirmed_recovered', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=255,
)


_DUMP = _descriptor.Descriptor(
  name='Dump',
  full_name='Dump',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='Dump.rows', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=283,
)


_UPDATESTATUS = _descriptor.Descriptor(
  name='UpdateStatus',
  full_name='UpdateStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pull', full_name='UpdateStatus.pull', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=285,
  serialized_end=313,
)

_ROW.fields_by_name['location'].message_type = _LOCATION
_ROW.fields_by_name['date'].message_type = _DATE2
_DUMP.fields_by_name['rows'].message_type = _ROW
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['Date2'] = _DATE2
DESCRIPTOR.message_types_by_name['Row'] = _ROW
DESCRIPTOR.message_types_by_name['Dump'] = _DUMP
DESCRIPTOR.message_types_by_name['UpdateStatus'] = _UPDATESTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'Messages_pb2'
  # @@protoc_insertion_point(class_scope:Location)
  })
_sym_db.RegisterMessage(Location)

Date2 = _reflection.GeneratedProtocolMessageType('Date2', (_message.Message,), {
  'DESCRIPTOR' : _DATE2,
  '__module__' : 'Messages_pb2'
  # @@protoc_insertion_point(class_scope:Date2)
  })
_sym_db.RegisterMessage(Date2)

Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), {
  'DESCRIPTOR' : _ROW,
  '__module__' : 'Messages_pb2'
  # @@protoc_insertion_point(class_scope:Row)
  })
_sym_db.RegisterMessage(Row)

Dump = _reflection.GeneratedProtocolMessageType('Dump', (_message.Message,), {
  'DESCRIPTOR' : _DUMP,
  '__module__' : 'Messages_pb2'
  # @@protoc_insertion_point(class_scope:Dump)
  })
_sym_db.RegisterMessage(Dump)

UpdateStatus = _reflection.GeneratedProtocolMessageType('UpdateStatus', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESTATUS,
  '__module__' : 'Messages_pb2'
  # @@protoc_insertion_point(class_scope:UpdateStatus)
  })
_sym_db.RegisterMessage(UpdateStatus)



_MESSENGER = _descriptor.ServiceDescriptor(
  name='Messenger',
  full_name='Messenger',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=315,
  serialized_end=392,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetDump',
    full_name='Messenger.GetDump',
    index=0,
    containing_service=None,
    input_type=_DATE2,
    output_type=_DUMP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='HasUpdate',
    full_name='Messenger.HasUpdate',
    index=1,
    containing_service=None,
    input_type=_DATE2,
    output_type=_UPDATESTATUS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MESSENGER)

DESCRIPTOR.services_by_name['Messenger'] = _MESSENGER

# @@protoc_insertion_point(module_scope)
