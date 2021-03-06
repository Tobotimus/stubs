# Stubs for discord.raw_models (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class RawMessageDeleteEvent:
    message_id: Any = ...
    channel_id: Any = ...
    guild_id: Any = ...
    def __init__(self, data: Any) -> None: ...

class RawBulkMessageDeleteEvent:
    message_ids: Any = ...
    channel_id: Any = ...
    guild_id: Any = ...
    def __init__(self, data: Any) -> None: ...

class RawMessageUpdateEvent:
    message_id: Any = ...
    data: Any = ...
    def __init__(self, data: Any) -> None: ...

class RawReactionActionEvent:
    message_id: Any = ...
    channel_id: Any = ...
    user_id: Any = ...
    emoji: Any = ...
    guild_id: Any = ...
    def __init__(self, data: Any, emoji: Any) -> None: ...

class RawReactionClearEvent:
    message_id: Any = ...
    channel_id: Any = ...
    guild_id: Any = ...
    def __init__(self, data: Any) -> None: ...
