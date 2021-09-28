# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/cfg.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import primitives_pb2 as protos_dot_primitives__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/cfg.proto',
  package='angr.protos',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10protos/cfg.proto\x12\x0b\x61ngr.protos\x1a\x17protos/primitives.proto\"H\n\x07\x43\x46GNode\x12\n\n\x02\x65\x61\x18\x01 \x01(\x04\x12\x0c\n\x04size\x18\x02 \x01(\r\x12\x10\n\x08\x62lock_id\x18\x03 \x03(\x03\x12\x11\n\treturning\x18\x04 \x01(\x08\"\x89\x01\n\x03\x43\x46G\x12\r\n\x05ident\x18\x01 \x01(\t\x12#\n\x05nodes\x18\x02 \x03(\x0b\x32\x14.angr.protos.CFGNode\x12 \n\x05\x65\x64ges\x18\x03 \x03(\x0b\x32\x11.angr.protos.Edge\x12,\n\x0bmemory_data\x18\x04 \x03(\x0b\x32\x17.angr.protos.MemoryData\"\xae\x02\n\nMemoryData\x12\n\n\x02\x65\x61\x18\x01 \x01(\x04\x12\x0c\n\x04size\x18\x02 \x01(\r\x12\x34\n\x04type\x18\x03 \x01(\x0e\x32&.angr.protos.MemoryData.MemoryDataType\"\xcf\x01\n\x0eMemoryDataType\x12\x13\n\x0fUnknownDataType\x10\x00\x12\x0f\n\x0bUnspecified\x10\x01\x12\x0b\n\x07Integer\x10\x02\x12\x10\n\x0cPointerArray\x10\x03\x12\n\n\x06String\x10\x04\x12\x11\n\rUnicodeString\x10\x05\x12\x13\n\x0fSegmentBoundary\x10\x06\x12\x11\n\rCodeReference\x10\x07\x12\x0f\n\x0bGOTPLTEntry\x10\x08\x12\r\n\tELFHeader\x10\t\x12\x11\n\rFloatingPoint\x10\nb\x06proto3'
  ,
  dependencies=[protos_dot_primitives__pb2.DESCRIPTOR,])



_MEMORYDATA_MEMORYDATATYPE = _descriptor.EnumDescriptor(
  name='MemoryDataType',
  full_name='angr.protos.MemoryData.MemoryDataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UnknownDataType', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unspecified', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Integer', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PointerArray', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='String', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UnicodeString', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SegmentBoundary', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CodeReference', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOTPLTEntry', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ELFHeader', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FloatingPoint', index=10, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=368,
  serialized_end=575,
)
_sym_db.RegisterEnumDescriptor(_MEMORYDATA_MEMORYDATATYPE)


_CFGNODE = _descriptor.Descriptor(
  name='CFGNode',
  full_name='angr.protos.CFGNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ea', full_name='angr.protos.CFGNode.ea', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='angr.protos.CFGNode.size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_id', full_name='angr.protos.CFGNode.block_id', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='returning', full_name='angr.protos.CFGNode.returning', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  serialized_start=58,
  serialized_end=130,
)


_CFG = _descriptor.Descriptor(
  name='CFG',
  full_name='angr.protos.CFG',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ident', full_name='angr.protos.CFG.ident', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='angr.protos.CFG.nodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edges', full_name='angr.protos.CFG.edges', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory_data', full_name='angr.protos.CFG.memory_data', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=133,
  serialized_end=270,
)


_MEMORYDATA = _descriptor.Descriptor(
  name='MemoryData',
  full_name='angr.protos.MemoryData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ea', full_name='angr.protos.MemoryData.ea', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='angr.protos.MemoryData.size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='angr.protos.MemoryData.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MEMORYDATA_MEMORYDATATYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=575,
)

_CFG.fields_by_name['nodes'].message_type = _CFGNODE
_CFG.fields_by_name['edges'].message_type = protos_dot_primitives__pb2._EDGE
_CFG.fields_by_name['memory_data'].message_type = _MEMORYDATA
_MEMORYDATA.fields_by_name['type'].enum_type = _MEMORYDATA_MEMORYDATATYPE
_MEMORYDATA_MEMORYDATATYPE.containing_type = _MEMORYDATA
DESCRIPTOR.message_types_by_name['CFGNode'] = _CFGNODE
DESCRIPTOR.message_types_by_name['CFG'] = _CFG
DESCRIPTOR.message_types_by_name['MemoryData'] = _MEMORYDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CFGNode = _reflection.GeneratedProtocolMessageType('CFGNode', (_message.Message,), {
  'DESCRIPTOR' : _CFGNODE,
  '__module__' : 'protos.cfg_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.CFGNode)
  })
_sym_db.RegisterMessage(CFGNode)

CFG = _reflection.GeneratedProtocolMessageType('CFG', (_message.Message,), {
  'DESCRIPTOR' : _CFG,
  '__module__' : 'protos.cfg_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.CFG)
  })
_sym_db.RegisterMessage(CFG)

MemoryData = _reflection.GeneratedProtocolMessageType('MemoryData', (_message.Message,), {
  'DESCRIPTOR' : _MEMORYDATA,
  '__module__' : 'protos.cfg_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.MemoryData)
  })
_sym_db.RegisterMessage(MemoryData)


# @@protoc_insertion_point(module_scope)
