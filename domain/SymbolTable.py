from domain.HashTable import HashTable


class SymbolTable:
    def __init__(self):
        self.index = 0
        self.identifiersTable = HashTable()
        self.constantsTable = HashTable()

    def add_identifier(self, identifier):
        if self.identifiersTable.find(identifier) != -1:
            return
        self.identifiersTable.insert(identifier, self.index)
        self.index += 1

    def add_constant(self, constant):
        if self.constantsTable.find(constant) != -1:
            return
        self.constantsTable.insert(constant, self.index)
        self.index += 1

    def find(self, token):
        pos = self.identifiersTable.find(token)
        if pos != -1:
            return pos

        pos = self.constantsTable.find(token)
        return pos

    def get_tables(self):
        return self.identifiersTable.get_table("IDENTIFIER", "ST_POS"), self.constantsTable.get_table("CONSTANT", "ST_POS")
