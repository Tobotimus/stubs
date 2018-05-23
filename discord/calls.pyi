import datetime
from typing import Any, Optional, List
from .channel import GroupChannel
from .enums import VoiceRegion
from .member import VoiceState
from .message import Message
from .user import User

class CallMessage:
    message: "Message" = ...
    ended_timestamp: Optional[datetime.datetime] = ...
    participants: List["User"] = ...
    def __init__(self, message: "Message", **kwargs: Any) -> None: ...
    @property
    def call_ended(self) -> bool: ...
    @property
    def channel(self) -> "GroupChannel": ...
    @property
    def duration(self) -> datetime.timedelta: ...

class GroupCall:
    call: CallMessage = ...
    unavailable: bool = ...
    ringing: List["User"] = ...
    region: VoiceRegion = ...
    def __init__(self, **kwargs: Any) -> None: ...
    @property
    def connected(self) -> List["User"]: ...
    @property
    def channel(self) -> "GroupChannel": ...
    def voice_state_for(self, user: "User") -> VoiceState: ...
