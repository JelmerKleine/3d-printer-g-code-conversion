new_file = open("test.txt","w")
with open('g-code.txt') as f:
    new_line = ""
    for line in f:
        stripped = line.split('S', 1)[0]
        filtered = stripped.replace("E","S=")
        filtered2 = filtered.split('G92 ', 1)[0]
        filtered3 = filtered2.split('G28 ', 1)[0]
        filtered4 = filtered3.split('M84', 1)[0]
        filtered5 = filtered4.split('S= ', 1)[0]
        doubleStripped = filtered5.split(';', 1)[0]
        lhs = doubleStripped.split('=')
        #print(doubleStripped)
        #print(lhs[0])
        if(len(lhs) == 2):
            #print("="+lhs[1])
            lhs2 = lhs[1].split('F')
            newLine = lhs[0]
            if(len(lhs2) == 2):
                #print("F" + lhs2[1])
                newLine = newLine + "=" + str(float(lhs2[0])*100000) + " F" + lhs2[1]
            else:
                newLine = newLine + "=" + str(float(lhs2[0])*100000)
        else:
            newLine = lhs[0]

        print(newLine)
        #print(rhs)
        #print("hi")
        new_file.write(newLine  + "\n")
        #print(new_lind)