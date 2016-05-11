import sys
f=open('address.txt','r')
f2=open('address.txt','r')
argv=sys.argv
argc=len(argv)
if(argc!=2):
	print 'Usage pyton %s number' %argv[0]
	quit()
x=int(argv[1])
i=0
for line in f:
	i+=1

i2=0
for line2 in f2:
	if(i2>=i-x):
		print line2
	i2+=1
