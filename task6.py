import sys , math
try:
	infilename = sys.argv [1]
	outfilename = sys.argv [2]
except:
	print "Usage:", sys.argv[0], "infile  outfile"
	sys.exit (1)

ifile = open(infilename , 'r')
ofile = open(outfilename , 'w')

for line in ifile:
	args = line.split ()
	len_args = len(args)
	
	for i in range(len_args):
		ofile.write('%12.6f' % float(args[i]))

	# average value in a row
	mid = 0
	if len_args % 2 == 0:
		mid = (float(args[len_args/2]) + float(args[len_args/2-1])) / 2
	else:
		mid = float(args[int(len_args/2)])
	ofile.write('%12.6f\n' % mid)

ifile.close()
ofile.close()
