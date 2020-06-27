x = int(input())
suma = 0
for i in range(3):
    suma+=int(x%10)
    x=int(x/10)

print(suma)
