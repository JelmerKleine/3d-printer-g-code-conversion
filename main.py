with open('g-code.txt') as f:
    for line in f:
        new_line=""
        for i in line:
            if i =='e':
                break
            new_line=i+new_line
    print(line)
    print(new_line)