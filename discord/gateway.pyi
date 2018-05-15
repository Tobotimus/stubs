# Stubs for discord.gateway (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import threading
import websockets
from collections import namedtuple
from typing import Any, Optional

class ResumeWebSocket(Exception):
    shard_id: Any = ...
    def __init__(self, shard_id: Any) -> None: ...

EventListener = namedtuple('EventListener', 'predicate event result future')

class KeepAliveHandler(threading.Thread):
    ws: Any = ...
    interval: Any = ...
    daemon: bool = ...
    shard_id: Any = ...
    msg: str = ...
    heartbeat_timeout: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def run(self): ...
    def get_payload(self): ...
    def stop(self) -> None: ...
    def ack(self) -> None: ...

class VoiceKeepAliveHandler(KeepAliveHandler):
    msg: str = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_payload(self): ...

class DiscordWebSocket(websockets.client.WebSocketClientProtocol):
    DISPATCH: int = ...
    HEARTBEAT: int = ...
    IDENTIFY: int = ...
    PRESENCE: int = ...
    VOICE_STATE: int = ...
    VOICE_PING: int = ...
    RESUME: int = ...
    RECONNECT: int = ...
    REQUEST_MEMBERS: int = ...
    INVALIDATE_SESSION: int = ...
    HELLO: int = ...
    HEARTBEAT_ACK: int = ...
    GUILD_SYNC: int = ...
    max_size: Any = ...
    session_id: Any = ...
    sequence: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def from_client(cls, client: Any, *, shard_id: Optional[Any] = ..., session: Optional[Any] = ..., sequence: Optional[Any] = ..., resume: bool = ...): ...
    def wait_for(self, event: Any, predicate: Any, result: Optional[Any] = ...): ...
    def identify(self) -> None: ...
    def resume(self) -> None: ...
    def received_message(self, msg: Any): ...
    @property
    def latency(self): ...
    def poll_event(self) -> None: ...
    def send(self, data: Any) -> None: ...
    def send_as_json(self, data: Any) -> None: ...
    def change_presence(self, *, activity: Optional[Any] = ..., status: Optional[Any] = ..., afk: bool = ..., since: float = ...) -> None: ...
    def request_sync(self, guild_ids: Any) -> None: ...
    def voice_state(self, guild_id: Any, channel_id: Any, self_mute: bool = ..., self_deaf: bool = ...) -> None: ...
    def close_connection(self, *args: Any, **kwargs: Any) -> None: ...

class DiscordVoiceWebSocket(websockets.client.WebSocketClientProtocol):
    IDENTIFY: int = ...
    SELECT_PROTOCOL: int = ...
    READY: int = ...
    HEARTBEAT: int = ...
    SESSION_DESCRIPTION: int = ...
    SPEAKING: int = ...
    HEARTBEAT_ACK: int = ...
    RESUME: int = ...
    HELLO: int = ...
    INVALIDATE_SESSION: int = ...
    max_size: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def send_as_json(self, data: Any) -> None: ...
    def resume(self) -> None: ...
    def identify(self) -> None: ...
    @classmethod
    def from_client(cls, client: Any, *, resume: bool = ...): ...
    def select_protocol(self, ip: Any, port: Any) -> None: ...
    def speak(self, is_speaking: bool = ...) -> None: ...
    def received_message(self, msg: Any) -> None: ...
    def initial_connection(self, data: Any) -> None: ...
    def load_secret_key(self, data: Any) -> None: ...
    def poll_event(self) -> None: ...
    def close_connection(self, *args: Any, **kwargs: Any) -> None: ...
