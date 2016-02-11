import calendar
def removeArticles(query):
	articles = ["a","an","the"]
	for token in query:
		if token in articles:
			query.remove(token)
	return query
def removePrepositions(query):
	prepositions = ["of","in","for","on","from","to","too","off"]
	for token in query:
		if token in prepositions:
			query.remove(token)
	return query
def removeConjunctions(query):
	conjunctions = ["and","between"]
	for token in query:
		if token in conjunctions:
			query.remove(token)
	return query
def removePunctuations(query):
	punctuations = ['?',',','!',"."]
	for i in query:
		for i in punctuations:
			query = query.replace('?','')
	return query

def queryProcessing(query):
	query = query.lower()
	query = removePunctuations(query)
	query = query.split(" ")
	# compare sales or profits or losses or margins
	comparelist = ["compare","contrast","difference","differentiate","better","worse","vs"]
	# list stuff
	showlist = ["show","list","give","print","tell","display","return","get"]
	# question
	questionlist = ["what","which","how","where"]
	if any(token in query for token in comparelist):
		return compare(query,comparelist)
	if any(token in query for token in showlist):
		return show(query,showlist)
	if any(token in query for token in questionlist):
		return question(query,questionlist)

def question(query,questionlist):
	for token in questionlist:
		if token in query:
			query.remove(token)
	query = removeArticles(query)
	query = removePrepositions(query)
	query = removeConjunctions(query)
	# increase decrease
	todolist = ["increase","improve","double","reduce","decrease","earn","more","lose","losing","gain","gaining"]
	if any(token in query for token in todolist):
		return todo(query,todolist)
	else:
		show(query,"")

def todo(query,todolist):
	for token in query:
		if token in todolist:
			return token,"todo"

def show(query,showlist):
	for token in showlist:
		if token in query:
			query.remove(token)
	query = removeArticles(query)
	query = removePrepositions(query)
	query = removeConjunctions(query)

	profit = ["profits","profit","gain","profitable","gain","gaining"]
	loss = ["loss","losses","losing"]
	if any(token in query for token in profit):
		return "profit","show"
	if any(token in query for token in loss):
		return "loss","show"
	
def compare(query,comparelist):
	for token in comparelist:
		if token in query:
			query.remove(token)
	query = removeArticles(query)
	query = removePrepositions(query)
	query = removeConjunctions(query)


	months = [x.lower() for x in list(calendar.month_name)]
	months_abbr = [x.lower() for x in list(calendar.month_abbr)]
	year = ['2014','2015']
	for token in query:
		if not(token in months or token in months_abbr):
			if token not in year:
				query.remove(token)


	startmonth, startyear, endmonth, endyear = -1,-1,-1,-1
	for token in query:
		if token.isdigit():
			startyear = int(token)
			query.remove(token)
			break
	for token in query:
		if token.isdigit():
			endyear = int(token)
			query.remove(token)
			break
	for token in query:
		if token in months or token in months_abbr:
			startmonth = token
			query.remove(token)
			break
	for token in query:
		if token in months or token in months_abbr:
			endmonth = token
			query.remove(token)
			break
	return [startmonth,startyear,endmonth,endyear],"compare"




'''query = "Compare the sales of June 2014 and July 2015"
queryProcessing(query)
query = "Compare the sales of 2014 and 2015"
queryProcessing(query)
query = "Compare the sales of June 2014 and 2015"
queryProcessing(query)
query = "differentiate the sales of 2014 and 2015"
queryProcessing(query)
query = "Was 2014 better than 2015?"
queryProcessing(query)
query = "Compare sales of 2014"
queryProcessing(query)
query = "show flights going in profit"
queryProcessing(query)
query = "How can I earn more"
print queryProcessing(query)
query = "Show me the profits"
print queryProcessing(query)
query = "How can I earn losses"
print queryProcessing(query)
query = "Where am i losing money?"
print queryProcessing(query)
query = "List all the flights losing money"
print queryProcessing(query)'''
query = "Show flights in profits"
print queryProcessing(query)
