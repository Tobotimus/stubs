from typing import Any

class StringView:
    index: int = ...
    buffer: Any = ...
    end: Any = ...
    previous: int = ...
    def __init__(self, buffer: Any) -> None: ...
    @property
    def current(self): ...
    @property
    def eof(self): ...
    def undo(self) -> None: ...
    def skip_ws(self): ...
    def skip_string(self, string: Any): ...
    def read_rest(self): ...
    def read(self, n: Any): ...
    def get(self): ...
    def get_word(self): ...

def quoted_word(view: Any): ...
