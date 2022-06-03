import math

new_file = open("calibrationCube2.nc", "w")
with open('CE6_xyzCalibration_cube.gcode') as f:
    new_line = ""
    segment = 0

    for line in f:
        stripped = line.split('S', 1)[0]
        stripped2 = stripped.replace("E","H=")
        stripped3 = stripped2.replace("G92","M01")
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
        filtered11 = filtered10.split('M106', 1)[0]
        doubleStripped = filtered11.split(';', 1)[0]
        lhs = doubleStripped.split('=')
        #print(doubleStripped)
        #print(lhs[0])

        if(len(lhs) == 2):
            #print("="+lhs[1])
            lhs2 = lhs[1].split('F')
            lhs3 = lhs[1].split('Z')
            newLine = lhs[0]
            if(len(lhs3) == 2): # if a z has been encounterd after an E command
                # E command is multiplied with 100000 and the rest o the command is pasted after
                newLine = newLine + "=" + str(float(lhs3[0]) * 100000) + " Z" + lhs3[1]
                lastNumber = float(lhs3[0])

            elif(len(lhs2) == 2): #if a F has been encounterd after an E command
                # E command is multiplied with 100000 and the rest o the command is pasted after
                """if (lhs2[0].find("-2 ") != -1):
                    number = str(lastNumber - float(lhs2[0]))
                else:
                    number = str(float(lhs2[0]))
                    lastNumber = float(lhs2[0])""" #useless code

                newLine = newLine + "=" + str(float(lhs2[0])*100000) + " F" + lhs2[1]



            else: # no letters after the E commands
                newLine = newLine + "=" + str(float(lhs2[0])*100000) #/((math.pi*math.pow(1.75,2))/4)
                lastNumber = float(lhs3[0])
        else:
            newLine = lhs[0] # no E command

        new_file.write(newLine + "\n")
        if (newLine.find("G90") != -1): #if the last line has G90 then write a M2 command
            new_file.write("M2")
        #print(rhs)
        #print("hi")
        #if segment == 1 :
            #new_file.write(newLine  + "\n")
       # if segment == 2:
            #new_file_2.write(newLine + "\n")
       # else:
            #print(newLine)
        #print(new_lind)