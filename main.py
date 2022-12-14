from domain.LexicalScanner import LexicalScanner
from domain.SymbolTable import SymbolTable
from fa.domain.Fa import Fa
from grammar.domain.Grammar import Grammar
from grammar.domain.Parser import Parser

if __name__ == "__main__":
    st = SymbolTable()
    scanner = LexicalScanner("res/input/src/p3.txt", "res/input/utils/token.in", st, Fa("res/input/fa/integer.in"), Fa(
        "res/input/fa/identifier.in"))

    try:
        scanner.generate_symbol_table()
        identifier_table, constants_table = st.get_tables()

        f = open("res/out/ST.out", "w")
        f.write("Using 2 hash tables (one for the identifiers and one for the constants)")
        f.write("\n\nIdentifier table: \n\n")
        f.write(identifier_table)
        f.write("\n\nConstants table: \n\n")
        f.write(constants_table)
        f.close()

        scanner.generate_pif()
        f = open("res/out/PIF.out", "w")
        f.write("PIF table: \n\n")
        f.write(scanner.get_pif_table())
    except Exception as e:
        f = open("res/out/ST.out", "w")
        f.write("")
        f.close()
        f = open("res/out/PIF.out", "w")
        f.write("")
        f.close()
        print(e)
        exit()

    gr = Grammar("grammar/res/g2.txt")
    if gr.cfg_check():
        for non_terminal in gr.non_terminals:
            print(str(non_terminal) + " -> " + str(gr.get_production(non_terminal)))
    pr = Parser(gr)
    pr.first()
    pr.follow()

    print()
    try:
        pr.parse_table()
    except Exception as e:
        print(e)
        exit()
    print(pr.get_parsing_table_as_string())
    print()

    sequence = " ".join([f[0] for f in scanner.pif])

    print(sequence)

    try:
        pr.parse_algorithm_start(sequence, "parser_output.txt")
    except Exception as e:
        print(e)
