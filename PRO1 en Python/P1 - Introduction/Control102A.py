x, a, b, c, d = input().split()
x = int(x)
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if(x >= a and x <= b) or (x >= c and x <= d):
    print("si")
else:
    print("no")
#miro si b y c son iguales si lo son solo miro si a existe entre a y d
