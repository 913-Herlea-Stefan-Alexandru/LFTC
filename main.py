from HashTable import HashTable

if __name__ == "__main__":
    identifierTable = HashTable()
    constantTable = HashTable()

    identifierTable.insert("a", "1")
    identifierTable.insert("b", "2")
    try:
        identifierTable.insert("b", "3")
    except Exception as e:
        print(e)

    constantTable.insert("abcd", "abcd")
    constantTable.insert("asfaf", "dafdafafd")

    print(identifierTable.find("a"))
    print(identifierTable.find("b"))
    print(identifierTable.find("n"))

    print(constantTable.find("abcd"))
    print(constantTable.find("asfaf"))
    print(constantTable.find("1"))
