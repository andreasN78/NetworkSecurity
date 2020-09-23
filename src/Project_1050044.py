
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

  # Δημιουργία Μεγάλων τυχαίων Αριθμών


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


# Ασσύμετρη Κρπτογράφηση
def encrypt(msg, q, h, g):
  en_msg = []

  k = gen_key(q)  # Ιδιωτικό κλειδί Αποστολέα
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
#Το αποτέλεσμα μου θα καταχωρηθεί στην μεταβλητή result και θα επιστραφεί στο κυρίως πρόγραμμα
  #Οι μετατοπίσεις ειναι εφικτό να αλλάζουν κάθε φορά
  #Για λόγους ορθής πιστοποίησης της λειτουργίας του αλγορίθμου χρησιμοποιήσαμε το κλασικό παράδειγμα απο τις διαφάνειες με 3 μετατοπίσεις

# Προσπέλασε όλο το κείμενο που σου δίνουμε σαν είσοδο
  for i in range(len(text)):
    #Παίρνει τον κάθε χαρακτήρα στην θέση i
    char = text[i]
        # Για κάθε κεφαλαίο γράμμα χρησιμοποίησε κρυπτογράφηση

    if (char.isupper()):#Εαν είναι κεφαλαίο
      result += chr((ord(char) + shiftsNumber - 65) % 26 + 65) #Βρές ποιος χαρακτήρας είναι πρόσθεσε την μετατόπιση και επέστρεψε τον κρυπτο χαρακτήρα
  # Κρυπτογράφησε τα μικρά γράμματα
    else:
      result += chr((ord(char) + shiftsNumber - 97) % 26 + 97)

  return result.replace('q',' ')

def textCipherInput():
  print(
    "Για να τρέξετε το πρόγραμμα με δικό σας κείμενο απλά πληκτρολογήστε, αλλιώς πιέστε ENTER και θα τρέξει παράδειγμα απο Διαφάνειες")
  text = str(input("Δώστε ένα κείμενο για Κρυπτογράφηση") or "I HAVE A SECRET")
  return text



def shiftsCaesarInput():
  print(
    "Για να τρέξετε το πρόγραμμα με δικό σας αριθμό απο μετατοπίσεις απλά πληκτρολογήστε, αλλιώς πιέστε ENTER και θα τρέξει παράδειγμα απο Διαφάνειες")
  shiftsNumber = int(input("Δώστε τον αριθμό των Μετατοπίσεων του Αλγορίθμου") or "3")
  return shiftsNumber

def Caesar():
  # Έλεγχος και είσοδος Δεδομένων
  text=textCipherInput()
  shiftsNumber=shiftsCaesarInput()
  #text = "I HAVE A SECRET "


  print("Αρχικό κείμενο : " + text)
  print("Μοτίβο Μετατόπισης : " + str(shiftsNumber))
  #Μέτρηση του Αλγορίθμου Χρόνος Εκτέλεσης
  from timeit import default_timer as timer
  start = timer()
  encryptedText=caesarEncrypt(text, shiftsNumber)
  end = timer()
  print("Κρυπτοκείμενο: ",encryptedText )

  print("Χρόνος Εκτέλεσης Κρυπτογράφησης σε nanoseconds  ",round(((end - start)*1000000000)))# H συνάρτηση επιστρέφει τον χρόνο σε δευτερόλεπτα για λόγους ευκρίνειας το μετατρέπω σε nanoseconds


  #Κρυπτογραφήσαμε το παραπάνω κώδικα με τον Αλγόριθμο του Καίσαρα
  #Θα τον σπάσουμε με την χρήση ωμής βίας για να δούμε σε πόσο χρόνο γίνεται και να δούμε πως μπορούμε να τον κάνουμε καλύτερο

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
  text = textCipherInput()
  print("Αρχικό μήνυμα Ελ Γκαμάλ :", text)

  q = random.randint(pow(10, 20), pow(10, 50))
  g = random.randint(2, q)

  key = gen_key(q)  # Ιδιωτικό κλειδί
  h = power(g, key, q)
  print("Γεννήτορας αριθμός g : ", g)
  print("g^a used : ", h)

#Κρυπτογράφηση
  from timeit import default_timer as timer
  start=timer()
  en_msg, p = encrypt(text, q, h, g)
  end=timer()
  print("Χρόνος Εκτέλεσης  Κρυπτογράφησης Eλ Γκαμαλ  σε nanoseconds  ",round(((end-start)*1000000000)))# H συνάρτηση επιστρέφει τον χρόνο σε δευτερόλεπτα για λόγους ευκρίνειας το μετατρέπω σε nanoseconds
  #Αποκρυπτογράφηση
  start=timer()
  dr_msg = decrypt(en_msg, p, key, q)
  end=timer()
  print("Χρόνος Εκτέλεσης  Αποκρυπτογράφησης Eλ Γκαμαλ  σε nanoseconds  ",round(((end - start)*1000000000)))# H συνάρτηση επιστρέφει τον χρόνο σε δευτερόλεπτα για λόγους ευκρίνειας το μετατρέπω σε nanoseconds
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






