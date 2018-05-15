# Stubs for discord.invite (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .mixins import Hashable
from .object import Object
from .utils import parse_time
from typing import Any, Optional

class Invite(Hashable):
    max_age: Any = ...
    code: Any = ...
    guild: Any = ...
    revoked: Any = ...
    created_at: Any = ...
    temporary: Any = ...
    uses: Any = ...
    max_uses: Any = ...
    inviter: Any = ...
    channel: Any = ...
    def __init__(self, state: Any, data: Any) -> None: ...
    @classmethod
    def from_incomplete(cls, state: Any, data: Any): ...
    def __hash__(self): ...
    @property
    def id(self): ...
    @property
    def url(self): ...
    def delete(self, *, reason: Optional[Any] = ...) -> None: ...