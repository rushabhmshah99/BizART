def validateUser(username):
	if(username=='apekshit' or username=='tanvi' or username=='rushabh'):
		return username
	else:
		return None
def validatePassword(username, password):
	if(username=='apekshit' and password=='ape'):
		return 'ape'
	elif(username=='tanvi'and password=='tan'):
		return 'tan'
	elif(username=='rushabh'and password=='rms'):
		return 'rms'
	else:
		return None