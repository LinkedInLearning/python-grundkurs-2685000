#!/usr/bin/env python3

# Eingaben über die Kommandozeile

# Einlesen eines Strings
name = input("Bitte geben Sie Ihren Namen ein: ")
print("Hallo, " + name + "!")

# Einlesen eines Integers und Umwandlung
alter = input("Bitte geben Sie Ihr Alter ein: ")
alter = int(alter)
print("Sie sind", alter, "Jahre alt.")
print("Sie sind " + str(alter) + " Jahre alt.")

# Berechnung mit der Eingabe
jahre_bis_30 = 30 - alter
if jahre_bis_30 > 0:
    print("In " + str(jahre_bis_30) + " Jahren werden Sie 30.")
else:
    print("Sie sind bereits 30 Jahre alt oder älter.")

# Aufgabe:
# Schreiben Sie ein Skript, das den Benutzer nach seinem Lieblingsfilm fragt
# und nach seiner Lieblingszahl. Addieren Sie 14.5 zu dieser Zahl. Geben Sie 
# dann eine personalisierte Nachricht aus, die diese Informationen enthält.
lieblingsfilm = input("Geben Sie ihren Lieblingsfilm an.")
lieblingszahl = input("Wie lautet ihre Lieblingszahl?")
lieblingszahl = int(lieblingszahl)
lieblingszahl += 14.5
print("Lieblingsfilm lautet " + lieblingsfilm + " und Zahl + 14.5 ist " + str(lieblingszahl))