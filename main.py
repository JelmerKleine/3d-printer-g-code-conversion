new_file = open("test_2.txt","w")
with open('g-code.txt') as f:
    new_line = ""
    for line in f:
        stripped = line.split('S', 1)[0]
        filtered = stripped.replace("E","S=")
        doubleStripped = filtered.split(';', 1)[0]
        print(doubleStripped)
        print("hi")
        new_file.write(doubleStripped+ "\n")
        #print(new_lind)