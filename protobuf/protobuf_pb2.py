# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eprotobuf.proto\x12\x08zkp_auth\"7\n\x0fRegisterRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\n\n\x02y1\x18\x02 \x01(\x03\x12\n\n\x02y2\x18\x03 \x01(\x03\"\x12\n\x10RegisterResponse\"F\n\x1e\x41uthenticationChallengeRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\n\n\x02r1\x18\x02 \x01(\x03\x12\n\n\x02r2\x18\x03 \x01(\x03\"=\n\x1f\x41uthenticationChallengeResponse\x12\x0f\n\x07\x61uth_id\x18\x01 \x01(\t\x12\t\n\x01\x63\x18\x02 \x01(\x03\"9\n\x1b\x41uthenticationAnswerRequest\x12\x0f\n\x07\x61uth_id\x18\x01 \x01(\t\x12\t\n\x01s\x18\x02 \x01(\x03\"2\n\x1c\x41uthenticationAnswerResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t2\xac\x02\n\x04\x41uth\x12\x43\n\x08Register\x12\x19.zkp_auth.RegisterRequest\x1a\x1a.zkp_auth.RegisterResponse\"\x00\x12v\n\x1d\x43reateAuthenticationChallenge\x12(.zkp_auth.AuthenticationChallengeRequest\x1a).zkp_auth.AuthenticationChallengeResponse\"\x00\x12g\n\x14VerifyAuthentication\x12%.zkp_auth.AuthenticationAnswerRequest\x1a&.zkp_auth.AuthenticationAnswerResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobuf_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGISTERREQUEST._serialized_start=28
  _REGISTERREQUEST._serialized_end=83
  _REGISTERRESPONSE._serialized_start=85
  _REGISTERRESPONSE._serialized_end=103
  _AUTHENTICATIONCHALLENGEREQUEST._serialized_start=105
  _AUTHENTICATIONCHALLENGEREQUEST._serialized_end=175
  _AUTHENTICATIONCHALLENGERESPONSE._serialized_start=177
  _AUTHENTICATIONCHALLENGERESPONSE._serialized_end=238
  _AUTHENTICATIONANSWERREQUEST._serialized_start=240
  _AUTHENTICATIONANSWERREQUEST._serialized_end=297
  _AUTHENTICATIONANSWERRESPONSE._serialized_start=299
  _AUTHENTICATIONANSWERRESPONSE._serialized_end=349
  _AUTH._serialized_start=352
  _AUTH._serialized_end=652
# @@protoc_insertion_point(module_scope)
