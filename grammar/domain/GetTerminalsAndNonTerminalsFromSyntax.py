
if __name__ == "__main__":
    f = open("D:\\Formal Languages\\L2\\Project\\grammar\\res\\g2.txt", "r")
    o = open("D:\\Formal Languages\\L2\\Project\\grammar\\res\\terminals_non-terminals.txt", "a")
    n = []
    for line in f:
        nt = line.strip().split(":")[0]
        n.append(nt.strip())
    o.write(" ".join(n) + "\n")
    f.close()

    f = open("D:\\Formal Languages\\L2\\Project\\grammar\\res\\g2.txt", "r")
    stuff = []
    for line in f:
        rs = line.strip().split(":")[1].split("|")
        for r in rs:
            stuff.append(r.split(" "))

    stuff = [i for item in stuff for i in item if i.strip() not in n]
    stuff = set(stuff)
    o.write(" ".join(stuff))
    f.close()
    o.close()
