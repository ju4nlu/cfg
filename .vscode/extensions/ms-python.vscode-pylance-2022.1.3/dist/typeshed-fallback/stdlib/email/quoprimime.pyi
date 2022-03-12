def header_check(octet: int) -> bool: ...
def body_check(octet: int) -> bool: ...
def header_length(bytearray: bytes) -> int: ...
def body_length(bytearray: bytes) -> int: ...
def unquote(s: str | bytes) -> str: ...
def quote(c: str | bytes) -> str: ...
def header_encode(header_bytes: bytes, charset: str = ...) -> str: ...
def body_encode(body: str, maxlinelen: int = ..., eol: str = ...) -> str: ...
def decode(encoded: str, eol: str = ...) -> str: ...
def header_decode(s: str) -> str: ...

body_decode = decode
decodestring = decode
