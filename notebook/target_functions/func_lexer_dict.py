from rich.syntax import Syntax
from .template import TargetProcess

from pathlib import PurePath
from pygments.lexers import get_all_lexers


class TPLexerDict(TargetProcess):
    def __init__(self):
        self.lexer_wc_dict, self.lexer_const_dict = self.__generate_lexer_dict()

    def exec_main_process(self, filepath):
        _ = Syntax(self.__read_file(filepath), self.__infer_filetype(filepath))

    def __read_file(self, filepath):
        with open(filepath, 'r') as f:
            return f.read()

    def __infer_filetype(self, filepath):
        filename = PurePath(filepath).name
        filetype = PurePath(filepath).suffix[1:]
        if filename in self.lexer_const_dict:
            return self.lexer_const_dict[filename]
        elif filetype in self.lexer_wc_dict:
            return self.lexer_wc_dict[filetype]
        else:
            return 'auto'

    def __generate_lexer_dict(self):
        """
        The fFunction generate lexer dict


        Returns
        -------
        dic_lexer_wc : dict
            Lexers with wildcard.
            - structure: {extension: alias}
        dic_lexer_const : dict
            Lexers which is constant filename.
            - structure: {filename: alias}

        See Also
        --------
        - pygments.lexers.get_all_lexers
            - https://github.com/pygments/pygments/blob/master/pygments/lexers/__init__.py
        - pygments.lexers._mapping.LEXERS
            - https://github.com/pygments/pygments/blob/master/pygments/lexers/_mapping.py
        """
        # Generate lexer list[name, aliases, filenames, mimetypes]
        lst_lexer = [[lexer[0], lexer[1], filenames, lexer[3]] for lexer in get_all_lexers() for filenames in lexer[2]]
        # Split lexer list into extensions with wildcard and const filename
        lst_lexer_wc = [lexer for lexer in lst_lexer if '*.' in lexer[2]]
        lst_lexer_const = [lexer for lexer in lst_lexer if '*.' not in lexer[2]]
        # Generate lexer dict{ext: alias}
        dic_lexer_wc = dict(zip(
            [lexer[2].replace('*.', '') for lexer in lst_lexer_wc],
            [lexer[1][0] for lexer in lst_lexer_wc]
        ))
        dic_lexer_const = dict(zip(
            [lexer[2] for lexer in lst_lexer_const],
            [lexer[1][0] for lexer in lst_lexer_const]
        ))
        return dic_lexer_wc, dic_lexer_const
