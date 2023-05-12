num=[1,4,7,9,12,16,47,37,323]
num.sort()
print(num)
print(num[::4])
print(num[-6:-1])
num.reverse()
num.sort(reverse=True)
print(num)
num.sort(reverse=False)
print(num)
for i in num:
    print(i)
