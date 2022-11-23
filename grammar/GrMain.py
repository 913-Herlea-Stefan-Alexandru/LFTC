from domain.Grammar import Grammar


if __name__ == "__main__":
    gr = Grammar("res/g1.txt")
    print("Non terminals: " + str(gr.non_terminals))
    print("Terminals: " + str(gr.terminals))
    print("Program: " + str(gr.program))
    for non_terminal in gr.non_terminals:
        print(str(non_terminal) + " -> " + str(gr.get_prediction(non_terminal)))
