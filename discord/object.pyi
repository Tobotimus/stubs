# Stubs for discord.object (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .mixins import Hashable
from typing import Any

class Object(Hashable):
    id: Any = ...
    def __init__(self, id: Any) -> None: ...
    @property
    def created_at(self): ...
