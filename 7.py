  a1=list(input())
for i in range(0,len(a1),2):
	a1[i],a1[i+1]=a1[i+1],a1[i]
print("".join(a1))
