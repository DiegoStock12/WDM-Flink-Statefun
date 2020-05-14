# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/orders.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/orders.proto',
  package='orders',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x15protobuf/orders.proto\x12\x06orders\"2\n\x05Order\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06userId\x18\x02 \x01(\x03\x12\r\n\x05items\x18\x03 \x03(\x03\"\x1d\n\x0b\x43reateOrder\x12\x0e\n\x06userId\x18\x01 \x01(\x03\"/\n\x11\x43reateOrderWithId\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06userId\x18\x02 \x01(\x03\"&\n\x13\x43reateOrderResponse\x12\x0f\n\x07orderId\x18\x01 \x01(\x03\"\xa9\x01\n\x0cOrderRequest\x12\x32\n\x0cremove_order\x18\x01 \x01(\x0b\x32\x1a.orders.RemoveOrderRequestH\x00\x12.\n\nfind_order\x18\x02 \x01(\x0b\x32\x18.orders.FindOrderRequestH\x00\x12*\n\x08\x61\x64\x64_item\x18\x03 \x01(\x0b\x32\x16.orders.AddItemRequestH\x00\x42\t\n\x07message\" \n\x12RemoveOrderRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"\x1e\n\x10\x46indOrderRequest\x12\n\n\x02id\x18\x01 \x01(\x03\",\n\x0e\x41\x64\x64ItemRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06itemId\x18\x02 \x01(\x03\x62\x06proto3'
)




_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='orders.Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.Order.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userId', full_name='orders.Order.userId', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='orders.Order.items', index=2,
      number=3, type=3, cpp_type=2, label=3,
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
  serialized_start=33,
  serialized_end=83,
)


_CREATEORDER = _descriptor.Descriptor(
  name='CreateOrder',
  full_name='orders.CreateOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='orders.CreateOrder.userId', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=85,
  serialized_end=114,
)


_CREATEORDERWITHID = _descriptor.Descriptor(
  name='CreateOrderWithId',
  full_name='orders.CreateOrderWithId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.CreateOrderWithId.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userId', full_name='orders.CreateOrderWithId.userId', index=1,
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
  serialized_start=116,
  serialized_end=163,
)


_CREATEORDERRESPONSE = _descriptor.Descriptor(
  name='CreateOrderResponse',
  full_name='orders.CreateOrderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orderId', full_name='orders.CreateOrderResponse.orderId', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=165,
  serialized_end=203,
)


_ORDERREQUEST = _descriptor.Descriptor(
  name='OrderRequest',
  full_name='orders.OrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='remove_order', full_name='orders.OrderRequest.remove_order', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='find_order', full_name='orders.OrderRequest.find_order', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='add_item', full_name='orders.OrderRequest.add_item', index=2,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='message', full_name='orders.OrderRequest.message',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=206,
  serialized_end=375,
)


_REMOVEORDERREQUEST = _descriptor.Descriptor(
  name='RemoveOrderRequest',
  full_name='orders.RemoveOrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.RemoveOrderRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=377,
  serialized_end=409,
)


_FINDORDERREQUEST = _descriptor.Descriptor(
  name='FindOrderRequest',
  full_name='orders.FindOrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.FindOrderRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=411,
  serialized_end=441,
)


_ADDITEMREQUEST = _descriptor.Descriptor(
  name='AddItemRequest',
  full_name='orders.AddItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.AddItemRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='itemId', full_name='orders.AddItemRequest.itemId', index=1,
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
  serialized_start=443,
  serialized_end=487,
)

_ORDERREQUEST.fields_by_name['remove_order'].message_type = _REMOVEORDERREQUEST
_ORDERREQUEST.fields_by_name['find_order'].message_type = _FINDORDERREQUEST
_ORDERREQUEST.fields_by_name['add_item'].message_type = _ADDITEMREQUEST
_ORDERREQUEST.oneofs_by_name['message'].fields.append(
  _ORDERREQUEST.fields_by_name['remove_order'])
_ORDERREQUEST.fields_by_name['remove_order'].containing_oneof = _ORDERREQUEST.oneofs_by_name['message']
_ORDERREQUEST.oneofs_by_name['message'].fields.append(
  _ORDERREQUEST.fields_by_name['find_order'])
_ORDERREQUEST.fields_by_name['find_order'].containing_oneof = _ORDERREQUEST.oneofs_by_name['message']
_ORDERREQUEST.oneofs_by_name['message'].fields.append(
  _ORDERREQUEST.fields_by_name['add_item'])
_ORDERREQUEST.fields_by_name['add_item'].containing_oneof = _ORDERREQUEST.oneofs_by_name['message']
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
DESCRIPTOR.message_types_by_name['CreateOrder'] = _CREATEORDER
DESCRIPTOR.message_types_by_name['CreateOrderWithId'] = _CREATEORDERWITHID
DESCRIPTOR.message_types_by_name['CreateOrderResponse'] = _CREATEORDERRESPONSE
DESCRIPTOR.message_types_by_name['OrderRequest'] = _ORDERREQUEST
DESCRIPTOR.message_types_by_name['RemoveOrderRequest'] = _REMOVEORDERREQUEST
DESCRIPTOR.message_types_by_name['FindOrderRequest'] = _FINDORDERREQUEST
DESCRIPTOR.message_types_by_name['AddItemRequest'] = _ADDITEMREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'protobuf.orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.Order)
  })
_sym_db.RegisterMessage(Order)

CreateOrder = _reflection.GeneratedProtocolMessageType('CreateOrder', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORDER,
  '__module__' : 'protobuf.orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.CreateOrder)
  })
_sym_db.RegisterMessage(CreateOrder)

CreateOrderWithId = _reflection.GeneratedProtocolMessageType('CreateOrderWithId', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORDERWITHID,
  '__module__' : 'protobuf.orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.CreateOrderWithId)
  })
_sym_db.RegisterMessage(CreateOrderWithId)

CreateOrderResponse = _reflection.GeneratedProtocolMessageType('CreateOrderResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORDERRESPONSE,
  '__module__' : 'protobuf.orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.CreateOrderResponse)
  })
_sym_db.RegisterMessage(CreateOrderResponse)

OrderRequest = _reflection.GeneratedProtocolMessageType('OrderRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORDERREQUEST,
  '__module__' : 'protobuf.orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.OrderRequest)
  })
_sym_db.RegisterMessage(OrderRequest)

RemoveOrderRequest = _reflection.GeneratedProtocolMessageType('RemoveOrderRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEORDERREQUEST,
  '__module__' : 'protobuf.orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.RemoveOrderRequest)
  })
_sym_db.RegisterMessage(RemoveOrderRequest)

FindOrderRequest = _reflection.GeneratedProtocolMessageType('FindOrderRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDORDERREQUEST,
  '__module__' : 'protobuf.orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.FindOrderRequest)
  })
_sym_db.RegisterMessage(FindOrderRequest)

AddItemRequest = _reflection.GeneratedProtocolMessageType('AddItemRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDITEMREQUEST,
  '__module__' : 'protobuf.orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.AddItemRequest)
  })
_sym_db.RegisterMessage(AddItemRequest)


# @@protoc_insertion_point(module_scope)
