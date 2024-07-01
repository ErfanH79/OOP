with open('schema.txt', 'r') as reader:
    line = reader.readlines()

while ("\n" in line):

    a = []

    for i in line:
        if (i == "\n"):
            line = line[line.index(i) + 1:]
            break
        else:
            a.append(i)

    table = str(a[0][:-1]) + ".txt"
    a = a[1:]
    n = str()
    for i in a:
        m = i.split(" ")[0]
        n = n + m + "  "
    with open(table, 'w') as writer:
        writer.write(n + "\n")
        writer.close()

if (len(line) != 0):

    a = line
    table = str(a[0][:-1]) + ".txt"
    a = a[1:]
    n = str()
    for i in a:
        m = i.split(" ")[0]
        n = n + m + "  "
    with open(table, 'w') as writer:
        writer.write(n + "\n")
        writer.close()
