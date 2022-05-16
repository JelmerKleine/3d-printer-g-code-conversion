import math

new_file = open("test_3.nc","w")
with open('g-code.txt') as f:
    new_line = ""
    for line in f:
        stripped = line.split('S', 1)[0]
        stripped2 = stripped.replace("E","Q1=")
        stripped3 = stripped2.replace("G92","M01")
        filtered = stripped3.split('G28', 1)[0]
        filtered2 = filtered.split('M84', 1)[0]
        filtered3 = filtered2.split('S= ', 1)[0]
        doubleStripped = filtered3.split(';', 1)[0]
        lhs = doubleStripped.split('=')
        #print(doubleStripped)
        #print(lhs[0])
        if(len(lhs) == 2):
            #print("="+lhs[1])
            lhs2 = lhs[1].split('F')
            newLine = lhs[0]
            if(len(lhs2) == 2):
                #print("F" + lhs2[1])
                newLine = newLine + "=" + str(float(lhs2[0])/((math.pi*math.pow(1.75,2))/4)) + " F" + lhs2[1] #*100000
            else:
                newLine = newLine + "=" + str(float(lhs2[0])/((math.pi*math.pow(1.75,2))/4))
        else:
            newLine = lhs[0]

        print(newLine)
        #print(rhs)
        #print("hi")
        new_file.write(newLine  + "\n")
        #print(new_lind)