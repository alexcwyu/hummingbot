"""Keep Injective protobuf schemas separate from other Cosmos SDKs."""
from google.protobuf import descriptor_pb2, descriptor_pool


class _InjectivePool:
    def __init__(self):
        self._pool = descriptor_pool.DescriptorPool()

    def _copy_dependency(self, descriptor):
        try:
            return self._pool.FindFileByName(descriptor.name)
        except KeyError:
            for dependency in descriptor.dependencies:
                self._copy_dependency(dependency)
            return self._pool.AddSerializedFile(descriptor.serialized_pb)

    def AddSerializedFile(self, data):
        schema = descriptor_pb2.FileDescriptorProto.FromString(data)
        for dependency in schema.dependency:
            try:
                self._pool.FindFileByName(dependency)
            except KeyError:
                if not dependency.startswith("google/"):
                    raise
                self._copy_dependency(descriptor_pool.Default().FindFileByName(dependency))
        return self._pool.AddSerializedFile(data)

    def __getattr__(self, name):
        return getattr(self._pool, name)


_pool = _InjectivePool()


def Default():
    return _pool
