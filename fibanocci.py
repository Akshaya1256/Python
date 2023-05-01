n=int(input("enter n "))
a=0
b=1
sumof=0
i=0
while(n>i):
    sumof=a+b
    print(sumof)
    a=b
    b=sumof
    i+=1

