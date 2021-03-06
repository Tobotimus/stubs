# Stubs for discord.activity (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import datetime
from typing import Any, Optional, Union, List, Dict
from .enums import ActivityType
from .colour import Colour

try:
    from mypy_extensions import TypedDict
except ImportError:
    TimeStampsDict = Dict[str, int]
    AssetsDict = Dict[str, str]
    PartyDict = Dict[str, Union[int, List[int]]]
else:
    TimeStampsDict = TypedDict(
        "TimeStampsDict", {"start": int, "end": int}, total=False
    )
    AssetsDict = TypedDict(
        "AssetsDict",
        {"large_image": str, "large_text": str, "small_image": str, "small_text": str},
        total=False,
    )
    PartyDict = TypedDict("PartyDict", {"id": int, "size": List[int]}, total=False)

__all__ = ("Activity", "Streaming", "Game", "Spotify")

class _ActivityTag: ...

class Activity(_ActivityTag):
    state: Optional[str] = ...
    details: Optional[str] = ...
    timestamps: TimeStampsDict = ...
    assets: AssetsDict = ...
    party: PartyDict = ...
    application_id: Optional[str] = ...
    name: Optional[str] = ...
    url: Optional[str] = ...
    flags: int = ...
    sync_id: Optional[str] = ...
    session_id: Optional[str] = ...
    type: ActivityType = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @property
    def start(self) -> Optional[datetime.datetime]: ...
    @property
    def end(self) -> Optional[datetime.datetime]: ...
    @property
    def large_image_url(self) -> Optional[str]: ...
    @property
    def small_image_url(self) -> Optional[str]: ...
    @property
    def large_image_text(self) -> Optional[str]: ...
    @property
    def small_image_text(self) -> Optional[str]: ...

class Game(_ActivityTag):
    name: str = ...
    def __init__(self, name: str, **extra: Any) -> None: ...
    @property
    def type(self) -> ActivityType: ...
    @property
    def start(self) -> Optional[datetime.datetime]: ...
    @property
    def end(self) -> Optional[datetime.datetime]: ...
    def to_dict(self) -> Dict[str, Any]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class Streaming(_ActivityTag):
    name: str = ...
    url: str = ...
    details: Optional[str] = ...
    assets: AssetsDict = ...
    def __init__(self, name: str, url: str, **extra: Any) -> None: ...
    @property
    def type(self) -> ActivityType: ...
    @property
    def twitch_name(self) -> Optional[str]: ...
    def to_dict(self) -> Dict[str, Any]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class Spotify:
    def __init__(self, **data: Any) -> None: ...
    @property
    def type(self) -> ActivityType: ...
    @property
    def colour(self) -> Colour: ...
    @property
    def color(self) -> Colour: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @property
    def name(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def title(self) -> str: ...
    @property
    def artists(self) -> List[str]: ...
    @property
    def artist(self) -> str: ...
    @property
    def album(self) -> str: ...
    @property
    def album_cover_url(self) -> str: ...
    @property
    def track_id(self) -> str: ...
    @property
    def start(self) -> datetime.datetime: ...
    @property
    def end(self) -> datetime.datetime: ...
    @property
    def duration(self) -> datetime.timedelta: ...
    @property
    def party_id(self) -> str: ...
