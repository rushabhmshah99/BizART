s = 1300
alpha = 80

def getCount(items, itemSet):
	count = 0

	for i in items:
		for j in itemSet:
			if set(i)<=set(j):
				count+=1
	return count

def pruning(listN, itemSet):
	c1 = []

	for j in listN:
		if getCount([j], itemSet) >= s:
			c1 += [j]
	return c1

def makeSets(itemSet):
	item_set = []
	for items in itemSet:
		for item in items:
			if [item] not in item_set:
				item_set +=[[item]]
	return list(item_set)


def makeTwoItem(element, itemSet):
	list1 = [element[0], element[1]]
	list2 = [element[0], element[2]]
	list3 = [element[1], element[2]]
	return [list1, list2, list3] 	

def applyAlgo(itemSet):

	l1 = pruning(makeSets(itemSet), itemSet)

	#print "L1: " + str(l1)+ "\n"
	c2 = []
	for i in range(0, len(l1)-1):
		for j in range(i+1, len(l1)):
			c2 += [list(set(l1[i]).union(set(l1[j])))]

	#print "C2: "+str(c2) + "\n"
	l2 = pruning(c2, itemSet)

	#print "L2: "+str(l2) + "\n"
	c3 = set()
	for i in range(0, len(l2)-1):
		for j in range(i+1, len(l2)):
			temp = frozenset(set(l2[i]).union(set(l2[j])))
			if len(temp)< (2*len(l2[i])):
				c3.add(temp)
	c3set = []
	for ele in c3:
		c3set += [list(ele)]
	#print "C3 (Before Apriori): "+str(c3set)+ "\n"

	c3final = []
	for element in c3set:
		list4 = makeTwoItem(element, itemSet)
		flag = 0
		for ele in list4:
			if ele not in l2:
				flag=1
		if flag==0:
			c3final += [element]
	#print "C3 (After Apriori): " + str(c3final)+ "\n"

	l3 = pruning(c3final, itemSet)
	print "L3: " + str(l3) 

	return l3