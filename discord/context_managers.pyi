# Stubs for discord.context_managers (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .compat import create_task
from typing import Any

class Typing:
    loop: Any = ...
    messageable: Any = ...
    def __init__(self, messageable: Any) -> None: ...
    def do_typing(self) -> None: ...
    task: Any = ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None: ...
    def __aenter__(self): ...
    def __aexit__(self, exc_type: Any, exc: Any, tb: Any) -> None: ...
