import re
from Constants import IDENTIFIER_FORMAT, CONSTANT_FORMAT
from tabulate import tabulate


class LexicalScanner:
    def __init__(self, file_name, token_file, symbol_table):
        self.file_name = file_name
        self.token_file = token_file
        self.symbol_table = symbol_table
        self.pif = []
        self.tokens = []
        self.delimiters = []
        self.split_program = []
        self.generate_tokens()
        self.get_delimiters_from_tokens()

    def generate_tokens(self):
        f = open(self.token_file, "r")
        for line in f:
            self.tokens.append(line[:-1])
        f.close()
        self.tokens.append(' ')

    def get_delimiters_from_tokens(self):
        for t in self.tokens:
            if re.findall(r'\b([a-zA-z]+\b)', t) == []:
                self.delimiters.append(t)

    def parse_source_code(self):
        f = open(self.file_name, "r")
        self.split_program = []
        regex_expr = '|\\'.join(self.delimiters) + '|\n|\t'
        regex_expr = '(\\' + regex_expr + ')'
        for line in f:
            split_line = re.split(regex_expr, line)
            split_line = [item for item in split_line if item not in ['', ' ', '\n', '\t']]
            if split_line:
                self.split_program.append(split_line)

    def check_for_errors(self):
        for line in range(len(self.split_program)):
            for token in self.split_program[line]:
                if token in self.tokens:
                    continue
                if re.findall(IDENTIFIER_FORMAT, token):
                    continue
                if re.findall(CONSTANT_FORMAT, token):
                    continue
                raise Exception("Lexical error on line " + str(line + 1) + "; token: " + token)
        print("Lexically correct")

    def generate_symbol_table(self):
        self.parse_source_code()
        self.check_for_errors()

        for line in self.split_program:
            for token in line:
                if token in self.tokens:
                    continue
                if re.findall(IDENTIFIER_FORMAT, token):
                    self.symbol_table.add_identifier(token)
                    continue
                if re.findall(CONSTANT_FORMAT, token):
                    self.symbol_table.add_constant(token)

    def generate_pif(self):
        self.pif = []
        for line in self.split_program:
            for token in line:
                pos = self.symbol_table.find(token)
                if token in self.tokens:
                    self.pif.append([token, pos])
                    continue
                if re.findall(IDENTIFIER_FORMAT, token):
                    self.pif.append(["id", pos])
                    continue
                if re.findall(CONSTANT_FORMAT, token):
                    self.pif.append(["const", pos])

    def get_pif_table(self):
        header = ["TOKEN", "ST_POS"]
        return tabulate(self.pif, headers=header, tablefmt="grid")