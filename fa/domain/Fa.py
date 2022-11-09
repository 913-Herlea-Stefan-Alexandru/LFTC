
class Fa:
    def __init__(self, file_name):
        self.file = file_name
        self.states, self.alphabet, self.start, self.end, self.transitions = self.generate_fa()

    def generate_fa(self):
        f = open(self.file, "r")
        fa = []
        for line in f:
            fa.append(line)
        f.close()
        states = fa[0].strip()
        transitions_list = [t.strip() for t in fa[4:]]
        transitions = {}
        for state in states:
            transitions[state] = {}
            for dest_state in states:
                transitions[state][dest_state] = ""

        for transition in transitions_list:
            start = transition[0]
            end = transition[-1]
            transitions[start][end] = transition[1:-1]

        return states, fa[1].strip(), fa[2].strip(), fa[3].strip(), transitions

    def verify_sequence(self, sequence):
        current_state = self.start

        for ch in sequence:
            found = False
            for next_state in self.transitions[current_state]:
                if ch in self.transitions[current_state][next_state]:
                    current_state = next_state
                    found = True
                    break
            if not found:
                return False

        if current_state not in self.end:
            return False

        return True

    def get_states(self):
        return self.states

    def get_alphabet(self):
        return self.alphabet

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_transitions(self):
        return self.transitions
