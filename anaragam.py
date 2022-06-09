s=input("enter string :  ")
y=input("enter text ;   ")
a={}
b={}
ans=0
for i in range(len(s)):
	a[s[i]]=s.count(s[i])
for j in range(len(y)):
	b[y[j]]=y.count(y[j])
for k in a:
	for l in b:
		if(k==l):
			if(a[k]==b[l]):
				ans=k
if(ans==s[len(s)-1]):
	print("it is anagram")
else:
	print("not")
