from abc import ABC
from abc import abstractmethod


class TargetProcess(ABC):
    """
    テストしたい処理用クラス
    """

    def __init__(self):
        pass

    def exec_preprocess(self):
        pass

    def exec_main_process(self):
        pass
