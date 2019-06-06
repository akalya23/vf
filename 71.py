bb=list(input())
for i in range(0,len(bb),2):
	bb[i],bb[i+1]=bb[i+1],bb[i]
print("".join(bb))
