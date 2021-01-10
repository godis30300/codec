import re
pat = re.compile(r'(\S{4}) (\d+) (\S{4}) (\d+)')
inputS = input().split("\n")
list1 = []
for i in range(int(inputS[0])):
    list1.append([])
    list1[i].append([])
    list1[i][0] = str(i)
    
def trueposition(i):
    if list1[int(i)][0]==i:
        return int(i)
    else :
        return int(list1[int(i)][0])

def clearup(i):
    position = trueposition(i)

    temp = list1[position].index(i)
    list1[position] = list1[position][:list1[position].index(i)]
    
    for m in temp:
        list1[int(m)].remove(m)
        list1[int(m)].extend([m])
        
def moveto(i,j):
    positioni = trueposition(i)
    positionj = trueposition(j)

    temp = list1[positioni][:list1[positioni].index(i)-1]
    list1[positionj].extend(list1[positioni][list1[positioni].index(i):])
    for m in temp:
        list1[int(m)].remove(m)
        list1[int(temp)].extend([str(positionj)])
    del list1[positioni][:]
    list1[positioni]=temp

def moveonto(i,j):
    clearup(i)
    clearup(j)
    
    positionj = trueposition(j)
    
    list1[int(i)].remove(i)
    list1[int(i)].extend([j])
    
    list1[positionj].extend([i])

def moveover(i,j) :
    clearup(i)
        
    positionj = trueposition([j])
    
    list1[int(i)].remove(i)
    list1[int(i)].extend([str(positionj)])
    list1[positionj].extend([i])

def pileonto(i,j):
    clearup(j)
    moveto(i,j)
def pileover(i,j):
    moveto(i,j)


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