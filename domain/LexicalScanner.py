import re

class LexicalScanner:

    def __init__(self, file_name, token_file, symbol_table):
        self.file_name = file_name
        self.token_file = token_file
        self.symbol_table = symbol_table
        self.tokens = []
        self.delimiters = []
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
        print(self.delimiters)

    def parse_source_code(self):
        f = open(self.file_name, "r")
        split_program = []
        regex_expr = '|\\'.join(self.delimiters) + '|\n|\t'
        regex_expr = '(\\' + regex_expr + ')'
        for line in f:
            split_line = re.split(regex_expr, line)
            split_line = [item for item in split_line if item not in ['', ' ', '\n', '\t']]
            if split_line:
                split_program += split_line
        print(split_program)

    def generate_symbol_table(self):
        pass
