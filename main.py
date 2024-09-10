import random

def Intro():
  print("--- Taschenrechner ---")
  print("Willkommen zum Taschenrechner, bitte gebe an was du machen willst.")
  print("\n1. Zufallszahl\n2. Taschenrechner\n3. Irgendwas\n4. Programm stoppen")

  toolSelect()

def toolSelect():
  tool=input("Worauf hast du lust? ")
  
  if tool == 1:
    Zufallszahl()
  elif tool == 2:
    Taschenrechner()
  elif tool == 3:
    Irgendwas()
  elif tool == 4:
    ProgrammStop()

  else:
    print("---")
    print("Bitte gebe eine Valide eingabe ab!")
    toolSelect()






def Zufallszahl():
  print("true")

def Taschenrechner():
  print("true")

def Irgendwas():
  print("true")

def ProgrammStop():
  exit()

def ui():
  print("true")

def end():
  print("true")

Intro()