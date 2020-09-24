#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import os

import random
from math import pow
import sys


a = random.randint(2, 10)


def gcd(a, b):
  if a < b:
    return gcd(b, a)
  elif a % b == 0:
    return b;
  else:
    return gcd(b, a % b)

  #  Creation of large random Numbers


def gen_key(q):
  key = random.randint(pow(10, 20), q)
  while gcd(q, key) != 1:
    key = random.randint(pow(10, 20), q)

  return key


# Modular exponentiation
def power(a, b, c):
  x = 1
  y = a

  while b > 0:
    if b % 2 == 0:
      x = (x * y) % c;
    y = (y * y) % c
    b = int(b / 2)

  return x % c


# Accymetric Encryption
def encrypt(msg, q, h, g):
  en_msg = []

  k = gen_key(q)  # Private Key of sender
  s = power(h, k, q)
  p = power(g, k, q)

  for i in range(0, len(msg)):
    en_msg.append(msg[i])

  print("g^k used : ", p)
  print("g^ak used : ", s)
  for i in range(0, len(en_msg)):
    en_msg[i] = s * ord(en_msg[i])

  return en_msg, p


def decrypt(en_msg, p, key, q):
  dr_msg = []
  h = power(p, key, q)
  for i in range(0, len(en_msg)):
    dr_msg.append(chr(int(en_msg[i] / h)))

  return dr_msg

def caesarEncrypt(text, shiftsNumber):
  result = ""
  #The result is going to be submitted in variable result and then return to the  main program
#Shifts are entitled to change every-time
  #For debug of the program i used a classic example with 3 shifts
  
#Traverse to all the text i give you as an input

  for i in range(len(text)):
      #Take every character in position i
    
    char = text[i]
    #For every capital letter use an encryption 
       

    if (char.isupper()):#If is capital
      result += chr((ord(char) + shiftsNumber - 65) % 26 + 65) #Find which character is sum the transition and return the crypto character
  # Encryption of lower case letters
    else:
      result += chr((ord(char) + shiftsNumber - 97) % 26 + 97)

  return result.replace('q',' ')
def Caesar():
  # Input control and Data
  text = "I HAVE A SECRET "
  shiftsNumber = 3

  print("Αρχικό κείμενο : " + text)
  print("Μοτίβο Μετατόπισης : " + str(shiftsNumber))
  #Count the execution time
  from timeit import default_timer as timer
  start = timer()
  encryptedText=caesarEncrypt(text, shiftsNumber)
  end = timer()
  print("Κρυπτοκείμενο: ",encryptedText )

  print("Χρόνος Εκτέλεσης Κρυπτογράφησης σε nanoseconds  ",round(((end - start)*1000000000)))# THis function calculates in seconds and i convert it to nanoseconds


  #Encrypt the above code in Caesar Encryption
  #Using brute force i break the code to count the time needed
  

  letterAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  keylist=[]
  descryptionText=''
  start = timer()
  for key in range(len(letterAlphabet)):

    if (not descryptionText):
      pass
    else:
      keylist.append(descryptionText)
    descryptionText = ''

    for symbol in encryptedText:
      if symbol in letterAlphabet:
        num = letterAlphabet.find(symbol)
        num = num - key
        if num < 0:
          num = num + len(letterAlphabet)
        descryptionText = descryptionText + letterAlphabet[num]
      else:
        descryptionText = descryptionText + symbol
  end = timer()


  print("ΛΙΣΤΑ ΑΠΟΚΡΥΠΤΟΓΡΑΦΗΜΕΝΩΝ ΚΛΕΙΔΙΩΝ")
  for number, letter in enumerate(keylist):
      print(number, " " ,letter)
  print("Αποκρυπτογραφημένο μήνυμα",keylist[3])
  print("Χρόνος Αποκρυπτογράφησης σε nanoseconds  ",round(((end - start)*1000000000)))


# Driver code
def elGamal():
  text = "I HAVE A SECRET "
  print("Αρχικό μήνυμα Ελ Γκαμάλ :", text)

  q = random.randint(pow(10, 20), pow(10, 50))
  g = random.randint(2, q)

  key = gen_key(q)  # Ιδιωτικό κλειδί
  h = power(g, key, q)
  print("Γεννήτορας αριθμός g : ", g)
  print("g^a used : ", h)

#Κρυπτογράφηση
  en_msg, p = encrypt(text, q, h, g)
  #Αποκρυπτογράφηση
  dr_msg = decrypt(en_msg, p, key, q)
  dmsg = ''.join(dr_msg)
  print("Κρυπτογραφημένο μήνυμα Ελ Γκαμάλ :", dmsg);
def menuEpilogis():
  print("*************ΚΑΛΩΣΗΡΘΑΤΕ ΣΤΟ ΠΡΟΓΡΑΜΜΑ ΚΡΥΠΤΟΓΡΑΦΗΣΗΣ***************")
  print("*******************ΜΕΝΟΥ ΕΠΙΛΟΓΩΝ********************************************")
  ans = True
  while ans:
    print("""
      1.Κρυπτογράφηση Καίσαρα
      2.Έλ Γκαμάλ
      3.Έξοδος
      """)
    ans = input("Παρακαλώ Επιλέξτε ")
    if ans == "1":
      Caesar()
    elif ans == "2":
     elGamal()
    elif ans == "3":
      print("\n Έξοδος")
      sys.exit()
    elif ans != " ":
      print("\n Μή έγκυρη επιλογή δοκιμάστε ξανά")




if __name__ == '__main__':
  menuEpilogis()





















"""
#Βελτιωμένος αλγόριθμος Καίσαρα
text=text.lower()
encryptedText=""
for letter in text:
  if letter.isalpha()==True:
    nowLetter=ord(letter) -97 #μετατροπη σε ASCII και αφαιρουμε τον χαρακτηρα a=97
    nowLetter+=shiftsNumber
    nowLetter=nowLetter%26
    encryptedText +=chr(nowLetter+97)
  else:
    encryptedText+=letter
print(encryptedText)
"""






