from domain.HashTable import HashTable

class SymbolTable:

    def __init__(self):
        self.index = 0
        self.identifiersTable = HashTable()
        self.constantsTable = HashTable()

    def add_identifier(self, identifier):
        self.identifiersTable.insert(identifier, self.index)
        self.index += 1

    def add_constant(self, constant):
        self.constantsTable.insert(constant, self.index)
        self.index += 1
