n=int(input("enter n:"))
count=0
for i in (2,n):
    for j in (2,i):
        if (i%j==0):
            count+=1
            j+=1
    if count==2:
        print(i)
    i+=1

