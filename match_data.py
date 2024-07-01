class model:

    def select(table,a,b):
        with open(f'{table}.txt', 'r') as reader:
            lines = reader.readlines()
            for i in lines:
                line = i.split("  ")
                if (a == line[0] and b == line[2]):
                    return line
                else:
                    return 0

    def insert(table, newline):
        with open(f'{table}.txt', 'r') as reader:
            files = reader.readlines()
            with open(f'{table}.txt', 'a') as writer:
                writer.write(str(len(files))+")"+"  "+newline)

    def delete(table, id):
        with open(f'{table}.txt', 'r') as reader:
            lines = reader.readlines()
            with open(f'{table}.txt', 'w') as writer:
                writer.write(lines[0])
                for i in lines[1:]:
                    line = i.split("  ")
                    if (id != line[1]):
                        writer.write(i)
        model.sort(table)

    def update(table, id, newline):
        model.sort(table)
        with open(f'{table}.txt', 'r') as reader:
            lines = reader.readlines()
            with open(f'{table}.txt', 'w') as writer:
                for i in lines:
                    line = i.split("  ")
                    if (id == line[1]):
                        writer.write(str(line[0])+"  "+newline)
                    else:
                        writer.write(i)
        
    def update1(table, id, newline):
        model.sort(table)
        with open(f'{table}.txt', 'r') as reader:
            lines = reader.readlines()
            with open(f'{table}.txt', 'w') as writer:
                for i in lines:
                    line = i.split("  ")
                    if (id == line[2]):
                        writer.write(str(line[0])+"  "+newline)
                    else:
                        writer.write(i)
       
    def sort(table):
        j=1
        with open(f'{table}.txt', 'r') as reader:
            lines = reader.readlines()
            for i in lines:
                if len(i) == 1 or len(i) == 0:
                    lines.remove(i)
            with open(f'{table}.txt', 'w') as writer:
                writer.write(lines[0])
                for i in lines[1:]:
                    l = i.split("  ")
                    f ="  "
                    for k in l[1:]:
                        f+= k +"  "
                    H = str(j)+')'+f
                    writer.write(H[:-2])
                    j+=1
