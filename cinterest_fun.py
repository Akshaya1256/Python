def compoundinterest(p:float,r:float,t:float)->float:
    ci=p*pow((1+r/100),t)
    return ci
p=float(input("Enter amount:"))
r=float(input("Enter rate of interest:"))
t=float(input("Enter time period:"))
ci=compoundinterest(p,r,t)
print("COMPOUND INTEREST:{}".format(ci))
