import random

def Intro():
  print("--- Taschenrechner ---")
  print("Willkommen zum Taschenrechner, bitte gebe an was du machen willst.")
  print(
      "\n1. Zufallszahl\n2. Taschenrechner\n3. Irgendwas\n4. Münze werfen\n5. Programm stoppen"
  )

def Menue():
  print("--- Taschenrechner ---")
  print("Willkommen zum Taschenrechner, bitte gebe an was du machen willst.")
  print(
      "\n1. Zufallszahl\n2. Taschenrechner\n3. Irgendwas\n4. Münze werfen\n5. Programm stoppen"
  )

def Programme():

  if tool == str(1):
    numOne = int(input("Gebe eine Zahl ein: "))
    numTow = int(input("Gebe eine Zahl ein: "))
    randomNumber = random.randint(numOne, numTow)
    print(randomNumber)

  elif tool == str(2):
    rechnung=input("Was möchtest du rechnen? ")
    ergebniss=eval(rechnung)
    print("Dein Ergebniss ist:", ergebniss)

  elif tool == str(3):
    irgendwas=random.randint(1,4)
    print("Nimm doch nächstes mal", irgendwas, "!")

  elif tool == str(4):
    print("Ich werfe jetzt eine Münze")
    coin = random.randint(1, 2)
    if coin == 1:
      print("Das Ergebniss ist Kopf")
    else:
      print("Das Ergebniss ist Zahl")

  elif tool == str(5):
    print("Bis zum nächsten mal!")
    exit()

  else:
    print("---")
    print("Bitte gebe eine Valide eingabe ab!")



Intro()
tool=input("Worauf hast du lust? ")
Programme()