def c(p,r,t):
	if t==0:
		return p
	else:
		return c(p+(p*r)/100,r,t-1)
#print(c(1000,10,2))
p=int(input("enter the principle amount"))
t=int(input("enter the time"))
r=int(input("enter the rate"))
print(c(p,r,t))
