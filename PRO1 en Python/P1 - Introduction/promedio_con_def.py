def promedio(x,y):
    res = (x + y)/2
    if((res * 10) % 10 != 0):
        return res
    else:
        return(int(res))

def main():
    x, y = input().split() #con .split() introducimos las variables en la misma linea
    x = int(x)
    y = int(y)
    print(promedio(x, y))

main()
