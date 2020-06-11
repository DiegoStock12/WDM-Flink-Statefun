# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orders.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import general_pb2 as general__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='orders.proto',
  package='orders',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0corders.proto\x12\x06orders\x1a\rgeneral.proto\"N\n\x0b\x43reateOrder\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\"\n\x0crequest_info\x18\x03 \x01(\x0b\x32\x0c.RequestInfo\"&\n\x13\x43reateOrderResponse\x12\x0f\n\x07orderId\x18\x01 \x01(\t\"\xbd\x04\n\x0cOrderRequest\x12\"\n\x0crequest_info\x18\x01 \x01(\x0b\x32\x0c.RequestInfo\x12?\n\x0cremove_order\x18\x02 \x01(\x0b\x32\'.orders.OrderRequest.RemoveOrderRequestH\x00\x12;\n\nfind_order\x18\x03 \x01(\x0b\x32%.orders.OrderRequest.FindOrderRequestH\x00\x12\x37\n\x08\x61\x64\x64_item\x18\x04 \x01(\x0b\x32#.orders.OrderRequest.AddItemRequestH\x00\x12=\n\x0bremove_item\x18\x05 \x01(\x0b\x32&.orders.OrderRequest.RemoveItemRequestH\x00\x12\x43\n\x0eorder_checkout\x18\x06 \x01(\x0b\x32).orders.OrderRequest.OrderCheckoutRequestH\x00\x1a \n\x12RemoveOrderRequest\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x1e\n\x10\x46indOrderRequest\x12\n\n\x02id\x18\x01 \x01(\t\x1a,\n\x0e\x41\x64\x64ItemRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06itemId\x18\x02 \x01(\t\x1a/\n\x11RemoveItemRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06itemId\x18\x02 \x01(\t\x1a\"\n\x14OrderCheckoutRequest\x12\n\n\x02id\x18\x01 \x01(\tB\t\n\x07message\"3\n\rOrderResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\t\"&\n\x04Item\x12\x0f\n\x07item_id\x18\x01 \x01(\x03\x12\r\n\x05price\x18\x02 \x01(\x03\"\xca\x01\n\x05Order\x12\n\n\x02id\x18\x01 \x01(\t\x12\"\n\x0crequest_info\x18\x02 \x01(\x0b\x32\x0c.RequestInfo\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\r\n\x05items\x18\x04 \x03(\t\x12\x12\n\ntotal_cost\x18\x05 \x01(\x03\x12\x0c\n\x04paid\x18\x06 \x01(\x08\x12$\n\x06intent\x18\x07 \x01(\x0e\x32\x14.orders.Order.Intent\")\n\x06Intent\x12\x07\n\x03PAY\x10\x00\x12\n\n\x06\x43\x41NCEL\x10\x01\x12\n\n\x06STATUS\x10\x02\"E\n\rOrdersPayFind\x12\"\n\x0crequest_info\x18\x01 \x01(\x0b\x32\x0c.RequestInfo\x12\x10\n\x08order_id\x18\x02 \x01(\t\"J\n\x12OrderPaymentCancel\x12\"\n\x0crequest_info\x18\x01 \x01(\x0b\x32\x0c.RequestInfo\x12\x10\n\x08order_id\x18\x02 \x01(\t\"N\n\x17OrderPaymentCancelReply\x12\"\n\x0crequest_info\x18\x01 \x01(\x0b\x32\x0c.RequestInfo\x12\x0f\n\x07success\x18\x02 \x01(\x08\x62\x06proto3'
  ,
  dependencies=[general__pb2.DESCRIPTOR,])



_ORDER_INTENT = _descriptor.EnumDescriptor(
  name='Intent',
  full_name='orders.Order.Intent',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PAY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCEL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=990,
  serialized_end=1031,
)
_sym_db.RegisterEnumDescriptor(_ORDER_INTENT)


_CREATEORDER = _descriptor.Descriptor(
  name='CreateOrder',
  full_name='orders.CreateOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='orders.CreateOrder.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.CreateOrder.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_info', full_name='orders.CreateOrder.request_info', index=2,
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
  ],
  serialized_start=39,
  serialized_end=117,
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
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=119,
  serialized_end=157,
)


_ORDERREQUEST_REMOVEORDERREQUEST = _descriptor.Descriptor(
  name='RemoveOrderRequest',
  full_name='orders.OrderRequest.RemoveOrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.OrderRequest.RemoveOrderRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=527,
  serialized_end=559,
)

_ORDERREQUEST_FINDORDERREQUEST = _descriptor.Descriptor(
  name='FindOrderRequest',
  full_name='orders.OrderRequest.FindOrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.OrderRequest.FindOrderRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=561,
  serialized_end=591,
)

_ORDERREQUEST_ADDITEMREQUEST = _descriptor.Descriptor(
  name='AddItemRequest',
  full_name='orders.OrderRequest.AddItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.OrderRequest.AddItemRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='itemId', full_name='orders.OrderRequest.AddItemRequest.itemId', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=593,
  serialized_end=637,
)

_ORDERREQUEST_REMOVEITEMREQUEST = _descriptor.Descriptor(
  name='RemoveItemRequest',
  full_name='orders.OrderRequest.RemoveItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.OrderRequest.RemoveItemRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='itemId', full_name='orders.OrderRequest.RemoveItemRequest.itemId', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=639,
  serialized_end=686,
)

_ORDERREQUEST_ORDERCHECKOUTREQUEST = _descriptor.Descriptor(
  name='OrderCheckoutRequest',
  full_name='orders.OrderRequest.OrderCheckoutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.OrderRequest.OrderCheckoutRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=688,
  serialized_end=722,
)

_ORDERREQUEST = _descriptor.Descriptor(
  name='OrderRequest',
  full_name='orders.OrderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_info', full_name='orders.OrderRequest.request_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove_order', full_name='orders.OrderRequest.remove_order', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='find_order', full_name='orders.OrderRequest.find_order', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='add_item', full_name='orders.OrderRequest.add_item', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove_item', full_name='orders.OrderRequest.remove_item', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_checkout', full_name='orders.OrderRequest.order_checkout', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ORDERREQUEST_REMOVEORDERREQUEST, _ORDERREQUEST_FINDORDERREQUEST, _ORDERREQUEST_ADDITEMREQUEST, _ORDERREQUEST_REMOVEITEMREQUEST, _ORDERREQUEST_ORDERCHECKOUTREQUEST, ],
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
  serialized_start=160,
  serialized_end=733,
)


_ORDERRESPONSE = _descriptor.Descriptor(
  name='OrderResponse',
  full_name='orders.OrderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='orders.OrderResponse.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='orders.OrderResponse.result', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=735,
  serialized_end=786,
)


_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='orders.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='orders.Item.item_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='orders.Item.price', index=1,
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
  serialized_start=788,
  serialized_end=826,
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
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_info', full_name='orders.Order.request_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='orders.Order.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='orders.Order.items', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_cost', full_name='orders.Order.total_cost', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paid', full_name='orders.Order.paid', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intent', full_name='orders.Order.intent', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ORDER_INTENT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=829,
  serialized_end=1031,
)


_ORDERSPAYFIND = _descriptor.Descriptor(
  name='OrdersPayFind',
  full_name='orders.OrdersPayFind',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_info', full_name='orders.OrdersPayFind.request_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='orders.OrdersPayFind.order_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1033,
  serialized_end=1102,
)


_ORDERPAYMENTCANCEL = _descriptor.Descriptor(
  name='OrderPaymentCancel',
  full_name='orders.OrderPaymentCancel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_info', full_name='orders.OrderPaymentCancel.request_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='orders.OrderPaymentCancel.order_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1104,
  serialized_end=1178,
)


_ORDERPAYMENTCANCELREPLY = _descriptor.Descriptor(
  name='OrderPaymentCancelReply',
  full_name='orders.OrderPaymentCancelReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_info', full_name='orders.OrderPaymentCancelReply.request_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='orders.OrderPaymentCancelReply.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=1180,
  serialized_end=1258,
)

_CREATEORDER.fields_by_name['request_info'].message_type = general__pb2._REQUESTINFO
_ORDERREQUEST_REMOVEORDERREQUEST.containing_type = _ORDERREQUEST
_ORDERREQUEST_FINDORDERREQUEST.containing_type = _ORDERREQUEST
_ORDERREQUEST_ADDITEMREQUEST.containing_type = _ORDERREQUEST
_ORDERREQUEST_REMOVEITEMREQUEST.containing_type = _ORDERREQUEST
_ORDERREQUEST_ORDERCHECKOUTREQUEST.containing_type = _ORDERREQUEST
_ORDERREQUEST.fields_by_name['request_info'].message_type = general__pb2._REQUESTINFO
_ORDERREQUEST.fields_by_name['remove_order'].message_type = _ORDERREQUEST_REMOVEORDERREQUEST
_ORDERREQUEST.fields_by_name['find_order'].message_type = _ORDERREQUEST_FINDORDERREQUEST
_ORDERREQUEST.fields_by_name['add_item'].message_type = _ORDERREQUEST_ADDITEMREQUEST
_ORDERREQUEST.fields_by_name['remove_item'].message_type = _ORDERREQUEST_REMOVEITEMREQUEST
_ORDERREQUEST.fields_by_name['order_checkout'].message_type = _ORDERREQUEST_ORDERCHECKOUTREQUEST
_ORDERREQUEST.oneofs_by_name['message'].fields.append(
  _ORDERREQUEST.fields_by_name['remove_order'])
_ORDERREQUEST.fields_by_name['remove_order'].containing_oneof = _ORDERREQUEST.oneofs_by_name['message']
_ORDERREQUEST.oneofs_by_name['message'].fields.append(
  _ORDERREQUEST.fields_by_name['find_order'])
_ORDERREQUEST.fields_by_name['find_order'].containing_oneof = _ORDERREQUEST.oneofs_by_name['message']
_ORDERREQUEST.oneofs_by_name['message'].fields.append(
  _ORDERREQUEST.fields_by_name['add_item'])
_ORDERREQUEST.fields_by_name['add_item'].containing_oneof = _ORDERREQUEST.oneofs_by_name['message']
_ORDERREQUEST.oneofs_by_name['message'].fields.append(
  _ORDERREQUEST.fields_by_name['remove_item'])
_ORDERREQUEST.fields_by_name['remove_item'].containing_oneof = _ORDERREQUEST.oneofs_by_name['message']
_ORDERREQUEST.oneofs_by_name['message'].fields.append(
  _ORDERREQUEST.fields_by_name['order_checkout'])
_ORDERREQUEST.fields_by_name['order_checkout'].containing_oneof = _ORDERREQUEST.oneofs_by_name['message']
_ORDER.fields_by_name['request_info'].message_type = general__pb2._REQUESTINFO
_ORDER.fields_by_name['intent'].enum_type = _ORDER_INTENT
_ORDER_INTENT.containing_type = _ORDER
_ORDERSPAYFIND.fields_by_name['request_info'].message_type = general__pb2._REQUESTINFO
_ORDERPAYMENTCANCEL.fields_by_name['request_info'].message_type = general__pb2._REQUESTINFO
_ORDERPAYMENTCANCELREPLY.fields_by_name['request_info'].message_type = general__pb2._REQUESTINFO
DESCRIPTOR.message_types_by_name['CreateOrder'] = _CREATEORDER
DESCRIPTOR.message_types_by_name['CreateOrderResponse'] = _CREATEORDERRESPONSE
DESCRIPTOR.message_types_by_name['OrderRequest'] = _ORDERREQUEST
DESCRIPTOR.message_types_by_name['OrderResponse'] = _ORDERRESPONSE
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
DESCRIPTOR.message_types_by_name['OrdersPayFind'] = _ORDERSPAYFIND
DESCRIPTOR.message_types_by_name['OrderPaymentCancel'] = _ORDERPAYMENTCANCEL
DESCRIPTOR.message_types_by_name['OrderPaymentCancelReply'] = _ORDERPAYMENTCANCELREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateOrder = _reflection.GeneratedProtocolMessageType('CreateOrder', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORDER,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.CreateOrder)
  })
_sym_db.RegisterMessage(CreateOrder)

CreateOrderResponse = _reflection.GeneratedProtocolMessageType('CreateOrderResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORDERRESPONSE,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.CreateOrderResponse)
  })
_sym_db.RegisterMessage(CreateOrderResponse)

OrderRequest = _reflection.GeneratedProtocolMessageType('OrderRequest', (_message.Message,), {

  'RemoveOrderRequest' : _reflection.GeneratedProtocolMessageType('RemoveOrderRequest', (_message.Message,), {
    'DESCRIPTOR' : _ORDERREQUEST_REMOVEORDERREQUEST,
    '__module__' : 'orders_pb2'
    # @@protoc_insertion_point(class_scope:orders.OrderRequest.RemoveOrderRequest)
    })
  ,

  'FindOrderRequest' : _reflection.GeneratedProtocolMessageType('FindOrderRequest', (_message.Message,), {
    'DESCRIPTOR' : _ORDERREQUEST_FINDORDERREQUEST,
    '__module__' : 'orders_pb2'
    # @@protoc_insertion_point(class_scope:orders.OrderRequest.FindOrderRequest)
    })
  ,

  'AddItemRequest' : _reflection.GeneratedProtocolMessageType('AddItemRequest', (_message.Message,), {
    'DESCRIPTOR' : _ORDERREQUEST_ADDITEMREQUEST,
    '__module__' : 'orders_pb2'
    # @@protoc_insertion_point(class_scope:orders.OrderRequest.AddItemRequest)
    })
  ,

  'RemoveItemRequest' : _reflection.GeneratedProtocolMessageType('RemoveItemRequest', (_message.Message,), {
    'DESCRIPTOR' : _ORDERREQUEST_REMOVEITEMREQUEST,
    '__module__' : 'orders_pb2'
    # @@protoc_insertion_point(class_scope:orders.OrderRequest.RemoveItemRequest)
    })
  ,

  'OrderCheckoutRequest' : _reflection.GeneratedProtocolMessageType('OrderCheckoutRequest', (_message.Message,), {
    'DESCRIPTOR' : _ORDERREQUEST_ORDERCHECKOUTREQUEST,
    '__module__' : 'orders_pb2'
    # @@protoc_insertion_point(class_scope:orders.OrderRequest.OrderCheckoutRequest)
    })
  ,
  'DESCRIPTOR' : _ORDERREQUEST,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.OrderRequest)
  })
_sym_db.RegisterMessage(OrderRequest)
_sym_db.RegisterMessage(OrderRequest.RemoveOrderRequest)
_sym_db.RegisterMessage(OrderRequest.FindOrderRequest)
_sym_db.RegisterMessage(OrderRequest.AddItemRequest)
_sym_db.RegisterMessage(OrderRequest.RemoveItemRequest)
_sym_db.RegisterMessage(OrderRequest.OrderCheckoutRequest)

OrderResponse = _reflection.GeneratedProtocolMessageType('OrderResponse', (_message.Message,), {
  'DESCRIPTOR' : _ORDERRESPONSE,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.OrderResponse)
  })
_sym_db.RegisterMessage(OrderResponse)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
  'DESCRIPTOR' : _ITEM,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.Item)
  })
_sym_db.RegisterMessage(Item)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.Order)
  })
_sym_db.RegisterMessage(Order)

OrdersPayFind = _reflection.GeneratedProtocolMessageType('OrdersPayFind', (_message.Message,), {
  'DESCRIPTOR' : _ORDERSPAYFIND,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.OrdersPayFind)
  })
_sym_db.RegisterMessage(OrdersPayFind)

OrderPaymentCancel = _reflection.GeneratedProtocolMessageType('OrderPaymentCancel', (_message.Message,), {
  'DESCRIPTOR' : _ORDERPAYMENTCANCEL,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.OrderPaymentCancel)
  })
_sym_db.RegisterMessage(OrderPaymentCancel)

OrderPaymentCancelReply = _reflection.GeneratedProtocolMessageType('OrderPaymentCancelReply', (_message.Message,), {
  'DESCRIPTOR' : _ORDERPAYMENTCANCELREPLY,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.OrderPaymentCancelReply)
  })
_sym_db.RegisterMessage(OrderPaymentCancelReply)


# @@protoc_insertion_point(module_scope)
