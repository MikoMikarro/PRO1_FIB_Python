from FIB import input
x, y = input().split()
x = int(x); y = int(y)

if y > x:
    for i in range((y - x)+1):
        print(y)
        y-=1
elif y < x:
    for i in range((x - y)+1):
        print(x)
        x-=1
else:
    print(x)
