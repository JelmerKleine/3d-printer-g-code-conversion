with open('g-code.txt') as f:
    new_line = ""
    for line in f:
        stripped = line.split('E', 1)[0]
        doubleStripped = stripped.split(';', 1)[0]
        print(doubleStripped)
        #print(new_line)