n=int(input("enter no of rows:"))
k=n
for i in range(0,n):
    for j in range(0,i+1):
        print(k,end=" ")
    k=k-1
    print(end='\n')

