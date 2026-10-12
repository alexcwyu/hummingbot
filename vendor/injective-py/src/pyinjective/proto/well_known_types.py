"""Construct standard protobuf messages in the Injective SDK descriptor pool."""
from types import SimpleNamespace

from google.protobuf import any_pb2 as _any_pb2, message_factory
from google.protobuf import timestamp_pb2 as _timestamp_pb2

from pyinjective.proto import descriptor_pool_compat


def _module(original, message_name):
    pool = descriptor_pool_compat.Default()
    pool._copy_dependency(original.DESCRIPTOR)
    descriptor = pool.FindMessageTypeByName("google.protobuf." + message_name)
    return SimpleNamespace(**{message_name: message_factory.GetMessageClass(descriptor)})


any_pb2 = _module(_any_pb2, "Any")
timestamp_pb2 = _module(_timestamp_pb2, "Timestamp")
