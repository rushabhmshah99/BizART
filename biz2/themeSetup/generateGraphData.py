import csv
data = []
months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def readFlightData():	
	with open('flightData.csv', 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:
	        data.append(row)

	print len(data)

def calcRevenueWithinTime(year, month=-1):

	readFlightData()
	data2 = [0]*(len(data)+1)
	rownum = 0
	with open('passengers_plane.csv', 'rb') as f:
	    reader = csv.reader(f) 
	    for row in reader:

	    	if rownum != 0:
	    		#print eval(row[1])+1
		    	if row[2] == 'Economy':
		    		rev = data[eval(row[1])][7]
		    	if row[2] == 'Business':
		    		rev = data[eval(row[1])][8]
		    	if row[2] == 'First Class':
		    		rev = data[eval(row[1])][9]
		    	data2[eval(row[1])] += eval(rev)
	    	rownum +=1

	
	for x in xrange(1, len(data2)-1):
		data2[x] = data2[x] - eval(data[x][10]) - eval(data[x][11]) - eval(data[x][12])
	print data2

	rev2 = 0
	for el in xrange(1, len(data)):
		str1 = data[el][1].split(" ")
		date = str1[0].split("-")
		if (int(date[0]) == year and month == -1) or (int(date[0]) == year and int(date[1]) == month):
			rev2 += data2[el]
	if month == -1:
		print "Revenue for "+str(year)+ " is "+str(rev2)
	else:
		print "Revenue for "+months[month]+", "+str(year)+ " is "+str(rev2)
	        
	

calcRevenueWithinTime(2015,1)