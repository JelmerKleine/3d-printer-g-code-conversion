new_file = open("test.txt","w")
with open('g-code.txt') as f:
    new_line = ""
    for line in f:
        filtered = line.replace("E","T")
        doubleStripped = filtered.split(';', 1)[0]
        print(doubleStripped)
        print("hi")
        new_file.write(doubleStripped+ "\n")
        #print(new_lind)