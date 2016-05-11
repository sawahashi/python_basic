import sys

argv=sys.argv
argc=len(argv)
if(argc!=2):
	print 'Usage pyton %s number' %argv[0]
	quit()
x=int(argv[1])
i=0
for line in open('address.txt','r'):
	print line
	i+=1
	if(x==i):
		break
