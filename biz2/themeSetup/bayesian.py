import sys

def countUnique(data):
	uniqueElements = [dict() for x in data[0]]
	for item in data:
		for i in xrange(len(item)):
			uniqueElements[i][item[i]] = 0
	#print uniqueElements
	return uniqueElements

def calcOutputProbability(element, index, data):
	for key, value in element.iteritems():
		for items in data:
			if items[index] == key:
				 value = value +1 
		element[key] = value
	
	return element

def createList(attribute_list, data):
	#print element
	len_attr = len(attribute_list)
	main_table = []
	for i in xrange(0, len_attr-1):
		attribute_table = []
		for key1, index in zip(attribute_list[i].iterkeys(), range(len(attribute_list[i]))):
			attribute_table.append([])
			for key2, index2 in zip(attribute_list[len_attr-1].iterkeys(), range(len(attribute_list[len_attr-1]))):

				attribute_table[index].append([])
				attribute_table[index][index2] = 0
				for item in data:
					if(item[i]==key1 and item[len_attr-1]==key2):
						attribute_table[index][index2] +=1
				attribute_table[index][index2] = 1.0*attribute_table[index][index2]/attribute_list[len_attr-1][key2] 

		#print attribute_table
		main_table.append(attribute_table)
	return main_table

def calcOutput(mainTable, input_data, attribute_list):
	print attribute_list
	conditionalProb = []
	for i in range(len(input_data)):
		index_attr = 0
		for key, index in zip(attribute_list[i].iterkeys(), range(len(attribute_list[i]))):
			if(key == input_data[i]):
				index_attr = index
				break
		conditionalProb.append(mainTable[i][index_attr])
	print conditionalProb
	len_attr = len(attribute_list)
	prob = [1.0]*len(attribute_list[len_attr-1])
	for i in range(len(attribute_list[len_attr-1])):
		for row in conditionalProb:
			prob[i] *= row[i]
	print prob
	list_kuch = [v for v in attribute_list[len_attr-1].itervalues()]
	for i in range(len(prob)):
		prob[i] *= list_kuch[i]

	print prob
	max_val = max(prob)
	index = prob.index(max_val)
	list_keys = [k for k in attribute_list[len_attr-1].iterkeys()]
	
	return list_keys[index]






'''min_val, range_val = loadData()
uniqueElements = countUnique()
attribute_list = []
for element in uniqueElements:
	ele = calcOutputProbability(element, uniqueElements.index(element))
	attribute_list+= [ele]
mainTable = createList(attribute_list)
print mainTable
print "Enter the attribute values:"
data = [0] *(len(attribute_list)-1)
for i in xrange(0, len(attribute_list)-1):
	data[i] = raw_input()
data[1] = int((eval(data[1]) - min_val)/range_val)
print data
calcOutput(mainTable, data, attribute_list)'''
