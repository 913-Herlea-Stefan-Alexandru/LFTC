
class Grammar:

    def __init__(self, file_name):
        self.file_name = file_name
        self.non_terminals, self.terminals, self.program, self.predictions = self.read_grammar()

    def read_grammar(self):
        f = open(self.file_name, "r")
        gr = []
        for line in f:
            gr.append(line)
        f.close()
        non_terminals = gr[0].strip().split(" ")
        terminals = gr[1].strip().split(" ")
        program = gr[2].strip()
        predictions_list = [t.strip() for t in gr[3:]]
        predictions = {}
        for p in predictions_list:
            pr = p.strip().split(" ")
            key = pr[0]
            predictions[key] = []
            for dest in pr[1:]:
                predictions[key].append(dest)
        return non_terminals, terminals, program, predictions

    def get_prediction(self, nominal):
        return self.predictions[nominal]
