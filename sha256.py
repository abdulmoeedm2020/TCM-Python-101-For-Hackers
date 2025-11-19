from pwn import *
import sys

if len(sys.argv) !=2:
	print("Invalid Arguments!")
	print(">> {} <sha256sum>".format(sys.argv[0]))
	exit()

wanted_hash = sys.argv[1]
password_file = 'rockyou.txt'
attempts = 0

with log.progress("Attempting to bacl: {}!\n".format(wanted_hash)) as p:
	with open(password_file, "r", encoding='latin-1') as password_lists:
		for password in password_lists:
			password = password.strip("\n").encode('latin-1')
			password_hash = sha256sum(password)
			p.status("[{}] {} == {}".format(attempts,password.decode('latin-1'),password_hash))
			if password_hash ==  wanted_hash:
				p.success("password hash found asfter {} attempts! {} hashed to {}!").format(attempts,password.decode('latin-1'),password_hash)
				exit()
			attempts +=1
		p.failure("password hash not found")
