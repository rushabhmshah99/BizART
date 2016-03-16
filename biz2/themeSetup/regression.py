def regression(data):

	x = []
	y = []
	n = len(data)
	for row in data:
		x.append(row[0])
		y.append(row[1])
	xmean,ymean,xy,sum1,sum2,sum3 = sum(x)/n,sum(y)/n,0,0,0,0
	for i in range(n):
		xy += x[i]*y[i]
		sum1 += (x[i]-xmean)*(y[i]-ymean)
		sum2 += (x[i]-xmean)**2
		sum3 += x[i]**2
	b1 = xy/sum3
	b0 = ymean - b1*xmean

	xin = int(raw_input("Enter x value\n"))
	print "The y value is",(b0+b1*xin)

	



	# 1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4 5 5 5 5
	# 3 5 6 9 4 6 7 10 4 6 8 10 5 7 9 12 7 10 12 6 
