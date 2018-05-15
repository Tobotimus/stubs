# Stubs for discord.relationship (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .enums import RelationshipType, try_enum
from typing import Any

class Relationship:
    type: Any = ...
    user: Any = ...
    def __init__(self, state: Any, data: Any) -> None: ...
    def delete(self) -> None: ...
    def accept(self) -> None: ...
