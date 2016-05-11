f1=open('col1.txt','r')
f2=open('col2.txt','r')
f3=open('address.txt','w')
line2=f2.readlines()
i=0
for line1 in f1:
	line1=line1.rstrip("\n")
	f3.write(line1+'\t'+line2[i])
	#print line2[i]
	i+=1
#print i

f1.close()
f2.close()
f3.close()	
