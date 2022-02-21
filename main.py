with open('g-code.txt') as f:
    new_line = ""
    for line in f:
        for i in line:
            #if i =='e':
            new_line = new_line + i
        #print(line)
        print(new_line)