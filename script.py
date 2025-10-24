#!/usr/bin/env python3

# Variablen speichern Werte
name = "Alice"  # String
alter = 25  # Integer

# Wert einer Variable ändern
alter = 26

# Typumwandlung (Casting)
alter_str = str(alter)  # Integer zu String

# Werte ausgeben
print("Name:", name)
print("Alter:", alter_str)

# Gleitkommazahl zu Ganzzahl casten
hoehe = 175.5  # Float
hoehe_int = int(hoehe)  # Float zu Integer

# Ergebnis ausgeben
print("Höhe als Ganzzahl:", hoehe_int)

# Listen sind eine Art Container, in dem Sie mehrere Werte speichern können.
meine_zahlen_liste = [1, 2, 3, 4, 5]
meine_buchstaben_liste = ["a", "b", "c", "d", "e"]
meine_gemischte_liste = [1, "a", 2, "b", 3, "c"]

# hinzufügen von Werten
meine_zahlen_liste.append(6)

# Wert ausgeben
print("meine_zahlen_liste:", meine_zahlen_liste)
print("1. Wert in der Liste meine_zahlen_liste:", meine_zahlen_liste[0])
print("2. Wert in der Liste meine_zahlen_liste:", meine_zahlen_liste[1])

# Wert ändern
meine_zahlen_liste[0] = 0
print("1. Wert in der Liste meine_zahlen_liste:", meine_zahlen_liste[0])

# Wert löschen
print("meine_zahlen_liste vor dem Löschen:", meine_zahlen_liste)
meine_zahlen_liste.remove(0)
print("meine_zahlen_liste nach dem Löschen:", meine_zahlen_liste)

# Länge der Liste
print("Länge der Liste meine_zahlen_liste:", len(meine_zahlen_liste))

# Dictonaries sind eine ebenfalls Art Container, in dem Sie mehrere Werte 
# speichern können, jedoch mit einem Key-Value.
mein_dictonary = {"name": "Alice", 
                  "alter": 25}
print("Name:", mein_dictonary["name"])

# Wert ändern
mein_dictonary["name"] = "Bob"
print("Name:", mein_dictonary["name"])

# Wert hinzufügen
mein_dictonary["hobby"] = "schwimmen"
print("Hobby:", mein_dictonary["hobby"])

# Wert löschen
print("mein_dictonary vor dem Löschen:", mein_dictonary)
del mein_dictonary["hobby"]
print("mein_dictonary nach dem Löschen:", mein_dictonary)


# Aufgabe:
# Legen Sie eine Integer-Variable meine_variable mit dem Wert 5 an,
# casten Sie diese in eine Float-Variable und geben Sie das Ergebnis aus.
meine_variable = 5
meine_variable_float = float(meine_variable)
print("Meine Variable:", meine_variable, "Meine Variable Float", meine_variable_float)