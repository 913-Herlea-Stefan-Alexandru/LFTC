from domain.HashTable import HashTable


class SymbolTable:
    def __init__(self):
        self.id_index = 0
        self.const_index = 0
        self.identifiersTable = HashTable()
        self.constantsTable = HashTable()

    def add_identifier(self, identifier):
        if self.identifiersTable.find(identifier) != -1:
            return
        self.identifiersTable.insert(identifier, self.id_index)
        self.id_index += 1

    def add_constant(self, constant):
        if self.constantsTable.find(constant) != -1:
            return
        self.constantsTable.insert(constant, self.const_index)
        self.const_index += 1

    def find_id(self, token):
        return self.identifiersTable.find(token)

    def find_const(self, token):
        return self.constantsTable.find(token)

    def get_tables(self):
        return self.identifiersTable.get_table("IDENTIFIER", "ST_POS"), self.constantsTable.get_table("CONSTANT", "ST_POS")
