# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='eventprocapi',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tapi.proto\x12\x0c\x65ventprocapi\"#\n\x13ListHandlersRequest\x12\x0c\n\x04hook\x18\x01 \x01(\t\"?\n\x14ListHandlersResponse\x12\'\n\x08handlers\x18\x01 \x03(\x0b\x32\x15.eventprocapi.Handler\"\xe7\x01\n\x07Handler\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04hook\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\x05\x12\x10\n\x08\x63\x61llable\x18\x05 \x01(\t\x12\x0b\n\x03tag\x18\x06 \x03(\t\x12\x19\n\x11notify_on_success\x18\x07 \x01(\t\x12\x19\n\x11notify_on_failure\x18\x08 \x01(\t\x12\x12\n\ncreated_by\x18\t \x01(\t\x12\x12\n\ncreated_at\x18\n \x01(\x03\x12\x12\n\nupdated_by\x18\x0b \x01(\t\x12\x12\n\nupdated_at\x18\x0c \x01(\x03\"\x12\n\x10ListHooksRequest\"6\n\x11ListHooksResponse\x12!\n\x05hooks\x18\x01 \x03(\x0b\x32\x12.eventprocapi.Hook\"\x14\n\x04Hook\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xb1\x01\n\x0cRegistration\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04hook\x18\x02 \x01(\t\x12\x0c\n\x04tags\x18\x03 \x03(\t\x12\x0c\n\x04\x62lob\x18\x04 \x01(\x0c\x12\x19\n\x11notify_on_success\x18\x05 \x01(\t\x12\x19\n\x11notify_on_failure\x18\x06 \x01(\t\x12\x14\n\x0c\x64\x65pendencies\x18\x07 \x01(\t\x12\x0c\n\x04user\x18\x08 \x01(\t\x12\x0f\n\x07\x61pi_key\x18\t \x01(\t\"C\n\x0fRegisterRequest\x12\x30\n\x0cregistration\x18\x01 \x01(\x0b\x32\x1a.eventprocapi.Registration\":\n\x10RegisterResponse\x12&\n\x07handler\x18\x01 \x01(\x0b\x32\x15.eventprocapi.Handler\"\x1f\n\x11\x44\x65registerRequest\x12\n\n\x02id\x18\x01 \x01(\x05\" \n\x12\x44\x65registerResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x32\xe1\x02\n\x16\x45ventProcessingService\x12N\n\tListHooks\x12\x1e.eventprocapi.ListHooksRequest\x1a\x1f.eventprocapi.ListHooksResponse\"\x00\x12W\n\x0cListHandlers\x12!.eventprocapi.ListHandlersRequest\x1a\".eventprocapi.ListHandlersResponse\"\x00\x12K\n\x08Register\x12\x1d.eventprocapi.RegisterRequest\x1a\x1e.eventprocapi.RegisterResponse\"\x00\x12Q\n\nDeregister\x12\x1f.eventprocapi.DeregisterRequest\x1a .eventprocapi.DeregisterResponse\"\x00\x62\x06proto3'
)




_LISTHANDLERSREQUEST = _descriptor.Descriptor(
  name='ListHandlersRequest',
  full_name='eventprocapi.ListHandlersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hook', full_name='eventprocapi.ListHandlersRequest.hook', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=27,
  serialized_end=62,
)


_LISTHANDLERSRESPONSE = _descriptor.Descriptor(
  name='ListHandlersResponse',
  full_name='eventprocapi.ListHandlersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='handlers', full_name='eventprocapi.ListHandlersResponse.handlers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=64,
  serialized_end=127,
)


_HANDLER = _descriptor.Descriptor(
  name='Handler',
  full_name='eventprocapi.Handler',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='eventprocapi.Handler.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hook', full_name='eventprocapi.Handler.hook', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='eventprocapi.Handler.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='eventprocapi.Handler.version', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='callable', full_name='eventprocapi.Handler.callable', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tag', full_name='eventprocapi.Handler.tag', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notify_on_success', full_name='eventprocapi.Handler.notify_on_success', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notify_on_failure', full_name='eventprocapi.Handler.notify_on_failure', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_by', full_name='eventprocapi.Handler.created_by', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='eventprocapi.Handler.created_at', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_by', full_name='eventprocapi.Handler.updated_by', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='eventprocapi.Handler.updated_at', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=130,
  serialized_end=361,
)


_LISTHOOKSREQUEST = _descriptor.Descriptor(
  name='ListHooksRequest',
  full_name='eventprocapi.ListHooksRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=363,
  serialized_end=381,
)


_LISTHOOKSRESPONSE = _descriptor.Descriptor(
  name='ListHooksResponse',
  full_name='eventprocapi.ListHooksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hooks', full_name='eventprocapi.ListHooksResponse.hooks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=383,
  serialized_end=437,
)


_HOOK = _descriptor.Descriptor(
  name='Hook',
  full_name='eventprocapi.Hook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='eventprocapi.Hook.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=439,
  serialized_end=459,
)


_REGISTRATION = _descriptor.Descriptor(
  name='Registration',
  full_name='eventprocapi.Registration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='eventprocapi.Registration.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hook', full_name='eventprocapi.Registration.hook', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='eventprocapi.Registration.tags', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blob', full_name='eventprocapi.Registration.blob', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notify_on_success', full_name='eventprocapi.Registration.notify_on_success', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notify_on_failure', full_name='eventprocapi.Registration.notify_on_failure', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='eventprocapi.Registration.dependencies', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='eventprocapi.Registration.user', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='api_key', full_name='eventprocapi.Registration.api_key', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=462,
  serialized_end=639,
)


_REGISTERREQUEST = _descriptor.Descriptor(
  name='RegisterRequest',
  full_name='eventprocapi.RegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='registration', full_name='eventprocapi.RegisterRequest.registration', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=641,
  serialized_end=708,
)


_REGISTERRESPONSE = _descriptor.Descriptor(
  name='RegisterResponse',
  full_name='eventprocapi.RegisterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='handler', full_name='eventprocapi.RegisterResponse.handler', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=710,
  serialized_end=768,
)


_DEREGISTERREQUEST = _descriptor.Descriptor(
  name='DeregisterRequest',
  full_name='eventprocapi.DeregisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='eventprocapi.DeregisterRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=770,
  serialized_end=801,
)


_DEREGISTERRESPONSE = _descriptor.Descriptor(
  name='DeregisterResponse',
  full_name='eventprocapi.DeregisterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='eventprocapi.DeregisterResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=803,
  serialized_end=835,
)

_LISTHANDLERSRESPONSE.fields_by_name['handlers'].message_type = _HANDLER
_LISTHOOKSRESPONSE.fields_by_name['hooks'].message_type = _HOOK
_REGISTERREQUEST.fields_by_name['registration'].message_type = _REGISTRATION
_REGISTERRESPONSE.fields_by_name['handler'].message_type = _HANDLER
DESCRIPTOR.message_types_by_name['ListHandlersRequest'] = _LISTHANDLERSREQUEST
DESCRIPTOR.message_types_by_name['ListHandlersResponse'] = _LISTHANDLERSRESPONSE
DESCRIPTOR.message_types_by_name['Handler'] = _HANDLER
DESCRIPTOR.message_types_by_name['ListHooksRequest'] = _LISTHOOKSREQUEST
DESCRIPTOR.message_types_by_name['ListHooksResponse'] = _LISTHOOKSRESPONSE
DESCRIPTOR.message_types_by_name['Hook'] = _HOOK
DESCRIPTOR.message_types_by_name['Registration'] = _REGISTRATION
DESCRIPTOR.message_types_by_name['RegisterRequest'] = _REGISTERREQUEST
DESCRIPTOR.message_types_by_name['RegisterResponse'] = _REGISTERRESPONSE
DESCRIPTOR.message_types_by_name['DeregisterRequest'] = _DEREGISTERREQUEST
DESCRIPTOR.message_types_by_name['DeregisterResponse'] = _DEREGISTERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListHandlersRequest = _reflection.GeneratedProtocolMessageType('ListHandlersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTHANDLERSREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:eventprocapi.ListHandlersRequest)
  })
_sym_db.RegisterMessage(ListHandlersRequest)

ListHandlersResponse = _reflection.GeneratedProtocolMessageType('ListHandlersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTHANDLERSRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:eventprocapi.ListHandlersResponse)
  })
_sym_db.RegisterMessage(ListHandlersResponse)

Handler = _reflection.GeneratedProtocolMessageType('Handler', (_message.Message,), {
  'DESCRIPTOR' : _HANDLER,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:eventprocapi.Handler)
  })
_sym_db.RegisterMessage(Handler)

ListHooksRequest = _reflection.GeneratedProtocolMessageType('ListHooksRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTHOOKSREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:eventprocapi.ListHooksRequest)
  })
_sym_db.RegisterMessage(ListHooksRequest)

ListHooksResponse = _reflection.GeneratedProtocolMessageType('ListHooksResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTHOOKSRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:eventprocapi.ListHooksResponse)
  })
_sym_db.RegisterMessage(ListHooksResponse)

Hook = _reflection.GeneratedProtocolMessageType('Hook', (_message.Message,), {
  'DESCRIPTOR' : _HOOK,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:eventprocapi.Hook)
  })
_sym_db.RegisterMessage(Hook)

Registration = _reflection.GeneratedProtocolMessageType('Registration', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRATION,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:eventprocapi.Registration)
  })
_sym_db.RegisterMessage(Registration)

RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:eventprocapi.RegisterRequest)
  })
_sym_db.RegisterMessage(RegisterRequest)

RegisterResponse = _reflection.GeneratedProtocolMessageType('RegisterResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:eventprocapi.RegisterResponse)
  })
_sym_db.RegisterMessage(RegisterResponse)

DeregisterRequest = _reflection.GeneratedProtocolMessageType('DeregisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _DEREGISTERREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:eventprocapi.DeregisterRequest)
  })
_sym_db.RegisterMessage(DeregisterRequest)

DeregisterResponse = _reflection.GeneratedProtocolMessageType('DeregisterResponse', (_message.Message,), {
  'DESCRIPTOR' : _DEREGISTERRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:eventprocapi.DeregisterResponse)
  })
_sym_db.RegisterMessage(DeregisterResponse)



_EVENTPROCESSINGSERVICE = _descriptor.ServiceDescriptor(
  name='EventProcessingService',
  full_name='eventprocapi.EventProcessingService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=838,
  serialized_end=1191,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListHooks',
    full_name='eventprocapi.EventProcessingService.ListHooks',
    index=0,
    containing_service=None,
    input_type=_LISTHOOKSREQUEST,
    output_type=_LISTHOOKSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListHandlers',
    full_name='eventprocapi.EventProcessingService.ListHandlers',
    index=1,
    containing_service=None,
    input_type=_LISTHANDLERSREQUEST,
    output_type=_LISTHANDLERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='eventprocapi.EventProcessingService.Register',
    index=2,
    containing_service=None,
    input_type=_REGISTERREQUEST,
    output_type=_REGISTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Deregister',
    full_name='eventprocapi.EventProcessingService.Deregister',
    index=3,
    containing_service=None,
    input_type=_DEREGISTERREQUEST,
    output_type=_DEREGISTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTPROCESSINGSERVICE)

DESCRIPTOR.services_by_name['EventProcessingService'] = _EVENTPROCESSINGSERVICE

# @@protoc_insertion_point(module_scope)
