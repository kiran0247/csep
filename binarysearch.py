n=int(input("size"))
arr=list(map(int,input().split()))
key=int(input("enter the number"))
ans=0
lo=0
hi=n-1
while(lo<=hi):
	mid=(lo+hi)//2
	if arr[mid]==key: 
		ans=1
		break
	elif(arr[mid]>key):
		hi=mid-1
	else:
		lo=lo+1
if(ans==1):
	print(" present")
else:
	print("not present")
