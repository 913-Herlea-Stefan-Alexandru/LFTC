from domain.LexicalScanner import LexicalScanner
from domain.SymbolTable import SymbolTable

if __name__ == "__main__":
    st = SymbolTable()
    scanner = LexicalScanner("res/input/src/p3.txt", "res/input/utils/token.in", st)

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
        print(e)
