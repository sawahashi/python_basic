with open('address.txt') as f:
#line = f.readlines()
	lines=sorted([line[:-1].split('\t') for line in f],key=lambda x:x[1])
for l in lines:
	print '\t'.join(l)	
