from .enums import RelationshipType
from typing import Any

class Relationship:
    type: Any = ...
    user: Any = ...
    def __init__(self, state: Any, data: Any) -> None: ...
    def delete(self) -> None: ...
    def accept(self) -> None: ...
