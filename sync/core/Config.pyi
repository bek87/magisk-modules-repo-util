from pathlib import Path

from ..model import ConfigJson
from ..utils import Log


class Config(ConfigJson):
    _log: Log
    _root_folder: Path

    def __init__(self, root_folder: Path): ...
    def _check_values(self): ...
    @classmethod
    def get_json_folder(cls, root_folder: Path) -> Path: ...
    @classmethod
    def get_modules_folder(cls, root_folder: Path) -> Path: ...
    @classmethod
    def get_local_folder(cls, root_folder: Path) -> Path: ...
