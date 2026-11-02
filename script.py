#!/usr/bin/env python3

# Aufgabe: Programmieren Sie einen einfachen Taschenrechner

# Ihr Taschenrechner soll folgende Funktionen unterstützen:
# - Addition (+)
# - Subtraktion (-)
# - Multiplikation (*)
# - Division (/)

# Der Benutzer sollte aufgefordert werden, zwei Zahlen einzugeben.
# Anschließend sollte der Benutzer die gewünschte Operation wählen können.

# Beispielablauf:
# 1. Benutzer gibt die erste Zahl ein.
# 2. Benutzer gibt die zweite Zahl ein.
# 3. Benutzer wählt die Operation (+, -, *, /).
# 4. Das Programm führt die Berechnung durch und gibt das Ergebnis aus.

# Optional: Erweitern Sie den Taschenrechner um weitere Funktionen wie Potenzierung oder Modulo.
zahl1=input("Zahl 1: ")
operation=input("Operation: +,-,/ oder *.")
zahl2=input("Zahl 2: ")

zahl1=int(zahl1)
zahl2=int(zahl2)

print(zahl1,operation,zahl2)

if(operation=="+"):
  ergebnis=zahl1+zahl2
  print("Ergebnis von Addition:",ergebnis)

elif (operation=="-"):
  ergebnis=zahl1-zahl2
  print("Ergebnis von Subtraktion:",ergebnis)

elif (operation=="/"):
  ergebnis=zahl1/zahl2
  print("Ergebnis von Division:",ergebnis)

elif(operation=="*"):
  ergebnis=zahl1*zahl2
  print("Ergebnis von Multiplikation:",ergebnis)

