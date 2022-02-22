new_file = open("test.txt","w")
with open('g-code.txt') as f:
    new_line = ""
    for line in f:
        stripped = line.split('E', 1)[0]
        doubleStripped = stripped.split(';', 1)[0]
        print(doubleStripped)
        new_file.write(doubleStripped)
        #print(new_line)