from typing import Any
from xml.sax.expatreader import ExpatParser as _ExpatParser

from django.core.serializers import base as base

class Serializer(base.Serializer):
    def indent(self, level: Any) -> None: ...
    xml: Any = ...
    def start_serialization(self) -> None: ...
    def end_serialization(self) -> None: ...
    def start_object(self, obj: Any) -> None: ...
    def end_object(self, obj: Any) -> None: ...
    def handle_field(self, obj: Any, field: Any) -> None: ...
    def handle_fk_field(self, obj: Any, field: Any) -> None: ...
    def handle_m2m_field(self, obj: Any, field: Any) -> None: ...

class Deserializer(base.Deserializer):
    handle_forward_references: Any = ...
    event_stream: Any = ...
    db: Any = ...
    ignore: Any = ...
    def __init__(
        self, stream_or_string: Any, *, using: Any = ..., ignorenonexistent: bool = ..., **options: Any
    ) -> None: ...
    def __next__(self): ...

def getInnerText(node: Any): ...

class DefusedExpatParser(_ExpatParser):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def start_doctype_decl(self, name: Any, sysid: Any, pubid: Any, has_internal_subset: Any) -> None: ...
    def entity_decl(
        self, name: Any, is_parameter_entity: Any, value: Any, base: Any, sysid: Any, pubid: Any, notation_name: Any
    ) -> None: ...
    def unparsed_entity_decl(self, name: Any, base: Any, sysid: Any, pubid: Any, notation_name: Any) -> None: ...
    def external_entity_ref_handler(self, context: Any, base: Any, sysid: Any, pubid: Any) -> None: ...
    def reset(self) -> None: ...

class DefusedXmlException(ValueError): ...

class DTDForbidden(DefusedXmlException):
    name: Any = ...
    sysid: Any = ...
    pubid: Any = ...
    def __init__(self, name: Any, sysid: Any, pubid: Any) -> None: ...

class EntitiesForbidden(DefusedXmlException):
    name: Any = ...
    value: Any = ...
    base: Any = ...
    sysid: Any = ...
    pubid: Any = ...
    notation_name: Any = ...
    def __init__(self, name: Any, value: Any, base: Any, sysid: Any, pubid: Any, notation_name: Any) -> None: ...

class ExternalReferenceForbidden(DefusedXmlException):
    context: Any = ...
    base: Any = ...
    sysid: Any = ...
    pubid: Any = ...
    def __init__(self, context: Any, base: Any, sysid: Any, pubid: Any) -> None: ...
