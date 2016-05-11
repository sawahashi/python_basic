#f1=open('address.txt','r')

#for line in f1:
#	count=0
#	ken1,machi1=line[:-1].split('\t')
#	for line2 in open('address.txt','r'):
#		ken2,machi2=line2[:-1].split('\t')
#		if(ken1==ken2):
#			count+=1
#	print ken1,'\t',machi1,'/',count

f=open('address.txt','r')
from collections import Counter

a=Counter()
for line in f:
	tmp=line.split('\t')
	a[tmp[0]]+=1
#lines=a.items()
for k, v in a.items():
	print k.strip("\n"),v

f.close()
