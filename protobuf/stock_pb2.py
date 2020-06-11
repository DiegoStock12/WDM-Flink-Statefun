# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stock.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import general_pb2 as general__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stock.proto',
  package='stock',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0bstock.proto\x12\x05stock\x1a\rgeneral.proto\"4\n\x08ItemData\x12\n\n\x02id\x18\x01 \x01(\x04\x12\r\n\x05price\x18\x02 \x01(\x03\x12\r\n\x05stock\x18\x03 \x01(\x03\"\x14\n\x05\x43ount\x12\x0b\n\x03num\x18\x01 \x01(\x04\"F\n\x11\x43reateItemRequest\x12\r\n\x05price\x18\x01 \x01(\x03\x12\"\n\x0crequest_info\x18\x02 \x01(\x0b\x32\x0c.RequestInfo\"c\n\x10\x43reateItemWithId\x12\n\n\x02id\x18\x01 \x01(\x04\x12\r\n\x05price\x18\x02 \x01(\x03\x12\"\n\x0crequest_info\x18\x03 \x01(\x0b\x32\x0c.RequestInfo\x12\x10\n\x08internal\x18\x04 \x01(\x08\"\xab\x03\n\x0cStockRequest\x12\"\n\x0crequest_info\x18\x01 \x01(\x0b\x32\x0c.RequestInfo\x12\x38\n\tfind_item\x18\x02 \x01(\x0b\x32#.stock.StockRequest.FindItemRequestH\x00\x12\x46\n\x0esubtract_stock\x18\x03 \x01(\x0b\x32,.stock.StockRequest.SubtractItemStockRequestH\x00\x12<\n\tadd_stock\x18\x04 \x01(\x0b\x32\'.stock.StockRequest.AddItemStockRequestH\x00\x12\x10\n\x08internal\x18\x06 \x01(\x08\x12\x10\n\x08order_id\x18\x07 \x01(\x03\x1a\x1d\n\x0f\x46indItemRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x1a\x36\n\x18SubtractItemStockRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x1a\x31\n\x13\x41\x64\x64ItemStockRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x42\t\n\x07message\"T\n\rStockResponse\x12\"\n\x0crequest_info\x18\x01 \x01(\x0b\x32\x0c.RequestInfo\x12\x0f\n\x07item_id\x18\x02 \x01(\x04\x12\x0e\n\x06result\x18\x03 \x01(\tb\x06proto3'
  ,
  dependencies=[general__pb2.DESCRIPTOR,])




_ITEMDATA = _descriptor.Descriptor(
  name='ItemData',
  full_name='stock.ItemData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='stock.ItemData.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='stock.ItemData.price', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stock', full_name='stock.ItemData.stock', index=2,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=89,
)


_COUNT = _descriptor.Descriptor(
  name='Count',
  full_name='stock.Count',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='stock.Count.num', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=91,
  serialized_end=111,
)


_CREATEITEMREQUEST = _descriptor.Descriptor(
  name='CreateItemRequest',
  full_name='stock.CreateItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='stock.CreateItemRequest.price', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_info', full_name='stock.CreateItemRequest.request_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=183,
)


_CREATEITEMWITHID = _descriptor.Descriptor(
  name='CreateItemWithId',
  full_name='stock.CreateItemWithId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='stock.CreateItemWithId.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='stock.CreateItemWithId.price', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_info', full_name='stock.CreateItemWithId.request_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal', full_name='stock.CreateItemWithId.internal', index=3,
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
  serialized_start=185,
  serialized_end=284,
)


_STOCKREQUEST_FINDITEMREQUEST = _descriptor.Descriptor(
  name='FindItemRequest',
  full_name='stock.StockRequest.FindItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='stock.StockRequest.FindItemRequest.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=567,
  serialized_end=596,
)

_STOCKREQUEST_SUBTRACTITEMSTOCKREQUEST = _descriptor.Descriptor(
  name='SubtractItemStockRequest',
  full_name='stock.StockRequest.SubtractItemStockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='stock.StockRequest.SubtractItemStockRequest.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='stock.StockRequest.SubtractItemStockRequest.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=598,
  serialized_end=652,
)

_STOCKREQUEST_ADDITEMSTOCKREQUEST = _descriptor.Descriptor(
  name='AddItemStockRequest',
  full_name='stock.StockRequest.AddItemStockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='stock.StockRequest.AddItemStockRequest.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='stock.StockRequest.AddItemStockRequest.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=654,
  serialized_end=703,
)

_STOCKREQUEST = _descriptor.Descriptor(
  name='StockRequest',
  full_name='stock.StockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_info', full_name='stock.StockRequest.request_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='find_item', full_name='stock.StockRequest.find_item', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subtract_stock', full_name='stock.StockRequest.subtract_stock', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='add_stock', full_name='stock.StockRequest.add_stock', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal', full_name='stock.StockRequest.internal', index=4,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='stock.StockRequest.order_id', index=5,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STOCKREQUEST_FINDITEMREQUEST, _STOCKREQUEST_SUBTRACTITEMSTOCKREQUEST, _STOCKREQUEST_ADDITEMSTOCKREQUEST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='message', full_name='stock.StockRequest.message',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=287,
  serialized_end=714,
)


_STOCKRESPONSE = _descriptor.Descriptor(
  name='StockResponse',
  full_name='stock.StockResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_info', full_name='stock.StockResponse.request_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='stock.StockResponse.item_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='stock.StockResponse.result', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=716,
  serialized_end=800,
)

_CREATEITEMREQUEST.fields_by_name['request_info'].message_type = general__pb2._REQUESTINFO
_CREATEITEMWITHID.fields_by_name['request_info'].message_type = general__pb2._REQUESTINFO
_STOCKREQUEST_FINDITEMREQUEST.containing_type = _STOCKREQUEST
_STOCKREQUEST_SUBTRACTITEMSTOCKREQUEST.containing_type = _STOCKREQUEST
_STOCKREQUEST_ADDITEMSTOCKREQUEST.containing_type = _STOCKREQUEST
_STOCKREQUEST.fields_by_name['request_info'].message_type = general__pb2._REQUESTINFO
_STOCKREQUEST.fields_by_name['find_item'].message_type = _STOCKREQUEST_FINDITEMREQUEST
_STOCKREQUEST.fields_by_name['subtract_stock'].message_type = _STOCKREQUEST_SUBTRACTITEMSTOCKREQUEST
_STOCKREQUEST.fields_by_name['add_stock'].message_type = _STOCKREQUEST_ADDITEMSTOCKREQUEST
_STOCKREQUEST.oneofs_by_name['message'].fields.append(
  _STOCKREQUEST.fields_by_name['find_item'])
_STOCKREQUEST.fields_by_name['find_item'].containing_oneof = _STOCKREQUEST.oneofs_by_name['message']
_STOCKREQUEST.oneofs_by_name['message'].fields.append(
  _STOCKREQUEST.fields_by_name['subtract_stock'])
_STOCKREQUEST.fields_by_name['subtract_stock'].containing_oneof = _STOCKREQUEST.oneofs_by_name['message']
_STOCKREQUEST.oneofs_by_name['message'].fields.append(
  _STOCKREQUEST.fields_by_name['add_stock'])
_STOCKREQUEST.fields_by_name['add_stock'].containing_oneof = _STOCKREQUEST.oneofs_by_name['message']
_STOCKRESPONSE.fields_by_name['request_info'].message_type = general__pb2._REQUESTINFO
DESCRIPTOR.message_types_by_name['ItemData'] = _ITEMDATA
DESCRIPTOR.message_types_by_name['Count'] = _COUNT
DESCRIPTOR.message_types_by_name['CreateItemRequest'] = _CREATEITEMREQUEST
DESCRIPTOR.message_types_by_name['CreateItemWithId'] = _CREATEITEMWITHID
DESCRIPTOR.message_types_by_name['StockRequest'] = _STOCKREQUEST
DESCRIPTOR.message_types_by_name['StockResponse'] = _STOCKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ItemData = _reflection.GeneratedProtocolMessageType('ItemData', (_message.Message,), {
  'DESCRIPTOR' : _ITEMDATA,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.ItemData)
  })
_sym_db.RegisterMessage(ItemData)

Count = _reflection.GeneratedProtocolMessageType('Count', (_message.Message,), {
  'DESCRIPTOR' : _COUNT,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.Count)
  })
_sym_db.RegisterMessage(Count)

CreateItemRequest = _reflection.GeneratedProtocolMessageType('CreateItemRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEITEMREQUEST,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.CreateItemRequest)
  })
_sym_db.RegisterMessage(CreateItemRequest)

CreateItemWithId = _reflection.GeneratedProtocolMessageType('CreateItemWithId', (_message.Message,), {
  'DESCRIPTOR' : _CREATEITEMWITHID,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.CreateItemWithId)
  })
_sym_db.RegisterMessage(CreateItemWithId)

StockRequest = _reflection.GeneratedProtocolMessageType('StockRequest', (_message.Message,), {

  'FindItemRequest' : _reflection.GeneratedProtocolMessageType('FindItemRequest', (_message.Message,), {
    'DESCRIPTOR' : _STOCKREQUEST_FINDITEMREQUEST,
    '__module__' : 'stock_pb2'
    # @@protoc_insertion_point(class_scope:stock.StockRequest.FindItemRequest)
    })
  ,

  'SubtractItemStockRequest' : _reflection.GeneratedProtocolMessageType('SubtractItemStockRequest', (_message.Message,), {
    'DESCRIPTOR' : _STOCKREQUEST_SUBTRACTITEMSTOCKREQUEST,
    '__module__' : 'stock_pb2'
    # @@protoc_insertion_point(class_scope:stock.StockRequest.SubtractItemStockRequest)
    })
  ,

  'AddItemStockRequest' : _reflection.GeneratedProtocolMessageType('AddItemStockRequest', (_message.Message,), {
    'DESCRIPTOR' : _STOCKREQUEST_ADDITEMSTOCKREQUEST,
    '__module__' : 'stock_pb2'
    # @@protoc_insertion_point(class_scope:stock.StockRequest.AddItemStockRequest)
    })
  ,
  'DESCRIPTOR' : _STOCKREQUEST,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.StockRequest)
  })
_sym_db.RegisterMessage(StockRequest)
_sym_db.RegisterMessage(StockRequest.FindItemRequest)
_sym_db.RegisterMessage(StockRequest.SubtractItemStockRequest)
_sym_db.RegisterMessage(StockRequest.AddItemStockRequest)

StockResponse = _reflection.GeneratedProtocolMessageType('StockResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOCKRESPONSE,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.StockResponse)
  })
_sym_db.RegisterMessage(StockResponse)


# @@protoc_insertion_point(module_scope)
