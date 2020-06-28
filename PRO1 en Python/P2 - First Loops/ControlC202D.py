from jutge import *

for x, y in read_many(int, int):
    suma_cubs = 0
    aux = x
    while aux <= y:
        suma_cubs += aux**3
        aux+=1
    print('suma dels cubs entre %d i %d: %d' %(x,y,suma_cubs))
