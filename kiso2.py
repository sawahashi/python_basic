f=open("address.txt","r")

for row in f:
	print (row.expandtabs(1))

f.close()

