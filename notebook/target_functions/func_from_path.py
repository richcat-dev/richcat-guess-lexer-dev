from rich.syntax import Syntax
from .template import TargetProcess


class TPFromPath(TargetProcess):
    def exec_main_process(self, filepath):
        _ = Syntax.from_path(filepath)
