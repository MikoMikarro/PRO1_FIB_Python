n = int(input())
aux = n
suma = 0
contador = 1

while n != 0:
    if contador%2 != 0:
        suma += int(n%10)
    n = int(n/10)
    contador+=1

if suma%2 == 0:
    print(aux,"ES TXATXI")
else:
    print(aux,"NO ES TXATXI")
