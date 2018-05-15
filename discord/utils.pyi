# Stubs for discord.utils (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .errors import InvalidArgument
from typing import Any, Optional

DISCORD_EPOCH: int

class cached_property:
    function: Any = ...
    __doc__: Any = ...
    def __init__(self, function: Any) -> None: ...
    def __get__(self, instance: Any, owner: Any): ...

class CachedSlotProperty:
    name: Any = ...
    function: Any = ...
    __doc__: Any = ...
    def __init__(self, name: Any, function: Any) -> None: ...
    def __get__(self, instance: Any, owner: Any): ...

def cached_slot_property(name: Any): ...
def parse_time(timestamp: Any): ...
def deprecated(instead: Optional[Any] = ...): ...
def oauth_url(client_id: Any, permissions: Optional[Any] = ..., guild: Optional[Any] = ..., redirect_uri: Optional[Any] = ...): ...
def snowflake_time(id: Any): ...
def time_snowflake(datetime_obj: Any, high: bool = ...): ...
def find(predicate: Any, seq: Any): ...
def get(iterable: Any, **attrs: Any): ...
def to_json(obj: Any): ...
def maybe_coroutine(f: Any, *args: Any, **kwargs: Any): ...
def async_all(gen: Any): ...
def sane_wait_for(futures: Any, timeout: Any, loop: Any) -> None: ...
def valid_icon_size(size: Any): ...
