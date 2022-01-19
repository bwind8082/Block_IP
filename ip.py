#!/bin/env python3


filepath = "list.txt"
with open(filepath) as fp:
    a = fp.read().splitlines()
with open(filepath, "w") as fp:
i = 0
j = 1
while(j<len(a)):
	a[i] = a[i].split(":")
	a[j] = a[j].split(":")
	#print(a[i][0])
	if(a[i][0]==a[j][0]):
		a[i][1]+=a[j][1]
		print(a[i][1])
		a[j]=':'.join(a[j])
		a[i]=':'.join(a[i])
		del(a[j])
		j=i+1
	else:
		a[j]=':'.join(a[j])
		a[i]=':'.join(a[i])
		i+=1
		j+=1
print(a)
        
        
