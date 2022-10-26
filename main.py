from domain.LexicalScanner import LexicalScanner
from domain.SymbolTable import SymbolTable

if __name__ == "__main__":
    st = SymbolTable()
    scanner = LexicalScanner("res/src/p1.txt", "res/utils/token.in", st)

    scanner.parse_source_code()
