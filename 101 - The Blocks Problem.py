'''
給N個區塊，區塊的編號從0 至 N-1，接著會有4種指令：
move a onto b： 把a和b上方的區塊都歸回到原本位置，再把a疊到b上方。
move a over b： 把a上方的區塊都歸回到原本位置， 再把a疊到b所在區塊堆的上方。
pile a onto b： 把b上方的區塊都歸回到原本位置， 再把a及它上面的區塊堆都疊到b上方。
pile a over b： 把a及上方的區塊都疊到b所在區塊堆的上方。  
如果a和b都在同一區塊堆，則該行指令無效。最後指令是quit時，顯示每個區塊堆的細節，如果該編號區塊已疊在別的區塊則那行空白。
'''

import re
pat = re.compile(r'(\S{4}) (\d+) (\S{4}) (\d+)')
inputS = input().split("\n")
list1 = []
for i in range(int(inputS[0])):
    list1.append([i])

def trueposition(i):
    if  list1[i][0] == i:
        return i
    else :
        return list1[i][0]

def moveonto(i,j):
    positioni = trueposition(i)
    positionj = trueposition(j)
    
    if positioni!=positionj:
        for m in list1[positioni][list1[positioni].index(i)+2:]:
            list1[m]=[m]

        list1[positioni] = list1[positioni][:list1[positioni].index(i)]
        for m in list1[positionj][list1[positionj].index(j)+1:]:
            list1[m]=[m]

        list1[positionj] = list1[positionj][:list1[positionj].index(j)+1]

        list1[i]=[positionj]
        list1[positionj].extend([i])

def moveover(i,j) :
    positioni = trueposition(i)
    positionj = trueposition(j)

    if positioni!=positionj:
        for m in list1[positioni][list1[positioni].index(i)+1:]:
            list1[m]=[m]
        list1[positioni] = list1[positioni][:list1[positioni].index(i)]

        list1[i]=[positionj]
        list1[positionj].extend([i])

def pileonto(i,j):
    positioni = trueposition(i)
    positionj = trueposition(j)
    
    if positioni!=positionj:
        
        temp1 = list1[positionj][list1[positionj].index(j)+1:]
        list1[positionj] = list1[positionj][:list1[positionj].index(j)+1]
        for m in temp1:
            list1[m]=[m]
        
        temp2 = list1[positioni][list1[positioni].index(i):]
        
        list1[positionj].extend(list1[positioni][list1[positioni].index(i):])
     
        list1[positioni] = list1[positioni][:list1[positioni].index(i)]
        for m in temp2:
            list1[m]=[positionj]
  
def pileover(i,j):
    positioni = trueposition(i)
    positionj = trueposition(j)
    if positioni!=positionj:
        list1[positionj].extend(list1[positioni][list1[positioni].index(i):])
    
    
        temp = list1[positioni][list1[positioni].index(i):]
        list1[positioni] = list1[positioni][:list1[positioni].index(i)]
        for m in temp:
            list1[m]=[positionj]
    

#Print list
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
                moveonto(int(run.group(2)), int(run.group(4)))
            if run.group(3) == "over":
                moveover(int(run.group(2)), int(run.group(4)))
        if run.group(1) == "pile":
            if run.group(3) == "onto":
                pileonto(int(run.group(2)), int(run.group(4)))
            if run.group(3) == "over":
                pileover(int(run.group(2)), int(run.group(4)))

for i in range(0, len(list1)):
    print('%d:'% i,end='')
    string2 = list1[i]
    if list1[i][0] != i:
        print()
        continue
    else:
        print(end=' ')
        for j in string2:
            print(j, end='')
            if j != string2[-1]:
                print(end=' ')
    print()
