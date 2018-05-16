# Stubs for discord.voice_client (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .gateway import *
from .backoff import ExponentialBackoff
from .player import AudioPlayer, AudioSource
from typing import Any, Optional

log: Any
has_nacl: bool

class VoiceClient:
    channel: Any = ...
    main_ws: Any = ...
    timeout: Any = ...
    ws: Any = ...
    socket: Any = ...
    loop: Any = ...
    sequence: int = ...
    timestamp: int = ...
    encoder: Any = ...
    def __init__(self, state: Any, timeout: Any, channel: Any) -> None: ...
    warn_nacl: Any = ...
    @property
    def guild(self): ...
    @property
    def user(self): ...
    def checked_add(self, attr: Any, value: Any, limit: Any) -> None: ...
    def start_handshake(self) -> None: ...
    def terminate_handshake(self, *, remove: bool = ...) -> None: ...
    def connect(
        self, *, reconnect: bool = ..., _tries: int = ..., do_handshake: bool = ...
    ) -> None: ...
    def poll_voice_ws(self, reconnect: Any) -> None: ...
    def disconnect(self, *, force: bool = ...): ...
    def move_to(self, channel: Any) -> None: ...
    def is_connected(self): ...
    def play(self, source: Any, *, after: Optional[Any] = ...) -> None: ...
    def is_playing(self): ...
    def is_paused(self): ...
    def stop(self) -> None: ...
    def pause(self) -> None: ...
    def resume(self) -> None: ...
    @property
    def source(self): ...
    @source.setter
    def source(self, value: Any) -> None: ...
    def send_audio_packet(self, data: Any, *, encode: bool = ...) -> None: ...
