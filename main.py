import math

new_file = open("leveling.nc", "w")
with open('CE6_20x20.gcode') as f:
    new_line = ""
    segment = 0

    for line in f: # for each line in file f
        # filtering lines that twincat doesn't recognize or replacing them
        stripped = line.split('S', 1)[0] # not neccesary
        stripped2 = stripped.replace("E","H=")  # replacing E with H=
        stripped3 = stripped2.replace("G92","M01") # replacing G92 with M01
        filtered = stripped3.split('G28', 1)[0]
        filtered2 = filtered.split('M82', 1)[0]
        filtered3 = filtered2.split('S= ', 1)[0]
        filtered4 = filtered3.split('M140', 1)[0]
        filtered5 = filtered4.split('M105', 1)[0]
        filtered6 = filtered5.split('M190', 1)[0]
        filtered7 = filtered6.split('M104', 1)[0]
        filtered8 = filtered7.split('M109', 1)[0]
        filtered9 = filtered8.split('M107', 1)[0]
        filtered10 = filtered9.split('M106', 1)[0]
        filtered11 = filtered10.split('M84', 1)[0]
        filtered12 = filtered11.split(';', 1)[0]
        lhs = filtered12.split('=') # splt the lines between = symbol into 2


        if(len(lhs) == 2): # if the line has an E command
            lhs2 = lhs[1].split('F') # split a lines with F into 2
            lhs3 = lhs[1].split('Z') # split a lines with Z into 2
            newLine = lhs[0] # add the first line to the newLine
            if(len(lhs3) == 2): # if a z has been encounterd after an E command

                if (lhs3[0].find("-2 ") != -1): # if line has number -2
                    lastNumber = lastNumber + float(lhs3[0])
                    newLine = newLine + "=" + str(lastNumber * 100000) + " Z" + lhs3[1]
                    print(lastNumber)

                else:
                    lastNumber = float(lhs2[0])
                    # E command is multiplied with 100000 and the rest o the command is pasted after
                    newLine = newLine + "=" + str(lastNumber * 100000) + " Z" + lhs3[1]

            elif(len(lhs2) == 2): # if a F has been encounterd after an E command

                if (lhs2[0].find("-2 ") != -1): # if line has number -2
                    lastNumber = lastNumber + float(lhs2[0])
                    newLine = newLine + "=" + str(lastNumber * 100000) + " Z" + lhs2[1]
                    print(lastNumber)

                else:
                    lastNumber = float(lhs2[0])
                    # E command is multiplied with 100000 and the rest o the command is pasted after
                    newLine = newLine + "=" + str(lastNumber * 100000) + " Z" + lhs2[1]



            else: # no letters after the E commands
                newLine = newLine + "=" + str(float(lhs3[0])*100000)
                lastNumber = float(lhs[1])
        else:
            newLine = lhs[0] # no E command

        new_file.write(newLine + "\n")
        if (newLine.find("G90") != -1): #if the  line has G90 then write a M2 command
            new_file.write("M2")
