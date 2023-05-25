#!bin/env/python

# password cracker for old unix using crypt algorithm to hash passwords
# code by: anomalous254 | nyando | am_request
# github: www.github.com/anomalous254

# loading imports i.e libraries
import crypt  # --> crypt algorithm for hashing passwd (password, salt) :)
from termcolor import colored  # for cool colorising the terminal
import threading
import time

# function to compare plaitext pass/word with hashes pass if equal i.e pass cracked


def cracker(hash_txt):
   salt = hash_txt[0:2]

   f = open('passdict.txt', 'r')
   for word in f.readlines():
      passwd = word.strip('\n')
      hashed = crypt.crypt(passwd, salt)

      if hashed == hash_txt:
         print(colored(
             f"[+] Password found for password hash ( {hash_txt} ) --> {passwd}", "green"))
      else:
         print(f'{colored("[-] password not found!!","red")}')


def main():

   f = open('hashedpass.txt', 'r')
   for hashed in f.readlines():
      passwd = hashed.strip('\n')
      timeon = time.time()
      cracker(passwd)
      timeoff = time.time()
      print(timeoff - timeon)


if __name__ == '__main__':

   t = threading.Thread(target=main, )
   t.start()
