# Injective SDK compatibility source

Source: published `injective-py` 1.16.2 from [PyPI](https://pypi.org/project/injective-py/1.16.2/), [official repository](https://github.com/InjectiveLabs/sdk-python). The Apache-2.0 license and notice are retained verbatim. All SDK modules are retained.

```json
[
  {
    "filename": "injective_py-1.16.2-py3-none-any.whl",
    "sha256": "8aacf4e628cefb5091c701855ac64f0ec3e12b8c23bfe85b91d965edf9e2f9b3",
    "url": "https://files.pythonhosted.org/packages/d6/eb/0cfab54e116152ad021222c36e4d8067a6193c7735e54cfb64429511a26a/injective_py-1.16.2-py3-none-any.whl"
  },
  {
    "filename": "injective_py-1.16.2.tar.gz",
    "sha256": "3acf917d20316eeda150b023e573aed42ebf703b9b90929a5e8889c8e9714e8a",
    "url": "https://files.pythonhosted.org/packages/91/b2/0de53daf2522de3d4501ed5ef26fb8e9634f8aec6530be5714eb5a226368/injective_py-1.16.2.tar.gz"
  }
]
```

Changes: generated `_pb2.py` modules register their unchanged serialized schemas in a private Injective DescriptorPool. Standard Google descriptor dependencies are copied recursively through the public protobuf descriptor API. This permits the real Injective and dYdX Cosmos schema revisions to coexist without duplicate-filename collisions in the global pool. The 403 serialized schema payloads are byte-identical to the published wheel; schema fields, wire numbers, fully qualified message names and endpoint methods remain unchanged. Private-pool Any and Timestamp classes preserve those wire definitions while providing the class identity required by the SDK's private descriptors. JSON parsing and serialization explicitly use the same pool so nested Any types resolve against the correct Cosmos revision. The protobuf constraint permits the verified 6.x runtime needed by current dYdX generated code.

Imported Python files also normalize line endings and trailing whitespace. An AST comparison verifies unchanged executable constants and operations; only whitespace in standalone documentation strings is normalized. The full license and notice remain verbatim, and the serialized-schema comparison is repeated after formatting.
