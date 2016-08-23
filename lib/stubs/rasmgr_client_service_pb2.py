# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rasmgr_client_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_service_pb2 as common__service__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rasmgr_client_service.proto',
  package='rasnet.service',
  #syntax='proto3'
  serialized_pb=_b('\n\x1brasmgr_client_service.proto\x12\x0erasnet.service\x1a\x14\x63ommon_service.proto\"4\n\nConnectReq\x12\x10\n\x08userName\x18\x01 \x01(\t\x12\x14\n\x0cpasswordHash\x18\x02 \x01(\t\"M\n\x0b\x43onnectRepl\x12\x12\n\nclientUUID\x18\x01 \x01(\t\x12\x18\n\x10keepAliveTimeout\x18\x02 \x01(\x05\x12\x10\n\x08\x63lientId\x18\x03 \x01(\x05\"5\n\rDisconnectReq\x12\x12\n\nclientUUID\x18\x01 \x01(\t\x12\x10\n\x08\x63lientId\x18\x02 \x01(\x05\"G\n\tOpenDbReq\x12\x12\n\nclientUUID\x18\x01 \x01(\t\x12\x10\n\x08\x63lientId\x18\x02 \x01(\x05\x12\x14\n\x0c\x64\x61tabaseName\x18\x03 \x01(\t\"`\n\nOpenDbRepl\x12\x17\n\x0f\x63lientSessionId\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x62SessionId\x18\x02 \x01(\t\x12\x16\n\x0eserverHostName\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\r\"G\n\nCloseDbReq\x12\x12\n\nclientUUID\x18\x01 \x01(\t\x12\x10\n\x08\x63lientId\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x62SessionId\x18\x03 \x01(\t\"\"\n\x0cKeepAliveReq\x12\x12\n\nclientUUID\x18\x01 \x01(\t2\xdb\x02\n\x13RasMgrClientService\x12\x42\n\x07\x43onnect\x12\x1a.rasnet.service.ConnectReq\x1a\x1b.rasnet.service.ConnectRepl\x12\x41\n\nDisconnect\x12\x1d.rasnet.service.DisconnectReq\x1a\x14.rasnet.service.Void\x12?\n\x06OpenDb\x12\x19.rasnet.service.OpenDbReq\x1a\x1a.rasnet.service.OpenDbRepl\x12;\n\x07\x43loseDb\x12\x1a.rasnet.service.CloseDbReq\x1a\x14.rasnet.service.Void\x12?\n\tKeepAlive\x12\x1c.rasnet.service.KeepAliveReq\x1a\x14.rasnet.service.VoidB#\n\x1borg.rasdaman.rasnet.service\x80\x01\x00\x88\x01\x00\x62\x06proto3')
  ,
  dependencies=[common__service__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CONNECTREQ = _descriptor.Descriptor(
  name='ConnectReq',
  full_name='rasnet.service.ConnectReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userName', full_name='rasnet.service.ConnectReq.userName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='passwordHash', full_name='rasnet.service.ConnectReq.passwordHash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  #syntax='proto3'
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=121,
)


_CONNECTREPL = _descriptor.Descriptor(
  name='ConnectRepl',
  full_name='rasnet.service.ConnectRepl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientUUID', full_name='rasnet.service.ConnectRepl.clientUUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keepAliveTimeout', full_name='rasnet.service.ConnectRepl.keepAliveTimeout', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='rasnet.service.ConnectRepl.clientId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  #syntax='proto3'
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=200,
)


_DISCONNECTREQ = _descriptor.Descriptor(
  name='DisconnectReq',
  full_name='rasnet.service.DisconnectReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientUUID', full_name='rasnet.service.DisconnectReq.clientUUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='rasnet.service.DisconnectReq.clientId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  #syntax='proto3'
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=255,
)


_OPENDBREQ = _descriptor.Descriptor(
  name='OpenDbReq',
  full_name='rasnet.service.OpenDbReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientUUID', full_name='rasnet.service.OpenDbReq.clientUUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='rasnet.service.OpenDbReq.clientId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='databaseName', full_name='rasnet.service.OpenDbReq.databaseName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  #syntax='proto3'
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=328,
)


_OPENDBREPL = _descriptor.Descriptor(
  name='OpenDbRepl',
  full_name='rasnet.service.OpenDbRepl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientSessionId', full_name='rasnet.service.OpenDbRepl.clientSessionId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dbSessionId', full_name='rasnet.service.OpenDbRepl.dbSessionId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serverHostName', full_name='rasnet.service.OpenDbRepl.serverHostName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='rasnet.service.OpenDbRepl.port', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  #syntax='proto3'
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=330,
  serialized_end=426,
)


_CLOSEDBREQ = _descriptor.Descriptor(
  name='CloseDbReq',
  full_name='rasnet.service.CloseDbReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientUUID', full_name='rasnet.service.CloseDbReq.clientUUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='rasnet.service.CloseDbReq.clientId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dbSessionId', full_name='rasnet.service.CloseDbReq.dbSessionId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  #syntax='proto3'
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=428,
  serialized_end=499,
)


_KEEPALIVEREQ = _descriptor.Descriptor(
  name='KeepAliveReq',
  full_name='rasnet.service.KeepAliveReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientUUID', full_name='rasnet.service.KeepAliveReq.clientUUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  #syntax='proto3'
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=501,
  serialized_end=535,
)

DESCRIPTOR.message_types_by_name['ConnectReq'] = _CONNECTREQ
DESCRIPTOR.message_types_by_name['ConnectRepl'] = _CONNECTREPL
DESCRIPTOR.message_types_by_name['DisconnectReq'] = _DISCONNECTREQ
DESCRIPTOR.message_types_by_name['OpenDbReq'] = _OPENDBREQ
DESCRIPTOR.message_types_by_name['OpenDbRepl'] = _OPENDBREPL
DESCRIPTOR.message_types_by_name['CloseDbReq'] = _CLOSEDBREQ
DESCRIPTOR.message_types_by_name['KeepAliveReq'] = _KEEPALIVEREQ

ConnectReq = _reflection.GeneratedProtocolMessageType('ConnectReq', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTREQ,
  __module__ = 'rasmgr_client_service_pb2'
  # @@protoc_insertion_point(class_scope:rasnet.service.ConnectReq)
  ))
_sym_db.RegisterMessage(ConnectReq)

ConnectRepl = _reflection.GeneratedProtocolMessageType('ConnectRepl', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTREPL,
  __module__ = 'rasmgr_client_service_pb2'
  # @@protoc_insertion_point(class_scope:rasnet.service.ConnectRepl)
  ))
_sym_db.RegisterMessage(ConnectRepl)

DisconnectReq = _reflection.GeneratedProtocolMessageType('DisconnectReq', (_message.Message,), dict(
  DESCRIPTOR = _DISCONNECTREQ,
  __module__ = 'rasmgr_client_service_pb2'
  # @@protoc_insertion_point(class_scope:rasnet.service.DisconnectReq)
  ))
_sym_db.RegisterMessage(DisconnectReq)

OpenDbReq = _reflection.GeneratedProtocolMessageType('OpenDbReq', (_message.Message,), dict(
  DESCRIPTOR = _OPENDBREQ,
  __module__ = 'rasmgr_client_service_pb2'
  # @@protoc_insertion_point(class_scope:rasnet.service.OpenDbReq)
  ))
_sym_db.RegisterMessage(OpenDbReq)

OpenDbRepl = _reflection.GeneratedProtocolMessageType('OpenDbRepl', (_message.Message,), dict(
  DESCRIPTOR = _OPENDBREPL,
  __module__ = 'rasmgr_client_service_pb2'
  # @@protoc_insertion_point(class_scope:rasnet.service.OpenDbRepl)
  ))
_sym_db.RegisterMessage(OpenDbRepl)

CloseDbReq = _reflection.GeneratedProtocolMessageType('CloseDbReq', (_message.Message,), dict(
  DESCRIPTOR = _CLOSEDBREQ,
  __module__ = 'rasmgr_client_service_pb2'
  # @@protoc_insertion_point(class_scope:rasnet.service.CloseDbReq)
  ))
_sym_db.RegisterMessage(CloseDbReq)

KeepAliveReq = _reflection.GeneratedProtocolMessageType('KeepAliveReq', (_message.Message,), dict(
  DESCRIPTOR = _KEEPALIVEREQ,
  __module__ = 'rasmgr_client_service_pb2'
  # @@protoc_insertion_point(class_scope:rasnet.service.KeepAliveReq)
  ))
_sym_db.RegisterMessage(KeepAliveReq)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033org.rasdaman.rasnet.service\200\001\000\210\001\000'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class RasMgrClientServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Connect = channel.unary_unary(
        '/rasnet.service.RasMgrClientService/Connect',
        request_serializer=ConnectReq.SerializeToString,
        response_deserializer=ConnectRepl.FromString,
        )
    self.Disconnect = channel.unary_unary(
        '/rasnet.service.RasMgrClientService/Disconnect',
        request_serializer=DisconnectReq.SerializeToString,
        response_deserializer=common__service__pb2.Void.FromString,
        )
    self.OpenDb = channel.unary_unary(
        '/rasnet.service.RasMgrClientService/OpenDb',
        request_serializer=OpenDbReq.SerializeToString,
        response_deserializer=OpenDbRepl.FromString,
        )
    self.CloseDb = channel.unary_unary(
        '/rasnet.service.RasMgrClientService/CloseDb',
        request_serializer=CloseDbReq.SerializeToString,
        response_deserializer=common__service__pb2.Void.FromString,
        )
    self.KeepAlive = channel.unary_unary(
        '/rasnet.service.RasMgrClientService/KeepAlive',
        request_serializer=KeepAliveReq.SerializeToString,
        response_deserializer=common__service__pb2.Void.FromString,
        )


class RasMgrClientServiceServicer(object):

  def Connect(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Disconnect(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def OpenDb(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CloseDb(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KeepAlive(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RasMgrClientServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Connect': grpc.unary_unary_rpc_method_handler(
          servicer.Connect,
          request_deserializer=ConnectReq.FromString,
          response_serializer=ConnectRepl.SerializeToString,
      ),
      'Disconnect': grpc.unary_unary_rpc_method_handler(
          servicer.Disconnect,
          request_deserializer=DisconnectReq.FromString,
          response_serializer=common__service__pb2.Void.SerializeToString,
      ),
      'OpenDb': grpc.unary_unary_rpc_method_handler(
          servicer.OpenDb,
          request_deserializer=OpenDbReq.FromString,
          response_serializer=OpenDbRepl.SerializeToString,
      ),
      'CloseDb': grpc.unary_unary_rpc_method_handler(
          servicer.CloseDb,
          request_deserializer=CloseDbReq.FromString,
          response_serializer=common__service__pb2.Void.SerializeToString,
      ),
      'KeepAlive': grpc.unary_unary_rpc_method_handler(
          servicer.KeepAlive,
          request_deserializer=KeepAliveReq.FromString,
          response_serializer=common__service__pb2.Void.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'rasnet.service.RasMgrClientService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaRasMgrClientServiceServicer(object):
  def Connect(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def Disconnect(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def OpenDb(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def CloseDb(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def KeepAlive(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaRasMgrClientServiceStub(object):
  def Connect(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Connect.future = None
  def Disconnect(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Disconnect.future = None
  def OpenDb(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  OpenDb.future = None
  def CloseDb(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  CloseDb.future = None
  def KeepAlive(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  KeepAlive.future = None


def beta_create_RasMgrClientService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('rasnet.service.RasMgrClientService', 'CloseDb'): CloseDbReq.FromString,
    ('rasnet.service.RasMgrClientService', 'Connect'): ConnectReq.FromString,
    ('rasnet.service.RasMgrClientService', 'Disconnect'): DisconnectReq.FromString,
    ('rasnet.service.RasMgrClientService', 'KeepAlive'): KeepAliveReq.FromString,
    ('rasnet.service.RasMgrClientService', 'OpenDb'): OpenDbReq.FromString,
  }
  response_serializers = {
    ('rasnet.service.RasMgrClientService', 'CloseDb'): common__service__pb2.Void.SerializeToString,
    ('rasnet.service.RasMgrClientService', 'Connect'): ConnectRepl.SerializeToString,
    ('rasnet.service.RasMgrClientService', 'Disconnect'): common__service__pb2.Void.SerializeToString,
    ('rasnet.service.RasMgrClientService', 'KeepAlive'): common__service__pb2.Void.SerializeToString,
    ('rasnet.service.RasMgrClientService', 'OpenDb'): OpenDbRepl.SerializeToString,
  }
  method_implementations = {
    ('rasnet.service.RasMgrClientService', 'CloseDb'): face_utilities.unary_unary_inline(servicer.CloseDb),
    ('rasnet.service.RasMgrClientService', 'Connect'): face_utilities.unary_unary_inline(servicer.Connect),
    ('rasnet.service.RasMgrClientService', 'Disconnect'): face_utilities.unary_unary_inline(servicer.Disconnect),
    ('rasnet.service.RasMgrClientService', 'KeepAlive'): face_utilities.unary_unary_inline(servicer.KeepAlive),
    ('rasnet.service.RasMgrClientService', 'OpenDb'): face_utilities.unary_unary_inline(servicer.OpenDb),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_RasMgrClientService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('rasnet.service.RasMgrClientService', 'CloseDb'): CloseDbReq.SerializeToString,
    ('rasnet.service.RasMgrClientService', 'Connect'): ConnectReq.SerializeToString,
    ('rasnet.service.RasMgrClientService', 'Disconnect'): DisconnectReq.SerializeToString,
    ('rasnet.service.RasMgrClientService', 'KeepAlive'): KeepAliveReq.SerializeToString,
    ('rasnet.service.RasMgrClientService', 'OpenDb'): OpenDbReq.SerializeToString,
  }
  response_deserializers = {
    ('rasnet.service.RasMgrClientService', 'CloseDb'): common__service__pb2.Void.FromString,
    ('rasnet.service.RasMgrClientService', 'Connect'): ConnectRepl.FromString,
    ('rasnet.service.RasMgrClientService', 'Disconnect'): common__service__pb2.Void.FromString,
    ('rasnet.service.RasMgrClientService', 'KeepAlive'): common__service__pb2.Void.FromString,
    ('rasnet.service.RasMgrClientService', 'OpenDb'): OpenDbRepl.FromString,
  }
  cardinalities = {
    'CloseDb': cardinality.Cardinality.UNARY_UNARY,
    'Connect': cardinality.Cardinality.UNARY_UNARY,
    'Disconnect': cardinality.Cardinality.UNARY_UNARY,
    'KeepAlive': cardinality.Cardinality.UNARY_UNARY,
    'OpenDb': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'rasnet.service.RasMgrClientService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
