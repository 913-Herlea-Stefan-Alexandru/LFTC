from grammar.domain.Parser import EPSILON


class Grammar:

    def __init__(self, file_name):
        self.file_name = file_name
        self.non_terminals, self.terminals, self.program, self.productions = self.read_grammar()
        self.productions_with_numbers = []
        self.create_numbered_productions()

    def create_numbered_productions(self):
        for production_key in self.productions:
            production_values = self.productions[production_key]

            for prod in production_values:
                self.productions_with_numbers.append((production_key, prod))

    def read_grammar(self):
        f = open(self.file_name, "r")
        gr = []
        for line in f:
            gr.append(line)
        f.close()
        non_terminals = gr[0].strip().split(" ")
        terminals = gr[1].strip().split(" ")
        program = gr[2].strip()
        productions_list = [t.strip() for t in gr[3:]]
        productions = {}
        for p in productions_list:
            pr = p.strip().split(":")
            key = pr[0]
            productions[key] = []
            dest = pr[1].split("|")
            for d in dest:
                productions[key].append(d.split(" "))
        return non_terminals, terminals, program, productions

    def get_production(self, non_terminal):
        return self.productions[non_terminal]

    def cfg_check(self):
        for symbol in self.productions:
            if symbol not in self.non_terminals:
                return False
            productions = self.productions[symbol]
            for production in productions:
                for elem in production:
                    if elem == EPSILON:
                        continue
                    if elem not in self.non_terminals and elem not in self.terminals:
                        return False
        return True
