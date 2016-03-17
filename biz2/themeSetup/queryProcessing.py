import calendar
dict = {'alabama':'US-AL', 'alaska':'US-AK', 'arizona':'US-AZ', 'arkansas':'US-AR', 'california':'US-CA', 'colorado':'US-CO', 'connecticut':'US-CT', 'delaware':'US-DE', 'florida':'US-FL', 'georgia':'US-GA', 'hawaii':'US-HI', 'idaho':'US-ID', 'illinois':'US-IL', 'indiana':'US-IN', 'iowa':'US-IA', 'kansas':'US-KS', 'kentucky':'US-KY', 'louisiana':'US-LA', 'maine':'US-ME', 'maryland':'US-MD', 'massachusetts':'US-MA', 'michigan':'US-MI', 'minnesota':'US-MN', 'mississippi':'US-MS', 'missouri':'US-MO', 'montana':'US-MT', 'nebraska':'US-NE', 'nevada':'US-NV', 'new hampshire':'US-NH', 'new jersey':'US-NJ', 'new mexico':'US-NM', 'new york':'US-NY', 'north carolina':'US-NC', 'north dakota':'US-ND', 'ohio':'US-OH', 'oklahoma':'US-OK', 'oregon':'US-OR', 'pennsylvania':'US-PA', 'rhode island':'US-RI', 'south carolina':'US-SC', 'south dakota':'US-SD', 'tennessee':'US-TN', 'texas':'US-TX', 'utah':'US-UT', 'vermont':'US-VT', 'virginia':'US-VA', 'washington':'US-WA', 'west virginia':'US-WV', 'wisconsin':'US-WI', 'wyoming':'US-WY', 'andhra pradesh':'IN-AP', 'arunachal pradesh':'IN-AR', 'assam':'IN-AS', 'bihar':'IN-BR', 'chhattisgarh':'IN-CT', 'goa':'IN-GA', 'gujarat':'IN-GJ', 'haryana':'IN-HR', 'himanchal pradesh':'IN-HP', 'jammu and kashmir':'IN-JK', 'jharkhand':'IN-JH', 'karnataka':'IN-KA', 'kerela':'IN-KL', 'madhya pradesh':'IN-MP', 'maharashtra':'IN-MH', 'manipur':'IN-MN', 'meghalaya':'IN-ML', 'mizoram':'IN-MZ', 'nagaland':'IN-NL', 'odisha':'IN-OR', 'punjab':'IN-PB', 'rajasthan':'IN-RJ', 'sikkim':'IN-SK', 'tamil nadu':'IN-TN', 'telangana':'IN-TG', 'tripura':'IN-TR', 'uttarakhand':'IN-UT', 'uttar pradesh':'IN-UP', 'west bengal':'IN-WB', 'andaman and nicobar islands':'IN-AN', 'chandigarh':'IN-CH', 'dadra and nagar haveli':'IN-DN', 'daman and diu':'IN-DD', 'delhi':'IN-DL', 'lakshadweep':'IN-LD', 'puducherry':'IN-PY', 'abu dhabi':'AE-AZ', 'ajman':'AE-AJ', 'fujairah':'AE-FU', 'sharjah':'AE-SH', 'dubai':'AE-DU', 'ras al khaymah':'AE-RK', 'umm al-quwain':'AE-UQ'}
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
def removeExtraWords(query):
	extrawords = ["all","information","details","are"]
	for token in query:
		if token in extrawords:
			query.remove(token)
	return query
def removePunctuations(query):
	punctuations = ['?',',','!',"."]
	for i in query:
		for i in punctuations:
			query = query.replace('?','')
	return query
def AreaCodeMapping(commonName):
	return dict[commonName]
def queryProcessing(query):
	query = query.lower()
	query = removePunctuations(query)
	query = query.split(" ")
	# compare sales or profits or losses or margins
	comparelist = ["compare","contrast","difference","differentiate","better","worse","vs","comparison"]
	# list stuff
	showlist = ["show","list","give","print","tell","display","return","get"]
	# question
	questionlist = ["what","which","how","where","is"]
	# suggest
	suggestlist = ["suggest","should"]

	if any(token in query for token in comparelist):
		return compare(query,comparelist)
	if any(token in query for token in showlist):
		return show(query,showlist)
	if any(token in query for token in questionlist):
		return question(query,questionlist)
	if any(token in query for token in suggestlist):
		return suggest(query,suggestlist)

def suggest(query,suggestlist):
	for token in suggestlist:
		if token in query:
			query.remove(token)
	query = removeArticles(query)
	query = removePrepositions(query)
	query = removeConjunctions(query)
	query = removeExtraWords(query)
	newflightlist = ["frequency","flight","flights","openings","new","opportunities","more","required"]
	if any(token in query for token in newflightlist):
		for token in newflightlist:
			if token in query:
				query.remove(token)
		
		# hence query = "source, destination". 
		# Map the source and destination to their respective country and state codes

	for token in query:
		if token in dict:
			source = AreaCodeMapping(token)
			query.remove(token)
			break
	for token in query:
		if token in dict:
			dest = AreaCodeMapping(token)
			query.remove(token)
			break
	return [source,dest],"suggest"



def question(query,questionlist):
	for token in questionlist:
		if token in query:
			query.remove(token)
	query = removeArticles(query)
	query = removePrepositions(query)
	query = removeConjunctions(query)
	query = removeExtraWords(query)
	# increase decrease
	todolist = ["increase","improve","double","reduce","decrease","earn","more","lose","gain","gaining"]
	suggestlist = ["new","flights","openings","opportunities","flight","open"]
	if any(token in query for token in todolist):
		return todo(query,todolist)
	elif any(token in query for token in suggestlist):
		return suggest(query,suggestlist)
	else:
		return show(query,"")

def todo(query,todolist):
	for token in query:
		if token in todolist:
			return token,"profit"

def show(query,showlist):
	for token in showlist:
		if token in query:
			query.remove(token)
	query = removeArticles(query)
	query = removePrepositions(query)
	query = removeConjunctions(query)
	query = removeExtraWords(query)
	profit = ["profits","profit","gain","profitable","gain","gaining"]
	loss = ["loss","losses","losing"]
	attribue_flights = ["flights","flight","plane","planes"]
	attribute_passengers = ["passengers","passengers"]
	attribute_competitor = ["competitor","competitors"]
	if any(token in query for token in profit):
		return "profit","show"
	elif any(token in query for token in loss):
		return "loss","show"
	elif any(token in query for token in attribue_flights):
		return "flights","show"
	elif any(token in query for token in attribute_passengers):
		return "passengers","show"
	elif any(token in query for token in attribute_competitor):
		return "competitor","show"
	
def compare(query,comparelist):
	for token in comparelist:
		if token in query:
			query.remove(token)
	query = removeArticles(query)
	query = removePrepositions(query)
	query = removeConjunctions(query)
	query = removeExtraWords(query)

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
query = "How can I earn on losses"
print queryProcessing(query)
query = "Where am i losing money?"
print queryProcessing(query)
query = "List all the flights losing money"
print queryProcessing(query)
query = "Show flights in profits"
print queryProcessing(query)
query = "suggest new flight openings from delhi to maharashtra"
query = "Should I increase the frequency of flights from delhi to maharashtra"
query = "Is a new flight from A to B required?"
query = "what will be my revenue on opening new flights from Delhi to Maharashtra?"



clustering K means
#dates and avg revenue convert dates to miliseconds
cost
male female passengers related to competitors
occupation of passengers
age group
#UI dashboard
baysian predict if new flight is in profit or loss
apriori
simple query processing

'''