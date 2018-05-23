import datetime
from abc import ABCMeta, abstractmethod
from collections import namedtuple
from typing import Type, Any, Optional, Union, List, Tuple
from .channel import CategoryChannel
from .context_managers import Typing
from .embeds import Embed
from .file import File
from .guild import Guild
from .invite import Invite
from .iterators import HistoryIterator
from .member import Member
from .message import Message
from .permissions import PermissionOverwrite, Permissions
from .role import Role
from .voice_client import VoiceClient

_Overwriteable = Union[Role, "Member"]
_Occurrence = Union["Message", datetime.datetime]

class _Undefined: ...

class Snowflake(metaclass=ABCMeta):
    @property
    @abstractmethod
    def created_at(self) -> datetime.datetime: ...
    @classmethod
    def __subclasshook__(cls, C: Type[Any]) -> Union[bool, NotImplemented]: ...

class User(metaclass=ABCMeta):
    @property
    @abstractmethod
    def display_name(self) -> str: ...
    @property
    @abstractmethod
    def mention(self) -> str: ...
    @classmethod
    def __subclasshook__(cls, C: Type[Any]) -> Union[bool, NotImplemented]: ...

class PrivateChannel(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, C: Type[Any]) -> Union[bool, NotImplemented]: ...

_Overwrites = namedtuple("_Overwrites", "id allow deny type")

class GuildChannel:
    name: str = ...
    guild: "Guild" = ...
    position: int = ...
    @property
    def changed_roles(self) -> List[Role]: ...
    @property
    def mention(self) -> str: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    def overwrites_for(self, obj: Union[Role, User]) -> PermissionOverwrite: ...
    @property
    def overwrites(self) -> List[Tuple[_Overwriteable, PermissionOverwrite]]: ...
    @property
    def category(self) -> Optional["CategoryChannel"]: ...
    def permissions_for(self, member: "Member") -> Permissions: ...
    async def delete(self, *, reason: Optional[str] = ...) -> None: ...
    async def set_permissions(
        self,
        target: _Overwriteable,
        *,
        overwrite: PermissionOverwrite = ...,
        reason: Optional[str] = ...,
        **permissions: bool
    ) -> None: ...
    async def create_invite(
        self,
        *,
        reason: Optional[str] = ...,
        max_age: int = ...,
        max_uses: int = ...,
        temporary: bool = ...,
        unique: bool = ...
    ) -> Invite: ...
    async def invites(self) -> List[Invite]: ...

class Messageable(metaclass=ABCMeta):
    async def send(
        self,
        content: Optional[str] = ...,
        *,
        tts: bool = ...,
        embed: Optional["Embed"] = ...,
        file: Optional[File] = ...,
        files: Optional[List[File]] = ...,
        delete_after: Optional[float] = ...,
        nonce: Optional[int] = ...
    ) -> "Message": ...
    async def trigger_typing(self) -> None: ...
    async def typing(self) -> Typing: ...
    async def get_message(self, id: int) -> "Message": ...
    async def pins(self) -> List["Message"]: ...
    def history(
        self,
        *,
        limit: int = ...,
        before: Optional[_Occurrence] = ...,
        after: Optional[_Occurrence] = ...,
        around: Optional[_Occurrence] = ...,
        reverse: Optional[bool] = ...
    ) -> HistoryIterator: ...

class Connectable(metaclass=ABCMeta):
    async def connect(self, *, timeout: float = ..., reconnect: bool = ...) -> VoiceClient: ...
