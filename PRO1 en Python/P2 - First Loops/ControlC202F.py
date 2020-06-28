from jutge import *

cont = 0
first = True
for i in read_many(int):
    if first:
        n = i
        print('nombres que acaben igual que %d:'%(n))
        first = False
    elif i%1000 == n%1000:
        print(i)
        cont+=1
if not first:
    print('total:',cont)
