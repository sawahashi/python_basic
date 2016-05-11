from collections import Counter

f=open('col2.txt','r')

a=Counter()
for line in f:
	a[line]+=1
lines=sorted(a.items(),key=lambda x:x[1],reverse=True)
for k, v in lines:
	#print '\t'.join(l)
	print k.rstrip("\n"),v
f.close() 
