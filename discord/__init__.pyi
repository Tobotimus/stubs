from .activity import *
from .channel import *
from .errors import *
from .enums import *
from .player import *
from .webhook import *
import logging
from .audit_logs import AuditLogChanges, AuditLogDiff, AuditLogEntry
from .calls import CallMessage, GroupCall
from .client import AppInfo, Client
from .colour import Color, Colour
from .embeds import Embed
from .emoji import Emoji, PartialEmoji
from .file import File
from .guild import Guild
from .invite import Invite
from .member import Member, VoiceState
from .message import Attachment, Message
from .object import Object
from .permissions import PermissionOverwrite, Permissions
from .reaction import Reaction
from .relationship import Relationship
from .role import Role
from .shard import AutoShardedClient
from .user import ClientUser, Profile, User
from .voice_client import VoiceClient
from collections import namedtuple
from typing import Any

__title__: str
__license__: str
__copyright__: str

VersionInfo = namedtuple("VersionInfo", "major minor micro releaselevel serial")
version_info: VersionInfo

class NullHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None: ...
