#
# This file is part of rasdaman community.
#
# Rasdaman community is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Rasdaman community is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rasdaman community.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2003, 2004, 2005, 2006, 2007, 2008, 2009 Peter Baumann / rasdaman GmbH.
#
# For more information please see <http://www.rasdaman.org>
# or contact Peter Baumann via <baumann@rasdaman.com>.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rasmgr_client_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pb2
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_service_pb2 as common__service__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rasmgr_client_service.proto',
  package='rasnet.service',
  # syntax='proto3',
  serialized_pb=b'\n\x1brasmgr_client_service.proto\x12\x0erasnet.service\x1a\x14\x63ommon_service.proto\"*\n\x0e\x43lientIdentity\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\x12\n\n\x02id\x18\x02 \x01(\x05\"4\n\nConnectReq\x12\x10\n\x08userName\x18\x01 \x01(\t\x12\x14\n\x0cpasswordHash\x18\x02 \x01(\t\"M\n\x0b\x43onnectRepl\x12\x12\n\nclientUUID\x18\x01 \x01(\t\x12\x18\n\x10keepAliveTimeout\x18\x02 \x01(\x05\x12\x10\n\x08\x63lientId\x18\x03 \x01(\x05\"5\n\rDisconnectReq\x12\x12\n\nclientUUID\x18\x01 \x01(\t\x12\x10\n\x08\x63lientId\x18\x02 \x01(\x05\"G\n\tOpenDbReq\x12\x12\n\nclientUUID\x18\x01 \x01(\t\x12\x10\n\x08\x63lientId\x18\x02 \x01(\x05\x12\x14\n\x0c\x64\x61tabaseName\x18\x03 \x01(\t\"G\n\nOpenDbRepl\x12\x13\n\x0b\x64\x62SessionId\x18\x01 \x01(\t\x12\x16\n\x0eserverHostName\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\r\"G\n\nCloseDbReq\x12\x12\n\nclientUUID\x18\x01 \x01(\t\x12\x10\n\x08\x63lientId\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x62SessionId\x18\x03 \x01(\t\"4\n\x0cKeepAliveReq\x12\x12\n\nclientUUID\x18\x01 \x01(\t\x12\x10\n\x08\x63lientId\x18\x02 \x01(\x05\x32\xdb\x02\n\x13RasMgrClientService\x12\x42\n\x07\x43onnect\x12\x1a.rasnet.service.ConnectReq\x1a\x1b.rasnet.service.ConnectRepl\x12\x41\n\nDisconnect\x12\x1d.rasnet.service.DisconnectReq\x1a\x14.rasnet.service.Void\x12?\n\x06OpenDb\x12\x19.rasnet.service.OpenDbReq\x1a\x1a.rasnet.service.OpenDbRepl\x12;\n\x07\x43loseDb\x12\x1a.rasnet.service.CloseDbReq\x1a\x14.rasnet.service.Void\x12?\n\tKeepAlive\x12\x1c.rasnet.service.KeepAliveReq\x1a\x14.rasnet.service.VoidB#\n\x1borg.rasdaman.rasnet.service\x80\x01\x00\x88\x01\x00\x62\x06proto3'
  ,
  dependencies=[common__service__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CLIENTIDENTITY = _descriptor.Descriptor(
  name='ClientIdentity',
  full_name='rasnet.service.ClientIdentity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='rasnet.service.ClientIdentity.uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='rasnet.service.ClientIdentity.id', index=1,
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
  # syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=111,
)


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
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='passwordHash', full_name='rasnet.service.ConnectReq.passwordHash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  # syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=165,
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
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  # syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=244,
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
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  # syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=246,
  serialized_end=299,
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
      has_default_value=False, default_value=b"".decode('utf-8'),
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
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  # syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=301,
  serialized_end=372,
)


_OPENDBREPL = _descriptor.Descriptor(
  name='OpenDbRepl',
  full_name='rasnet.service.OpenDbRepl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbSessionId', full_name='rasnet.service.OpenDbRepl.dbSessionId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serverHostName', full_name='rasnet.service.OpenDbRepl.serverHostName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='rasnet.service.OpenDbRepl.port', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  # syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=374,
  serialized_end=445,
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
      has_default_value=False, default_value=b"".decode('utf-8'),
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
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  # syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=447,
  serialized_end=518,
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
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='rasnet.service.KeepAliveReq.clientId', index=1,
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
  # syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=520,
  serialized_end=572,
)

DESCRIPTOR.message_types_by_name['ClientIdentity'] = _CLIENTIDENTITY
DESCRIPTOR.message_types_by_name['ConnectReq'] = _CONNECTREQ
DESCRIPTOR.message_types_by_name['ConnectRepl'] = _CONNECTREPL
DESCRIPTOR.message_types_by_name['DisconnectReq'] = _DISCONNECTREQ
DESCRIPTOR.message_types_by_name['OpenDbReq'] = _OPENDBREQ
DESCRIPTOR.message_types_by_name['OpenDbRepl'] = _OPENDBREPL
DESCRIPTOR.message_types_by_name['CloseDbReq'] = _CLOSEDBREQ
DESCRIPTOR.message_types_by_name['KeepAliveReq'] = _KEEPALIVEREQ

ClientIdentity = _reflection.GeneratedProtocolMessageType('ClientIdentity', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTIDENTITY,
  __module__ = 'rasmgr_client_service_pb2'
  # @@protoc_insertion_point(class_scope:rasnet.service.ClientIdentity)
  ))
_sym_db.RegisterMessage(ClientIdentity)

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
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), b'\n\033org.rasdaman.rasnet.service\200\001\000\210\001\000')
import abc
from grpc.beta import implementations as beta_implementations
from grpc.early_adopter import implementations as early_adopter_implementations
from grpc.framework.alpha import utilities as alpha_utilities
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
class EarlyAdopterRasMgrClientServiceServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Connect(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Disconnect(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def OpenDb(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def CloseDb(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def KeepAlive(self, request, context):
    raise NotImplementedError()
class EarlyAdopterRasMgrClientServiceServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterRasMgrClientServiceStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Connect(self, request):
    raise NotImplementedError()
  Connect.async = None
  @abc.abstractmethod
  def Disconnect(self, request):
    raise NotImplementedError()
  Disconnect.async = None
  @abc.abstractmethod
  def OpenDb(self, request):
    raise NotImplementedError()
  OpenDb.async = None
  @abc.abstractmethod
  def CloseDb(self, request):
    raise NotImplementedError()
  CloseDb.async = None
  @abc.abstractmethod
  def KeepAlive(self, request):
    raise NotImplementedError()
  KeepAlive.async = None
def early_adopter_create_RasMgrClientService_server(servicer, port, private_key=None, certificate_chain=None):
  import rasmgr_client_service_pb2
  import common_service_pb2
  method_service_descriptions = {
    "CloseDb": alpha_utilities.unary_unary_service_description(
      servicer.CloseDb,
      rasmgr_client_service_pb2.CloseDbReq.FromString,
      common_service_pb2.Void.SerializeToString,
    ),
    "Connect": alpha_utilities.unary_unary_service_description(
      servicer.Connect,
      rasmgr_client_service_pb2.ConnectReq.FromString,
      rasmgr_client_service_pb2.ConnectRepl.SerializeToString,
    ),
    "Disconnect": alpha_utilities.unary_unary_service_description(
      servicer.Disconnect,
      rasmgr_client_service_pb2.DisconnectReq.FromString,
      common_service_pb2.Void.SerializeToString,
    ),
    "KeepAlive": alpha_utilities.unary_unary_service_description(
      servicer.KeepAlive,
      rasmgr_client_service_pb2.KeepAliveReq.FromString,
      common_service_pb2.Void.SerializeToString,
    ),
    "OpenDb": alpha_utilities.unary_unary_service_description(
      servicer.OpenDb,
      rasmgr_client_service_pb2.OpenDbReq.FromString,
      rasmgr_client_service_pb2.OpenDbRepl.SerializeToString,
    ),
  }
  return early_adopter_implementations.server("rasnet.service.RasMgrClientService", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_RasMgrClientService_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import rasmgr_client_service_pb2
  import common_service_pb2
  method_invocation_descriptions = {
    "CloseDb": alpha_utilities.unary_unary_invocation_description(
      rasmgr_client_service_pb2.CloseDbReq.SerializeToString,
      common_service_pb2.Void.FromString,
    ),
    "Connect": alpha_utilities.unary_unary_invocation_description(
      rasmgr_client_service_pb2.ConnectReq.SerializeToString,
      rasmgr_client_service_pb2.ConnectRepl.FromString,
    ),
    "Disconnect": alpha_utilities.unary_unary_invocation_description(
      rasmgr_client_service_pb2.DisconnectReq.SerializeToString,
      common_service_pb2.Void.FromString,
    ),
    "KeepAlive": alpha_utilities.unary_unary_invocation_description(
      rasmgr_client_service_pb2.KeepAliveReq.SerializeToString,
      common_service_pb2.Void.FromString,
    ),
    "OpenDb": alpha_utilities.unary_unary_invocation_description(
      rasmgr_client_service_pb2.OpenDbReq.SerializeToString,
      rasmgr_client_service_pb2.OpenDbRepl.FromString,
    ),
  }
  return early_adopter_implementations.stub("rasnet.service.RasMgrClientService", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)

class BetaRasMgrClientServiceServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Connect(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Disconnect(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def OpenDb(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def CloseDb(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def KeepAlive(self, request, context):
    raise NotImplementedError()

class BetaRasMgrClientServiceStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Connect(self, request, timeout):
    raise NotImplementedError()
  Connect.future = None
  @abc.abstractmethod
  def Disconnect(self, request, timeout):
    raise NotImplementedError()
  Disconnect.future = None
  @abc.abstractmethod
  def OpenDb(self, request, timeout):
    raise NotImplementedError()
  OpenDb.future = None
  @abc.abstractmethod
  def CloseDb(self, request, timeout):
    raise NotImplementedError()
  CloseDb.future = None
  @abc.abstractmethod
  def KeepAlive(self, request, timeout):
    raise NotImplementedError()
  KeepAlive.future = None

def beta_create_RasMgrClientService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import rasmgr_client_service_pb2
  import common_service_pb2
  request_deserializers = {
    ('rasnet.service.RasMgrClientService', 'CloseDb'): rasmgr_client_service_pb2.CloseDbReq.FromString,
    ('rasnet.service.RasMgrClientService', 'Connect'): rasmgr_client_service_pb2.ConnectReq.FromString,
    ('rasnet.service.RasMgrClientService', 'Disconnect'): rasmgr_client_service_pb2.DisconnectReq.FromString,
    ('rasnet.service.RasMgrClientService', 'KeepAlive'): rasmgr_client_service_pb2.KeepAliveReq.FromString,
    ('rasnet.service.RasMgrClientService', 'OpenDb'): rasmgr_client_service_pb2.OpenDbReq.FromString,
  }
  response_serializers = {
    ('rasnet.service.RasMgrClientService', 'CloseDb'): common_service_pb2.Void.SerializeToString,
    ('rasnet.service.RasMgrClientService', 'Connect'): rasmgr_client_service_pb2.ConnectRepl.SerializeToString,
    ('rasnet.service.RasMgrClientService', 'Disconnect'): common_service_pb2.Void.SerializeToString,
    ('rasnet.service.RasMgrClientService', 'KeepAlive'): common_service_pb2.Void.SerializeToString,
    ('rasnet.service.RasMgrClientService', 'OpenDb'): rasmgr_client_service_pb2.OpenDbRepl.SerializeToString,
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
  import rasmgr_client_service_pb2
  import common_service_pb2
  request_serializers = {
    ('rasnet.service.RasMgrClientService', 'CloseDb'): rasmgr_client_service_pb2.CloseDbReq.SerializeToString,
    ('rasnet.service.RasMgrClientService', 'Connect'): rasmgr_client_service_pb2.ConnectReq.SerializeToString,
    ('rasnet.service.RasMgrClientService', 'Disconnect'): rasmgr_client_service_pb2.DisconnectReq.SerializeToString,
    ('rasnet.service.RasMgrClientService', 'KeepAlive'): rasmgr_client_service_pb2.KeepAliveReq.SerializeToString,
    ('rasnet.service.RasMgrClientService', 'OpenDb'): rasmgr_client_service_pb2.OpenDbReq.SerializeToString,
  }
  response_deserializers = {
    ('rasnet.service.RasMgrClientService', 'CloseDb'): common_service_pb2.Void.FromString,
    ('rasnet.service.RasMgrClientService', 'Connect'): rasmgr_client_service_pb2.ConnectRepl.FromString,
    ('rasnet.service.RasMgrClientService', 'Disconnect'): common_service_pb2.Void.FromString,
    ('rasnet.service.RasMgrClientService', 'KeepAlive'): common_service_pb2.Void.FromString,
    ('rasnet.service.RasMgrClientService', 'OpenDb'): rasmgr_client_service_pb2.OpenDbRepl.FromString,
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