# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weni/protobuf/connect/project.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='weni/protobuf/connect/project.proto',
  package='weni.connect.project',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#weni/protobuf/connect/project.proto\x12\x14weni.connect.project\x1a\x1bgoogle/protobuf/empty.proto\"x\n\x12\x43lassifierResponse\x12\x1a\n\x12\x61uthorization_uuid\x18\x01 \x01(\t\x12\x17\n\x0f\x63lassifier_type\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\tis_active\x18\x04 \x01(\x08\x12\x0c\n\x04uuid\x18\x05 \x01(\t\"-\n\x15\x43lassifierListRequest\x12\x14\n\x0cproject_uuid\x18\x01 \x01(\t\"z\n\x17\x43lassifierCreateRequest\x12\x14\n\x0cproject_uuid\x18\x01 \x01(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x17\n\x0f\x63lassifier_type\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x05 \x01(\t\")\n\x19\x43lassifierRetrieveRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"<\n\x18\x43lassifierDestroyRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x12\n\nuser_email\x18\x02 \x01(\t\"h\n\x13\x43hannelListResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x03 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\x12\x14\n\x0cproject_uuid\x18\x05 \x01(\t\"T\n\x15\x43hannelCreateResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x03 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\"*\n\x12\x43hannelListRequest\x12\x14\n\x0c\x63hannel_type\x18\x01 \x01(\t\"b\n\x14\x43reateChannelRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x14\n\x0cproject_uuid\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\x12\x18\n\x10\x63hanneltype_code\x18\x04 \x01(\t\";\n\x15ReleaseChannelRequest\x12\x14\n\x0c\x63hannel_uuid\x18\x01 \x01(\t\x12\x0c\n\x04user\x18\x02 \x01(\t2\xe6\x05\n\x11ProjectController\x12g\n\nClassifier\x12+.weni.connect.project.ClassifierListRequest\x1a(.weni.connect.project.ClassifierResponse\"\x00\x30\x01\x12m\n\x10\x43reateClassifier\x12-.weni.connect.project.ClassifierCreateRequest\x1a(.weni.connect.project.ClassifierResponse\"\x00\x12q\n\x12RetrieveClassifier\x12/.weni.connect.project.ClassifierRetrieveRequest\x1a(.weni.connect.project.ClassifierResponse\"\x00\x12]\n\x11\x44\x65stroyClassifier\x12..weni.connect.project.ClassifierDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x62\n\x07\x43hannel\x12(.weni.connect.project.ChannelListRequest\x1a).weni.connect.project.ChannelListResponse\"\x00\x30\x01\x12j\n\rCreateChannel\x12*.weni.connect.project.CreateChannelRequest\x1a+.weni.connect.project.ChannelCreateResponse\"\x00\x12W\n\x0eReleaseChannel\x12+.weni.connect.project.ReleaseChannelRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_CLASSIFIERRESPONSE = _descriptor.Descriptor(
  name='ClassifierResponse',
  full_name='weni.connect.project.ClassifierResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='authorization_uuid', full_name='weni.connect.project.ClassifierResponse.authorization_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='classifier_type', full_name='weni.connect.project.ClassifierResponse.classifier_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.connect.project.ClassifierResponse.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_active', full_name='weni.connect.project.ClassifierResponse.is_active', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.connect.project.ClassifierResponse.uuid', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=90,
  serialized_end=210,
)


_CLASSIFIERLISTREQUEST = _descriptor.Descriptor(
  name='ClassifierListRequest',
  full_name='weni.connect.project.ClassifierListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_uuid', full_name='weni.connect.project.ClassifierListRequest.project_uuid', index=0,
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
  serialized_start=212,
  serialized_end=257,
)


_CLASSIFIERCREATEREQUEST = _descriptor.Descriptor(
  name='ClassifierCreateRequest',
  full_name='weni.connect.project.ClassifierCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_uuid', full_name='weni.connect.project.ClassifierCreateRequest.project_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='weni.connect.project.ClassifierCreateRequest.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='classifier_type', full_name='weni.connect.project.ClassifierCreateRequest.classifier_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.connect.project.ClassifierCreateRequest.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_token', full_name='weni.connect.project.ClassifierCreateRequest.access_token', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=259,
  serialized_end=381,
)


_CLASSIFIERRETRIEVEREQUEST = _descriptor.Descriptor(
  name='ClassifierRetrieveRequest',
  full_name='weni.connect.project.ClassifierRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.connect.project.ClassifierRetrieveRequest.uuid', index=0,
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
  serialized_start=383,
  serialized_end=424,
)


_CLASSIFIERDESTROYREQUEST = _descriptor.Descriptor(
  name='ClassifierDestroyRequest',
  full_name='weni.connect.project.ClassifierDestroyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.connect.project.ClassifierDestroyRequest.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_email', full_name='weni.connect.project.ClassifierDestroyRequest.user_email', index=1,
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
  serialized_start=426,
  serialized_end=486,
)


_CHANNELLISTRESPONSE = _descriptor.Descriptor(
  name='ChannelListResponse',
  full_name='weni.connect.project.ChannelListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.connect.project.ChannelListResponse.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.connect.project.ChannelListResponse.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='weni.connect.project.ChannelListResponse.config', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='weni.connect.project.ChannelListResponse.address', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_uuid', full_name='weni.connect.project.ChannelListResponse.project_uuid', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=488,
  serialized_end=592,
)


_CHANNELCREATERESPONSE = _descriptor.Descriptor(
  name='ChannelCreateResponse',
  full_name='weni.connect.project.ChannelCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.connect.project.ChannelCreateResponse.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.connect.project.ChannelCreateResponse.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='weni.connect.project.ChannelCreateResponse.config', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='weni.connect.project.ChannelCreateResponse.address', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=594,
  serialized_end=678,
)


_CHANNELLISTREQUEST = _descriptor.Descriptor(
  name='ChannelListRequest',
  full_name='weni.connect.project.ChannelListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_type', full_name='weni.connect.project.ChannelListRequest.channel_type', index=0,
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
  serialized_start=680,
  serialized_end=722,
)


_CREATECHANNELREQUEST = _descriptor.Descriptor(
  name='CreateChannelRequest',
  full_name='weni.connect.project.CreateChannelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='weni.connect.project.CreateChannelRequest.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_uuid', full_name='weni.connect.project.CreateChannelRequest.project_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='weni.connect.project.CreateChannelRequest.data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channeltype_code', full_name='weni.connect.project.CreateChannelRequest.channeltype_code', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=724,
  serialized_end=822,
)


_RELEASECHANNELREQUEST = _descriptor.Descriptor(
  name='ReleaseChannelRequest',
  full_name='weni.connect.project.ReleaseChannelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_uuid', full_name='weni.connect.project.ReleaseChannelRequest.channel_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='weni.connect.project.ReleaseChannelRequest.user', index=1,
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
  serialized_start=824,
  serialized_end=883,
)

DESCRIPTOR.message_types_by_name['ClassifierResponse'] = _CLASSIFIERRESPONSE
DESCRIPTOR.message_types_by_name['ClassifierListRequest'] = _CLASSIFIERLISTREQUEST
DESCRIPTOR.message_types_by_name['ClassifierCreateRequest'] = _CLASSIFIERCREATEREQUEST
DESCRIPTOR.message_types_by_name['ClassifierRetrieveRequest'] = _CLASSIFIERRETRIEVEREQUEST
DESCRIPTOR.message_types_by_name['ClassifierDestroyRequest'] = _CLASSIFIERDESTROYREQUEST
DESCRIPTOR.message_types_by_name['ChannelListResponse'] = _CHANNELLISTRESPONSE
DESCRIPTOR.message_types_by_name['ChannelCreateResponse'] = _CHANNELCREATERESPONSE
DESCRIPTOR.message_types_by_name['ChannelListRequest'] = _CHANNELLISTREQUEST
DESCRIPTOR.message_types_by_name['CreateChannelRequest'] = _CREATECHANNELREQUEST
DESCRIPTOR.message_types_by_name['ReleaseChannelRequest'] = _RELEASECHANNELREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClassifierResponse = _reflection.GeneratedProtocolMessageType('ClassifierResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIERRESPONSE,
  '__module__' : 'weni.protobuf.connect.project_pb2'
  # @@protoc_insertion_point(class_scope:weni.connect.project.ClassifierResponse)
  })
_sym_db.RegisterMessage(ClassifierResponse)

ClassifierListRequest = _reflection.GeneratedProtocolMessageType('ClassifierListRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIERLISTREQUEST,
  '__module__' : 'weni.protobuf.connect.project_pb2'
  # @@protoc_insertion_point(class_scope:weni.connect.project.ClassifierListRequest)
  })
_sym_db.RegisterMessage(ClassifierListRequest)

ClassifierCreateRequest = _reflection.GeneratedProtocolMessageType('ClassifierCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIERCREATEREQUEST,
  '__module__' : 'weni.protobuf.connect.project_pb2'
  # @@protoc_insertion_point(class_scope:weni.connect.project.ClassifierCreateRequest)
  })
_sym_db.RegisterMessage(ClassifierCreateRequest)

ClassifierRetrieveRequest = _reflection.GeneratedProtocolMessageType('ClassifierRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIERRETRIEVEREQUEST,
  '__module__' : 'weni.protobuf.connect.project_pb2'
  # @@protoc_insertion_point(class_scope:weni.connect.project.ClassifierRetrieveRequest)
  })
_sym_db.RegisterMessage(ClassifierRetrieveRequest)

ClassifierDestroyRequest = _reflection.GeneratedProtocolMessageType('ClassifierDestroyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIERDESTROYREQUEST,
  '__module__' : 'weni.protobuf.connect.project_pb2'
  # @@protoc_insertion_point(class_scope:weni.connect.project.ClassifierDestroyRequest)
  })
_sym_db.RegisterMessage(ClassifierDestroyRequest)

ChannelListResponse = _reflection.GeneratedProtocolMessageType('ChannelListResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELLISTRESPONSE,
  '__module__' : 'weni.protobuf.connect.project_pb2'
  # @@protoc_insertion_point(class_scope:weni.connect.project.ChannelListResponse)
  })
_sym_db.RegisterMessage(ChannelListResponse)

ChannelCreateResponse = _reflection.GeneratedProtocolMessageType('ChannelCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELCREATERESPONSE,
  '__module__' : 'weni.protobuf.connect.project_pb2'
  # @@protoc_insertion_point(class_scope:weni.connect.project.ChannelCreateResponse)
  })
_sym_db.RegisterMessage(ChannelCreateResponse)

ChannelListRequest = _reflection.GeneratedProtocolMessageType('ChannelListRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELLISTREQUEST,
  '__module__' : 'weni.protobuf.connect.project_pb2'
  # @@protoc_insertion_point(class_scope:weni.connect.project.ChannelListRequest)
  })
_sym_db.RegisterMessage(ChannelListRequest)

CreateChannelRequest = _reflection.GeneratedProtocolMessageType('CreateChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECHANNELREQUEST,
  '__module__' : 'weni.protobuf.connect.project_pb2'
  # @@protoc_insertion_point(class_scope:weni.connect.project.CreateChannelRequest)
  })
_sym_db.RegisterMessage(CreateChannelRequest)

ReleaseChannelRequest = _reflection.GeneratedProtocolMessageType('ReleaseChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _RELEASECHANNELREQUEST,
  '__module__' : 'weni.protobuf.connect.project_pb2'
  # @@protoc_insertion_point(class_scope:weni.connect.project.ReleaseChannelRequest)
  })
_sym_db.RegisterMessage(ReleaseChannelRequest)



_PROJECTCONTROLLER = _descriptor.ServiceDescriptor(
  name='ProjectController',
  full_name='weni.connect.project.ProjectController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=886,
  serialized_end=1628,
  methods=[
  _descriptor.MethodDescriptor(
    name='Classifier',
    full_name='weni.connect.project.ProjectController.Classifier',
    index=0,
    containing_service=None,
    input_type=_CLASSIFIERLISTREQUEST,
    output_type=_CLASSIFIERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateClassifier',
    full_name='weni.connect.project.ProjectController.CreateClassifier',
    index=1,
    containing_service=None,
    input_type=_CLASSIFIERCREATEREQUEST,
    output_type=_CLASSIFIERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RetrieveClassifier',
    full_name='weni.connect.project.ProjectController.RetrieveClassifier',
    index=2,
    containing_service=None,
    input_type=_CLASSIFIERRETRIEVEREQUEST,
    output_type=_CLASSIFIERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DestroyClassifier',
    full_name='weni.connect.project.ProjectController.DestroyClassifier',
    index=3,
    containing_service=None,
    input_type=_CLASSIFIERDESTROYREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Channel',
    full_name='weni.connect.project.ProjectController.Channel',
    index=4,
    containing_service=None,
    input_type=_CHANNELLISTREQUEST,
    output_type=_CHANNELLISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateChannel',
    full_name='weni.connect.project.ProjectController.CreateChannel',
    index=5,
    containing_service=None,
    input_type=_CREATECHANNELREQUEST,
    output_type=_CHANNELCREATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReleaseChannel',
    full_name='weni.connect.project.ProjectController.ReleaseChannel',
    index=6,
    containing_service=None,
    input_type=_RELEASECHANNELREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROJECTCONTROLLER)

DESCRIPTOR.services_by_name['ProjectController'] = _PROJECTCONTROLLER

# @@protoc_insertion_point(module_scope)
