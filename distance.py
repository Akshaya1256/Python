import math
def distance(x1,y1,x2,y2):
    dist=math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
    return dist
x1=int(input("enter x1"))
x2=int(input("enter x2"))
y1=int(input("enter y1"))
y2=int(input("enter y2"))
dist=distance(x1,y1,x2,y2)
print(dist)
