# Stubs for discord.file (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class File:
    fp: Any = ...
    filename: Any = ...
    def __init__(self, fp: Any, filename: Optional[Any] = ...) -> None: ...
    def open_file(self): ...
    def close(self) -> None: ...
