# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/metaprov/modelaapi/services/reciperun/v1/reciperun.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='github.com/metaprov/modelaapi/services/reciperun/v1/reciperun.proto',
  package='github.com.metaprov.modelaapi.services.reciperun.v1',
  syntax='proto3',
  serialized_options=b'Z3github.com/metaprov/modelaapi/services/reciperun/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nCgithub.com/metaprov/modelaapi/services/reciperun/v1/reciperun.proto\x12\x33github.com.metaprov.modelaapi.services.reciperun.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x44github.com/metaprov/modelaapi/pkg/apis/data/v1alpha1/generated.proto\"\xc1\x01\n\x15ListRecipeRunsRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x66\n\x06labels\x18\x03 \x03(\x0b\x32V.github.com.metaprov.modelaapi.services.reciperun.v1.ListRecipeRunsRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"l\n\x16ListRecipeRunsResponse\x12R\n\x05items\x18\x01 \x01(\x0b\x32\x43.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.RecipeRunList\"g\n\x16\x43reateRecipeRunRequest\x12M\n\x04item\x18\x01 \x01(\x0b\x32?.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.RecipeRun\"\x19\n\x17\x43reateRecipeRunResponse\"g\n\x16UpdateRecipeRunRequest\x12M\n\x04item\x18\x01 \x01(\x0b\x32?.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.RecipeRun\"\x19\n\x17UpdateRecipeRunResponse\"6\n\x13GetRecipeRunRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"s\n\x14GetRecipeRunResponse\x12M\n\x04item\x18\x01 \x01(\x0b\x32?.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.RecipeRun\x12\x0c\n\x04yaml\x18\x02 \x01(\t\"9\n\x16\x44\x65leteRecipeRunRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x19\n\x17\x44\x65leteRecipeRunResponse2\xfa\x07\n\x10RecipeRunService\x12\xc1\x01\n\x0eListRecipeRuns\x12J.github.com.metaprov.modelaapi.services.reciperun.v1.ListRecipeRunsRequest\x1aK.github.com.metaprov.modelaapi.services.reciperun.v1.ListRecipeRunsResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/v1/reciperuns\x12\xc7\x01\n\x0f\x43reateRecipeRun\x12K.github.com.metaprov.modelaapi.services.reciperun.v1.CreateRecipeRunRequest\x1aL.github.com.metaprov.modelaapi.services.reciperun.v1.CreateRecipeRunResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/v1/reciperuns:\x01*\x12\xc2\x01\n\x0cGetRecipeRun\x12H.github.com.metaprov.modelaapi.services.reciperun.v1.GetRecipeRunRequest\x1aI.github.com.metaprov.modelaapi.services.reciperun.v1.GetRecipeRunResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/reciperuns/{name}\x12\xe1\x01\n\x0fUpdateRecipeRun\x12K.github.com.metaprov.modelaapi.services.reciperun.v1.UpdateRecipeRunRequest\x1aL.github.com.metaprov.modelaapi.services.reciperun.v1.UpdateRecipeRunResponse\"3\x82\xd3\xe4\x93\x02-\x1a(/v1/reciperuns/{reciperun.metadata.name}:\x01*\x12\xae\x01\n\x0f\x44\x65leteRecipeRun\x12K.github.com.metaprov.modelaapi.services.reciperun.v1.DeleteRecipeRunRequest\x1aL.github.com.metaprov.modelaapi.services.reciperun.v1.DeleteRecipeRunResponse\"\x00\x42\x35Z3github.com/metaprov/modelaapi/services/reciperun/v1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2.DESCRIPTOR,])




_LISTRECIPERUNSREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='github.com.metaprov.modelaapi.services.reciperun.v1.ListRecipeRunsRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='github.com.metaprov.modelaapi.services.reciperun.v1.ListRecipeRunsRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='github.com.metaprov.modelaapi.services.reciperun.v1.ListRecipeRunsRequest.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=418,
)

_LISTRECIPERUNSREQUEST = _descriptor.Descriptor(
  name='ListRecipeRunsRequest',
  full_name='github.com.metaprov.modelaapi.services.reciperun.v1.ListRecipeRunsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.reciperun.v1.ListRecipeRunsRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='github.com.metaprov.modelaapi.services.reciperun.v1.ListRecipeRunsRequest.labels', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LISTRECIPERUNSREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=418,
)


_LISTRECIPERUNSRESPONSE = _descriptor.Descriptor(
  name='ListRecipeRunsResponse',
  full_name='github.com.metaprov.modelaapi.services.reciperun.v1.ListRecipeRunsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='github.com.metaprov.modelaapi.services.reciperun.v1.ListRecipeRunsResponse.items', index=0,
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
  serialized_start=420,
  serialized_end=528,
)


_CREATERECIPERUNREQUEST = _descriptor.Descriptor(
  name='CreateRecipeRunRequest',
  full_name='github.com.metaprov.modelaapi.services.reciperun.v1.CreateRecipeRunRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='github.com.metaprov.modelaapi.services.reciperun.v1.CreateRecipeRunRequest.item', index=0,
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
  serialized_start=530,
  serialized_end=633,
)


_CREATERECIPERUNRESPONSE = _descriptor.Descriptor(
  name='CreateRecipeRunResponse',
  full_name='github.com.metaprov.modelaapi.services.reciperun.v1.CreateRecipeRunResponse',
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
  serialized_start=635,
  serialized_end=660,
)


_UPDATERECIPERUNREQUEST = _descriptor.Descriptor(
  name='UpdateRecipeRunRequest',
  full_name='github.com.metaprov.modelaapi.services.reciperun.v1.UpdateRecipeRunRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='github.com.metaprov.modelaapi.services.reciperun.v1.UpdateRecipeRunRequest.item', index=0,
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
  serialized_start=662,
  serialized_end=765,
)


_UPDATERECIPERUNRESPONSE = _descriptor.Descriptor(
  name='UpdateRecipeRunResponse',
  full_name='github.com.metaprov.modelaapi.services.reciperun.v1.UpdateRecipeRunResponse',
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
  serialized_start=767,
  serialized_end=792,
)


_GETRECIPERUNREQUEST = _descriptor.Descriptor(
  name='GetRecipeRunRequest',
  full_name='github.com.metaprov.modelaapi.services.reciperun.v1.GetRecipeRunRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.reciperun.v1.GetRecipeRunRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='github.com.metaprov.modelaapi.services.reciperun.v1.GetRecipeRunRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=794,
  serialized_end=848,
)


_GETRECIPERUNRESPONSE = _descriptor.Descriptor(
  name='GetRecipeRunResponse',
  full_name='github.com.metaprov.modelaapi.services.reciperun.v1.GetRecipeRunResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='github.com.metaprov.modelaapi.services.reciperun.v1.GetRecipeRunResponse.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yaml', full_name='github.com.metaprov.modelaapi.services.reciperun.v1.GetRecipeRunResponse.yaml', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=850,
  serialized_end=965,
)


_DELETERECIPERUNREQUEST = _descriptor.Descriptor(
  name='DeleteRecipeRunRequest',
  full_name='github.com.metaprov.modelaapi.services.reciperun.v1.DeleteRecipeRunRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='github.com.metaprov.modelaapi.services.reciperun.v1.DeleteRecipeRunRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='github.com.metaprov.modelaapi.services.reciperun.v1.DeleteRecipeRunRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=967,
  serialized_end=1024,
)


_DELETERECIPERUNRESPONSE = _descriptor.Descriptor(
  name='DeleteRecipeRunResponse',
  full_name='github.com.metaprov.modelaapi.services.reciperun.v1.DeleteRecipeRunResponse',
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
  serialized_start=1026,
  serialized_end=1051,
)

_LISTRECIPERUNSREQUEST_LABELSENTRY.containing_type = _LISTRECIPERUNSREQUEST
_LISTRECIPERUNSREQUEST.fields_by_name['labels'].message_type = _LISTRECIPERUNSREQUEST_LABELSENTRY
_LISTRECIPERUNSRESPONSE.fields_by_name['items'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2._RECIPERUNLIST
_CREATERECIPERUNREQUEST.fields_by_name['item'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2._RECIPERUN
_UPDATERECIPERUNREQUEST.fields_by_name['item'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2._RECIPERUN
_GETRECIPERUNRESPONSE.fields_by_name['item'].message_type = github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2._RECIPERUN
DESCRIPTOR.message_types_by_name['ListRecipeRunsRequest'] = _LISTRECIPERUNSREQUEST
DESCRIPTOR.message_types_by_name['ListRecipeRunsResponse'] = _LISTRECIPERUNSRESPONSE
DESCRIPTOR.message_types_by_name['CreateRecipeRunRequest'] = _CREATERECIPERUNREQUEST
DESCRIPTOR.message_types_by_name['CreateRecipeRunResponse'] = _CREATERECIPERUNRESPONSE
DESCRIPTOR.message_types_by_name['UpdateRecipeRunRequest'] = _UPDATERECIPERUNREQUEST
DESCRIPTOR.message_types_by_name['UpdateRecipeRunResponse'] = _UPDATERECIPERUNRESPONSE
DESCRIPTOR.message_types_by_name['GetRecipeRunRequest'] = _GETRECIPERUNREQUEST
DESCRIPTOR.message_types_by_name['GetRecipeRunResponse'] = _GETRECIPERUNRESPONSE
DESCRIPTOR.message_types_by_name['DeleteRecipeRunRequest'] = _DELETERECIPERUNREQUEST
DESCRIPTOR.message_types_by_name['DeleteRecipeRunResponse'] = _DELETERECIPERUNRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListRecipeRunsRequest = _reflection.GeneratedProtocolMessageType('ListRecipeRunsRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTRECIPERUNSREQUEST_LABELSENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.reciperun.v1.reciperun_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.reciperun.v1.ListRecipeRunsRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTRECIPERUNSREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.reciperun.v1.reciperun_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.reciperun.v1.ListRecipeRunsRequest)
  })
_sym_db.RegisterMessage(ListRecipeRunsRequest)
_sym_db.RegisterMessage(ListRecipeRunsRequest.LabelsEntry)

ListRecipeRunsResponse = _reflection.GeneratedProtocolMessageType('ListRecipeRunsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRECIPERUNSRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.reciperun.v1.reciperun_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.reciperun.v1.ListRecipeRunsResponse)
  })
_sym_db.RegisterMessage(ListRecipeRunsResponse)

CreateRecipeRunRequest = _reflection.GeneratedProtocolMessageType('CreateRecipeRunRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATERECIPERUNREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.reciperun.v1.reciperun_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.reciperun.v1.CreateRecipeRunRequest)
  })
_sym_db.RegisterMessage(CreateRecipeRunRequest)

CreateRecipeRunResponse = _reflection.GeneratedProtocolMessageType('CreateRecipeRunResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATERECIPERUNRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.reciperun.v1.reciperun_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.reciperun.v1.CreateRecipeRunResponse)
  })
_sym_db.RegisterMessage(CreateRecipeRunResponse)

UpdateRecipeRunRequest = _reflection.GeneratedProtocolMessageType('UpdateRecipeRunRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERECIPERUNREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.reciperun.v1.reciperun_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.reciperun.v1.UpdateRecipeRunRequest)
  })
_sym_db.RegisterMessage(UpdateRecipeRunRequest)

UpdateRecipeRunResponse = _reflection.GeneratedProtocolMessageType('UpdateRecipeRunResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERECIPERUNRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.reciperun.v1.reciperun_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.reciperun.v1.UpdateRecipeRunResponse)
  })
_sym_db.RegisterMessage(UpdateRecipeRunResponse)

GetRecipeRunRequest = _reflection.GeneratedProtocolMessageType('GetRecipeRunRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETRECIPERUNREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.reciperun.v1.reciperun_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.reciperun.v1.GetRecipeRunRequest)
  })
_sym_db.RegisterMessage(GetRecipeRunRequest)

GetRecipeRunResponse = _reflection.GeneratedProtocolMessageType('GetRecipeRunResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRECIPERUNRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.reciperun.v1.reciperun_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.reciperun.v1.GetRecipeRunResponse)
  })
_sym_db.RegisterMessage(GetRecipeRunResponse)

DeleteRecipeRunRequest = _reflection.GeneratedProtocolMessageType('DeleteRecipeRunRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETERECIPERUNREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.reciperun.v1.reciperun_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.reciperun.v1.DeleteRecipeRunRequest)
  })
_sym_db.RegisterMessage(DeleteRecipeRunRequest)

DeleteRecipeRunResponse = _reflection.GeneratedProtocolMessageType('DeleteRecipeRunResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERECIPERUNRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.reciperun.v1.reciperun_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.reciperun.v1.DeleteRecipeRunResponse)
  })
_sym_db.RegisterMessage(DeleteRecipeRunResponse)


DESCRIPTOR._options = None
_LISTRECIPERUNSREQUEST_LABELSENTRY._options = None

_RECIPERUNSERVICE = _descriptor.ServiceDescriptor(
  name='RecipeRunService',
  full_name='github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1054,
  serialized_end=2072,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListRecipeRuns',
    full_name='github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService.ListRecipeRuns',
    index=0,
    containing_service=None,
    input_type=_LISTRECIPERUNSREQUEST,
    output_type=_LISTRECIPERUNSRESPONSE,
    serialized_options=b'\202\323\344\223\002\020\022\016/v1/reciperuns',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateRecipeRun',
    full_name='github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService.CreateRecipeRun',
    index=1,
    containing_service=None,
    input_type=_CREATERECIPERUNREQUEST,
    output_type=_CREATERECIPERUNRESPONSE,
    serialized_options=b'\202\323\344\223\002\023\"\016/v1/reciperuns:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetRecipeRun',
    full_name='github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService.GetRecipeRun',
    index=2,
    containing_service=None,
    input_type=_GETRECIPERUNREQUEST,
    output_type=_GETRECIPERUNRESPONSE,
    serialized_options=b'\202\323\344\223\002\027\022\025/v1/reciperuns/{name}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateRecipeRun',
    full_name='github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService.UpdateRecipeRun',
    index=3,
    containing_service=None,
    input_type=_UPDATERECIPERUNREQUEST,
    output_type=_UPDATERECIPERUNRESPONSE,
    serialized_options=b'\202\323\344\223\002-\032(/v1/reciperuns/{reciperun.metadata.name}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteRecipeRun',
    full_name='github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService.DeleteRecipeRun',
    index=4,
    containing_service=None,
    input_type=_DELETERECIPERUNREQUEST,
    output_type=_DELETERECIPERUNRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RECIPERUNSERVICE)

DESCRIPTOR.services_by_name['RecipeRunService'] = _RECIPERUNSERVICE

# @@protoc_insertion_point(module_scope)
