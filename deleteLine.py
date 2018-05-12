with open("test.txt", "r") as f:
    lines = f.readlines()
    #print(lines)
with open("test.txt", "w") as f_w:
    for index, line in enumerate(lines):
        if index%2 == 0:
            f_w.write(line)
