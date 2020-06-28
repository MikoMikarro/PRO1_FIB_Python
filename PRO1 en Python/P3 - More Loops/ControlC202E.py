
n = int(input())
posicion_slash = n-1
for filas in range(n):
    for columnas in range(n):
        if columnas == posicion_slash:
            print('/', end='')
        elif columnas > posicion_slash:
            print('*', end='')
        else:
            print('+', end='')
    posicion_slash-=1
    print('')
