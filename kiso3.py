f=open('address.txt','r')
f1=open('col1.txt','w')
f2=open('col2.txt','w')
for line in f:
	ken,machi=line[:-1].split('\t')
	f1.write(ken)
	f1.write("\n")
	f2.write(machi)
	f2.write("\n")

f.close()
f1.close()
f2.close()













