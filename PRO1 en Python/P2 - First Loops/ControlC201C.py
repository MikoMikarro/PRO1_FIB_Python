from jutge import read_many, read

x = read(int)
cont = 0
for n in read_many(int):
    if n == 0 or n%x == 0:
        cont+=1

print(cont)
