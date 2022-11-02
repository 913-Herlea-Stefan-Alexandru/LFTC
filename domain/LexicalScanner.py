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
            tear_split_line = []
            in_string = [False, ""]
            token = ""
            for item in split_line:
                if item in ["'", '"']:
                    if in_string[0]:
                        if item == in_string[1]:
                            in_string[0] = False
                            in_string[1] = ""
                    else:
                        in_string[0] = True
                        in_string[1] = item
                    token += item
                    if not in_string[0]:
                        tear_split_line.append(token)
                        token = ""
                elif not in_string[0]:
                    token = ""
                    if item not in ['', ' ', '\n', '\t']:
                        tear_split_line.append(item)
                else:
                    token += item
            split_line = tear_split_line
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
                if token in self.tokens:
                    self.pif.append([token, -1])
                    continue
                if re.findall(IDENTIFIER_FORMAT, token):
                    self.pif.append(["id", self.symbol_table.find_id(token)])
                    continue
                if re.findall(CONSTANT_FORMAT, token):
                    self.pif.append(["const", self.symbol_table.find_const(token)])

    def get_pif_table(self):
        header = ["TOKEN", "ST_POS"]
        return tabulate(self.pif, headers=header, tablefmt="grid")
