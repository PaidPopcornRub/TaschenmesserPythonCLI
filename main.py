import random

print("--- Taschenrechner ---")
print("Willkommen zum Taschenrechner, bitte gebe an was du machen willst.")
print("\n1. Zufallszahl\n2. Taschenrechner\n3. Irgendwas\n4. Programm stoppen")

tool = input("Worauf hast du lust? ")

if tool == str(1):
  numOne = int(input("Gebe eine Zahl ein: "))
  numTow = int(input("Gebe eine Zahl ein: "))
  randomNumber = random.randint(numOne, numTow)
  print(randomNumber)

elif tool == str(2):
  print("aschenrechner")
  
elif tool == str(3):
  print()
  
elif tool == str(4):
  print("Bis zum nächsten mal!")
  exit()
  

else:
  print("---")
  print("Bitte gebe eine Valide eingabe ab!")
