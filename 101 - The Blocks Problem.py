import re
pat = re.compile(r'(\S{4}) (\d+) (\S{4}) (\d+)')
inputS = input().split("\n")
list1 = [[None] * int(inputS[0]) for _ in range(1)]

for i in range(1, len(inputS) + 1):
    if inputS[i] == "quit":
        break
    elif not (re.fullmatch(pat, inputS[i])):
        print("error input")
        break
    else:
        run = re.search(pat, inputS[i])
        if run.group(1) == "move":
            if run.group(3) == "onto":
                moveonto(run.group(2), run.group(4))
            if run.group(3) == "over":
                moveover(run.group(2), run.group(4))
        if run.group(1) == "pile":
            if run.group(3) == "onto":
                pileonto(run.group(2), run.group(4))
            if run.group(3) == "over":
                pileover(run.group(2), run.group(4))

for i in range(0, len(list1)):
    print(str(i) + ':', end=' ')
    string2 = list1[i]
    if list1[i][0] != str(i):
        print()
        continue
    else:
        for j in string2:
            print(j, end=' ')
    print()