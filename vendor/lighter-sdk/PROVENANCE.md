# Lighter SDK WebSocket compatibility

The Apache-2.0 licensed [official Lighter SDK](https://github.com/elliottech/lighter-python) source is copied from the published `lighter-sdk` 1.1.6 wheel, resolved on 2026-10-12. The complete package and its unchanged signer libraries for macOS, Linux and Windows are retained, preserving supported deployment platforms.

The only runtime source edit replaces deprecated `websockets.client.connect` with the public `websockets.asyncio.client.connect`. The SDK calls it with only its URL, supported by both APIs. Message processing, signing and HTTP operations remain unchanged. Local metadata removes the obsolete urllib3 upper bound to use the host's latest compatible release. No warning filters, test skips or assertions are changed. Remove this compatibility source when the published SDK adopts the current API.

Imported Python files also normalize line endings and trailing whitespace. An AST comparison verifies unchanged executable constants and operations; only whitespace in standalone documentation strings is normalized. The complete license and platform signer binaries remain byte-for-byte unchanged.
