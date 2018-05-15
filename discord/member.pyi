# Stubs for discord.member (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import discord.abc
from .activity import create_activity
from .colour import Colour
from .enums import Status, try_enum
from .object import Object
from .permissions import Permissions
from .user import BaseUser, User
from typing import Any, Optional

class VoiceState:
    session_id: Any = ...
    def __init__(self, data: Any, *, channel: Optional[Any] = ...) -> None: ...

def flatten_user(cls): ...

class Member(discord.abc.Messageable, _BaseUser):
    guild: Any = ...
    joined_at: Any = ...
    status: Any = ...
    activity: Any = ...
    nick: Any = ...
    def __init__(self, data: Any, guild: Any, state: Any) -> None: ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __hash__(self): ...
    @property
    def colour(self): ...
    color: Any = ...
    @property
    def mention(self): ...
    @property
    def display_name(self): ...
    def mentioned_in(self, message: Any): ...
    def permissions_in(self, channel: Any): ...
    @property
    def top_role(self): ...
    @property
    def guild_permissions(self): ...
    @property
    def voice(self): ...
    def ban(self, **kwargs: Any) -> None: ...
    def unban(self, *, reason: Optional[Any] = ...) -> None: ...
    def kick(self, *, reason: Optional[Any] = ...) -> None: ...
    def edit(self, *, reason: Optional[Any] = ..., **fields: Any) -> None: ...
    def move_to(self, channel: Any, *, reason: Optional[Any] = ...) -> None: ...
    def add_roles(self, *roles: Any, reason: Optional[Any] = ..., atomic: bool = ...) -> None: ...
    def remove_roles(self, *roles: Any, reason: Optional[Any] = ..., atomic: bool = ...) -> None: ...
