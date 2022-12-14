from domain.Grammar import Grammar
from domain.Parser import Parser


if __name__ == "__main__":
    gr = Grammar("res/g5.txt")
    # print("Non terminals: " + str(gr.non_terminals))
    # print("Terminals: " + str(gr.terminals))
    # print("Program: " + str(gr.program))
    if gr.cfg_check():
        for non_terminal in gr.non_terminals:
            print(str(non_terminal) + " -> " + str(gr.get_production(non_terminal)))

    # print(gr.cfg_check())
    pr = Parser(gr)
    pr.first()
    pr.follow()
    # print("\nFIRST")
    # for fs in pr.first():
    #     print(str(fs) + " -> " + str(pr.get_first_map()[fs]))
    # print("\nFOLLOW")
    # for fl in pr.follow():
    #     print(str(fl) + " -> " + str(pr.get_follow_map()[fl]))

    print()
    try:
        pr.parse_table()
    except Exception as e:
        print(e)
        exit()
    print(pr.get_parsing_table_as_string())
    print()

    # https://www.geeksforgeeks.org/compiler-design-ll1-parser-in-python/
    try:
        pr.parse_algorithm_start("a r k O", "parser_output.txt")
    except Exception as e:
        print(e)
