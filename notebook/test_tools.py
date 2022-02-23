import time
import pandas as pd


class TestExecutor(object):
    """
    テスト実行クラス

    Examples
    --------
    >>> from test_tools import TestExecutor
    >>> test_executor = TestExecutor(n_trails=1000)
    >>> result_dict = test_executor.exec_test(f=target_func, filepath_list=['test_data/test_file.txt'])
    """

    def __init__(self, n_trails):
        """
        コンストラクタ

        Parameters
        ----------
        n_trails : int
            試行回数
        """
        self.n_trails = n_trails

    def __measure_process_time(self, f, filepath):
        """
        メイン処理の処理時間計測を行うメソッド

        Parameters
        ----------
        f : function
            計測したい関数
        filepath : str
            ファイルパス

        Returns
        -------
        process_time_list : list
            計測結果リスト
        """
        process_time_list = []
        for _ in range(self.n_trails):
            start_time = time.process_time()
            f(filepath)
            end_time = time.process_time()
            process_time_list.append(end_time - start_time)
        return process_time_list

    def exec_test(self, f, filepath_list):
        """
        テスト実行メソッド

        Parameters
        ----------
        f : function
            計測したい関数
        filepath_list : list
            計測したいファイルパスのリスト

        Returns
        -------
        _ : dict
            テスト結果
        """
        return {filepath: self.__measure_process_time(f, filepath) for filepath in filepath_list}

    def show_result(self, result_dict):
        """
        テスト結果を表示するメソッド

        Parameters
        ----------
        result_dict : dict
            テスト結果
        """
        result_df = pd.DataFrame(result_dict)
        return result_df.describe()
