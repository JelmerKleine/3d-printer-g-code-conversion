import math

new_file = open("test_4.nc", "w")
with open('g-code.txt') as f:
    new_line = ""
    segment = 0
    for line in f:
        stripped = line.split('S', 1)[0]
        stripped2 = stripped.replace("E","H=")
        stripped3 = stripped2.replace("G92","MO1")
        filtered = stripped3.split('G28', 1)[0]
        filtered2 = filtered.split('M84', 1)[0]
        filtered3 = filtered2.split('S= ', 1)[0]
        filtered4 = filtered3.split('M140', 1)[0]
        filtered5 = filtered4.split('M105', 1)[0]
        filtered6 = filtered5.split('M190', 1)[0]
        filtered7 = filtered6.split('M104', 1)[0]
        filtered8 = filtered7.split('M109', 1)[0]
        filtered9 = filtered8.split('M107', 1)[0]
        filtered10 = filtered9.split('M82', 1)[0]
        filtered11 = filtered10.split('G90', 1)[0]
        filtered12 = filtered11.split('G91', 1)[0]
        filtered13 = filtered12.split('M106', 1)[0]
        doubleStripped = filtered13.split(';', 1)[0]
        lhs = doubleStripped.split('=')
        #print(doubleStripped)
        #print(lhs[0])

        if(len(lhs) == 2):
            #print("="+lhs[1])
            lhs2 = lhs[1].split('F')
            newLine = lhs[0]
            if(len(lhs2) == 2):
                #print("F" + lhs2[1])
                newLine = newLine + "=" + str(float(lhs2[0])) + " F" + lhs2[1] #/((math.pi*math.pow(1.75,2))/4)
            else:
                newLine = newLine + "=" + str(float(lhs2[0])) #/((math.pi*math.pow(1.75,2))/4)
        else:
            newLine = lhs[0]

        if (newLine.find("M") != -1):
            segment = segment + 1
            print("test")


        new_file.write(newLine + "\n")

        #print(rhs)
        #print("hi")
        #if segment == 1 :
            #new_file.write(newLine  + "\n")
       # if segment == 2:
            #new_file_2.write(newLine + "\n")
       # else:
            #print(newLine)
        #print(new_lind)