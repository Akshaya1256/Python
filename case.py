ch=input("enter a character")
if ch>='0' and ch<='9':
    print("digit")
if ch>='A' and ch<='Z':
    print("uppercase")
elif ch>='a' and ch<='z':
    print("lowercase")
else:
    print("Special character")

