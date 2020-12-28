import re
pat = re.compile(r'(\S{4}) (\d+) (\S{4}) (\d+)')
inputS = input().split("\n")
list1 = [None]*int(inputS[0])
for i in range(0,int(inputS[0])):
    list1[i] = str(i)

def clearup(i):
    if list1[int(i)][0]==i:
        position = int(i)
    else :
        position = int(list1[int(i)])
    temp = list1[position].split(i)
    list1[position] = temp[0]
    for m in temp[1]:
        list1[int(m)]=m
def moveto(i,j):
    if list1[int(i)][0]==i:
        positioni = int(i)
    else :
        positioni = int(list1[int(i)])
    if list1[int(j)][0]==j:
        positionj = int(j)
    else :
        positionj = int(list1[int(j)])
    temp = list1[positioni].split(i)
    list1[positioni] = temp[0]
    for m in temp[1]:
        list1[int(m)] = str(positionj)
    list1[int(i)] = str(positionj)
    list1[int(positionj)] += i
    list1[int(positionj)] += temp[1]

def moveonto(i,j):
    clearup(i)
    clearup(j)
    list1[int(i)]=j
    list1[int(j)]+=j
    list1[int(j)]+=i

def moveover(i,j) :
    clearup(i)
    if list1[int(j)][0] == j:
        positionj = int(j)
    else:
        positionj = int(list1[int(j)])
    list1[int(i)] = str(positionj)
    list1[positionj] += i

def pileonto(i,j):
    clearup(j)
    moveto(i,j)
def pileover(i,j):
    moveto(i,j)

for i in range(1,len(inputS)+1):
    if inputS[i]=="quit":
        break
    elif not(re.fullmatch(pat,inputS[i])):
        print("error input")
        break
    else :
        run = re.search(pat, inputS[i])
        if run.group(1) == "move" :
            if run.group(3) == "onto" :
                moveonto(run.group(2),run.group(4))
            if run.group(3) == "over" :
                moveover(run.group(2),run.group(4))
        if run.group(1) == "pile" :
            if run.group(3) == "onto" :
                pileonto(run.group(2),run.group(4))
            if run.group(3) == "over" :
                pileover(run.group(2),run.group(4))

for i in range(0,len(list1)):
    print(str(i)+':' ,end = ' ')
    string2 = list1[i]
    if list1[i][0] != str(i):
        print()
        continue
    else:
        for j in string2 :
            print(j,end = ' ')
    print()
