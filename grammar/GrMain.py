from domain.Grammar import Grammar


if __name__ == "__main__":
    gr = Grammar("res/g2.txt")
    print("Non terminals: " + str(gr.non_terminals))
    print("Terminals: " + str(gr.terminals))
    print("Program: " + str(gr.program))
    if gr.cfg_check():
        for non_terminal in gr.non_terminals:
            print(str(non_terminal) + " -> " + str(gr.get_production(non_terminal)))

    print(gr.cfg_check())
