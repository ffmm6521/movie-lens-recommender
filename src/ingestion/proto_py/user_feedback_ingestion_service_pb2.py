# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_feedback_ingestion_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user_feedback_ingestion_service.proto',
  package='e8',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%user_feedback_ingestion_service.proto\x12\x02\x65\x38\"]\n\x0eRatingFeedback\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x12\n\ncontent_id\x18\x02 \x01(\x03\x12\x16\n\x0etimestamp_secs\x18\x03 \x01(\x03\x12\x0e\n\x06rating\x18\x04 \x01(\x02\"L\n\x1cRecordRatingFeedbacksRequest\x12,\n\x10rating_feedbacks\x18\x01 \x03(\x0b\x32\x12.e8.RatingFeedback\"\x1f\n\x1dRecordRatingFeedbacksResponse2u\n\x15UserFeedbackIngestion\x12\\\n\x15RecordRatingFeedbacks\x12 .e8.RecordRatingFeedbacksRequest\x1a!.e8.RecordRatingFeedbacksResponseb\x06proto3'
)




_RATINGFEEDBACK = _descriptor.Descriptor(
  name='RatingFeedback',
  full_name='e8.RatingFeedback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='e8.RatingFeedback.user_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content_id', full_name='e8.RatingFeedback.content_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp_secs', full_name='e8.RatingFeedback.timestamp_secs', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rating', full_name='e8.RatingFeedback.rating', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=45,
  serialized_end=138,
)


_RECORDRATINGFEEDBACKSREQUEST = _descriptor.Descriptor(
  name='RecordRatingFeedbacksRequest',
  full_name='e8.RecordRatingFeedbacksRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rating_feedbacks', full_name='e8.RecordRatingFeedbacksRequest.rating_feedbacks', index=0,
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
  serialized_start=140,
  serialized_end=216,
)


_RECORDRATINGFEEDBACKSRESPONSE = _descriptor.Descriptor(
  name='RecordRatingFeedbacksResponse',
  full_name='e8.RecordRatingFeedbacksResponse',
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
  serialized_start=218,
  serialized_end=249,
)

_RECORDRATINGFEEDBACKSREQUEST.fields_by_name['rating_feedbacks'].message_type = _RATINGFEEDBACK
DESCRIPTOR.message_types_by_name['RatingFeedback'] = _RATINGFEEDBACK
DESCRIPTOR.message_types_by_name['RecordRatingFeedbacksRequest'] = _RECORDRATINGFEEDBACKSREQUEST
DESCRIPTOR.message_types_by_name['RecordRatingFeedbacksResponse'] = _RECORDRATINGFEEDBACKSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RatingFeedback = _reflection.GeneratedProtocolMessageType('RatingFeedback', (_message.Message,), {
  'DESCRIPTOR' : _RATINGFEEDBACK,
  '__module__' : 'user_feedback_ingestion_service_pb2'
  # @@protoc_insertion_point(class_scope:e8.RatingFeedback)
  })
_sym_db.RegisterMessage(RatingFeedback)

RecordRatingFeedbacksRequest = _reflection.GeneratedProtocolMessageType('RecordRatingFeedbacksRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECORDRATINGFEEDBACKSREQUEST,
  '__module__' : 'user_feedback_ingestion_service_pb2'
  # @@protoc_insertion_point(class_scope:e8.RecordRatingFeedbacksRequest)
  })
_sym_db.RegisterMessage(RecordRatingFeedbacksRequest)

RecordRatingFeedbacksResponse = _reflection.GeneratedProtocolMessageType('RecordRatingFeedbacksResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECORDRATINGFEEDBACKSRESPONSE,
  '__module__' : 'user_feedback_ingestion_service_pb2'
  # @@protoc_insertion_point(class_scope:e8.RecordRatingFeedbacksResponse)
  })
_sym_db.RegisterMessage(RecordRatingFeedbacksResponse)



_USERFEEDBACKINGESTION = _descriptor.ServiceDescriptor(
  name='UserFeedbackIngestion',
  full_name='e8.UserFeedbackIngestion',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=251,
  serialized_end=368,
  methods=[
  _descriptor.MethodDescriptor(
    name='RecordRatingFeedbacks',
    full_name='e8.UserFeedbackIngestion.RecordRatingFeedbacks',
    index=0,
    containing_service=None,
    input_type=_RECORDRATINGFEEDBACKSREQUEST,
    output_type=_RECORDRATINGFEEDBACKSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERFEEDBACKINGESTION)

DESCRIPTOR.services_by_name['UserFeedbackIngestion'] = _USERFEEDBACKINGESTION

# @@protoc_insertion_point(module_scope)
