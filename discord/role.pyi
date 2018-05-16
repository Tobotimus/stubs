# Stubs for discord.role (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .colour import Colour
from .mixins import Hashable
from .permissions import Permissions
from typing import Any, Optional

class Role(Hashable):
    guild: Any = ...
    id: int = ...
    def __init__(self, guild: Any, state: Any, data: Any) -> None: ...
    def __lt__(self, other: Any): ...
    def __le__(self, other: Any): ...
    def __gt__(self, other: Any): ...
    def __ge__(self, other: Any): ...
    def is_default(self): ...
    @property
    def created_at(self): ...
    @property
    def mention(self): ...
    @property
    def members(self): ...
    position: Any = ...
    def edit(self, *, reason: Optional[Any] = ..., **fields: Any) -> None: ...
    def delete(self, *, reason: Optional[Any] = ...) -> None: ...
