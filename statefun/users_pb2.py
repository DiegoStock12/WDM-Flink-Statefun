# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='users.proto',
  package='users',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0busers.proto\x12\x05users\"&\n\x08UserData\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0e\n\x06\x63redit\x18\x02 \x01(\x03\"\x14\n\x05\x43ount\x12\x0b\n\x03num\x18\x01 \x01(\x04\"\'\n\x11\x43reateUserRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\"2\n\x10\x43reateUserWithId\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x12\n\nrequest_id\x18\x02 \x01(\t\"\xc7\x03\n\x0bUserRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x37\n\tfind_user\x18\x02 \x01(\x0b\x32\".users.UserRequest.FindUserRequestH\x00\x12;\n\x0bremove_user\x18\x03 \x01(\x0b\x32$.users.UserRequest.RemoveUserRequestH\x00\x12\x43\n\x0fsubtract_credit\x18\x04 \x01(\x0b\x32(.users.UserRequest.SubtractCreditRequestH\x00\x12\x39\n\nadd_credit\x18\x05 \x01(\x0b\x32#.users.UserRequest.AddCreditRequestH\x00\x1a\x1d\n\x0f\x46indUserRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x1a\x1f\n\x11RemoveUserRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x1a\x33\n\x15SubtractCreditRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x1a.\n\x10\x41\x64\x64\x43reditRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x42\t\n\x07message\"2\n\x0cUserResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\tb\x06proto3'
)




_USERDATA = _descriptor.Descriptor(
  name='UserData',
  full_name='users.UserData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='users.UserData.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='credit', full_name='users.UserData.credit', index=1,
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
  serialized_start=22,
  serialized_end=60,
)


_COUNT = _descriptor.Descriptor(
  name='Count',
  full_name='users.Count',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='users.Count.num', index=0,
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
  serialized_start=62,
  serialized_end=82,
)


_CREATEUSERREQUEST = _descriptor.Descriptor(
  name='CreateUserRequest',
  full_name='users.CreateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='users.CreateUserRequest.request_id', index=0,
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
  serialized_start=84,
  serialized_end=123,
)


_CREATEUSERWITHID = _descriptor.Descriptor(
  name='CreateUserWithId',
  full_name='users.CreateUserWithId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='users.CreateUserWithId.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='users.CreateUserWithId.request_id', index=1,
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
  serialized_start=125,
  serialized_end=175,
)


_USERREQUEST_FINDUSERREQUEST = _descriptor.Descriptor(
  name='FindUserRequest',
  full_name='users.UserRequest.FindUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='users.UserRequest.FindUserRequest.id', index=0,
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
  serialized_start=459,
  serialized_end=488,
)

_USERREQUEST_REMOVEUSERREQUEST = _descriptor.Descriptor(
  name='RemoveUserRequest',
  full_name='users.UserRequest.RemoveUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='users.UserRequest.RemoveUserRequest.id', index=0,
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
  serialized_start=490,
  serialized_end=521,
)

_USERREQUEST_SUBTRACTCREDITREQUEST = _descriptor.Descriptor(
  name='SubtractCreditRequest',
  full_name='users.UserRequest.SubtractCreditRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='users.UserRequest.SubtractCreditRequest.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='users.UserRequest.SubtractCreditRequest.amount', index=1,
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
  serialized_start=523,
  serialized_end=574,
)

_USERREQUEST_ADDCREDITREQUEST = _descriptor.Descriptor(
  name='AddCreditRequest',
  full_name='users.UserRequest.AddCreditRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='users.UserRequest.AddCreditRequest.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='users.UserRequest.AddCreditRequest.amount', index=1,
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
  serialized_start=576,
  serialized_end=622,
)

_USERREQUEST = _descriptor.Descriptor(
  name='UserRequest',
  full_name='users.UserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='users.UserRequest.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='find_user', full_name='users.UserRequest.find_user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove_user', full_name='users.UserRequest.remove_user', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subtract_credit', full_name='users.UserRequest.subtract_credit', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='add_credit', full_name='users.UserRequest.add_credit', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_USERREQUEST_FINDUSERREQUEST, _USERREQUEST_REMOVEUSERREQUEST, _USERREQUEST_SUBTRACTCREDITREQUEST, _USERREQUEST_ADDCREDITREQUEST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='message', full_name='users.UserRequest.message',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=178,
  serialized_end=633,
)


_USERRESPONSE = _descriptor.Descriptor(
  name='UserResponse',
  full_name='users.UserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='users.UserResponse.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='users.UserResponse.result', index=1,
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
  serialized_start=635,
  serialized_end=685,
)

_USERREQUEST_FINDUSERREQUEST.containing_type = _USERREQUEST
_USERREQUEST_REMOVEUSERREQUEST.containing_type = _USERREQUEST
_USERREQUEST_SUBTRACTCREDITREQUEST.containing_type = _USERREQUEST
_USERREQUEST_ADDCREDITREQUEST.containing_type = _USERREQUEST
_USERREQUEST.fields_by_name['find_user'].message_type = _USERREQUEST_FINDUSERREQUEST
_USERREQUEST.fields_by_name['remove_user'].message_type = _USERREQUEST_REMOVEUSERREQUEST
_USERREQUEST.fields_by_name['subtract_credit'].message_type = _USERREQUEST_SUBTRACTCREDITREQUEST
_USERREQUEST.fields_by_name['add_credit'].message_type = _USERREQUEST_ADDCREDITREQUEST
_USERREQUEST.oneofs_by_name['message'].fields.append(
  _USERREQUEST.fields_by_name['find_user'])
_USERREQUEST.fields_by_name['find_user'].containing_oneof = _USERREQUEST.oneofs_by_name['message']
_USERREQUEST.oneofs_by_name['message'].fields.append(
  _USERREQUEST.fields_by_name['remove_user'])
_USERREQUEST.fields_by_name['remove_user'].containing_oneof = _USERREQUEST.oneofs_by_name['message']
_USERREQUEST.oneofs_by_name['message'].fields.append(
  _USERREQUEST.fields_by_name['subtract_credit'])
_USERREQUEST.fields_by_name['subtract_credit'].containing_oneof = _USERREQUEST.oneofs_by_name['message']
_USERREQUEST.oneofs_by_name['message'].fields.append(
  _USERREQUEST.fields_by_name['add_credit'])
_USERREQUEST.fields_by_name['add_credit'].containing_oneof = _USERREQUEST.oneofs_by_name['message']
DESCRIPTOR.message_types_by_name['UserData'] = _USERDATA
DESCRIPTOR.message_types_by_name['Count'] = _COUNT
DESCRIPTOR.message_types_by_name['CreateUserRequest'] = _CREATEUSERREQUEST
DESCRIPTOR.message_types_by_name['CreateUserWithId'] = _CREATEUSERWITHID
DESCRIPTOR.message_types_by_name['UserRequest'] = _USERREQUEST
DESCRIPTOR.message_types_by_name['UserResponse'] = _USERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserData = _reflection.GeneratedProtocolMessageType('UserData', (_message.Message,), {
  'DESCRIPTOR' : _USERDATA,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.UserData)
  })
_sym_db.RegisterMessage(UserData)

Count = _reflection.GeneratedProtocolMessageType('Count', (_message.Message,), {
  'DESCRIPTOR' : _COUNT,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.Count)
  })
_sym_db.RegisterMessage(Count)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

CreateUserWithId = _reflection.GeneratedProtocolMessageType('CreateUserWithId', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERWITHID,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.CreateUserWithId)
  })
_sym_db.RegisterMessage(CreateUserWithId)

UserRequest = _reflection.GeneratedProtocolMessageType('UserRequest', (_message.Message,), {

  'FindUserRequest' : _reflection.GeneratedProtocolMessageType('FindUserRequest', (_message.Message,), {
    'DESCRIPTOR' : _USERREQUEST_FINDUSERREQUEST,
    '__module__' : 'users_pb2'
    # @@protoc_insertion_point(class_scope:users.UserRequest.FindUserRequest)
    })
  ,

  'RemoveUserRequest' : _reflection.GeneratedProtocolMessageType('RemoveUserRequest', (_message.Message,), {
    'DESCRIPTOR' : _USERREQUEST_REMOVEUSERREQUEST,
    '__module__' : 'users_pb2'
    # @@protoc_insertion_point(class_scope:users.UserRequest.RemoveUserRequest)
    })
  ,

  'SubtractCreditRequest' : _reflection.GeneratedProtocolMessageType('SubtractCreditRequest', (_message.Message,), {
    'DESCRIPTOR' : _USERREQUEST_SUBTRACTCREDITREQUEST,
    '__module__' : 'users_pb2'
    # @@protoc_insertion_point(class_scope:users.UserRequest.SubtractCreditRequest)
    })
  ,

  'AddCreditRequest' : _reflection.GeneratedProtocolMessageType('AddCreditRequest', (_message.Message,), {
    'DESCRIPTOR' : _USERREQUEST_ADDCREDITREQUEST,
    '__module__' : 'users_pb2'
    # @@protoc_insertion_point(class_scope:users.UserRequest.AddCreditRequest)
    })
  ,
  'DESCRIPTOR' : _USERREQUEST,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.UserRequest)
  })
_sym_db.RegisterMessage(UserRequest)
_sym_db.RegisterMessage(UserRequest.FindUserRequest)
_sym_db.RegisterMessage(UserRequest.RemoveUserRequest)
_sym_db.RegisterMessage(UserRequest.SubtractCreditRequest)
_sym_db.RegisterMessage(UserRequest.AddCreditRequest)

UserResponse = _reflection.GeneratedProtocolMessageType('UserResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERRESPONSE,
  '__module__' : 'users_pb2'
  # @@protoc_insertion_point(class_scope:users.UserResponse)
  })
_sym_db.RegisterMessage(UserResponse)


# @@protoc_insertion_point(module_scope)
