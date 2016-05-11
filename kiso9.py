with open('address.txt') as f:
#line = f.readlines()
	lines=sorted([line[:-1].split('\t') for line in f],key=lambda x:x[0],reverse=True) 
	lines2=sorted(lines,key=lambda x:x[1],reverse=True)
for l in lines2:
    print '\t'.join(l)
