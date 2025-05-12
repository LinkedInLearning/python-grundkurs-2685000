#!/usr/bin/env python3

# Einführung in Funktionen mit Typehints

# Funktion zur Addition zweier Zahlen mit Typehints
def addiere(zahl1: int, zahl2: int) -> int:
    return zahl1 + zahl2

# Funktion zur Begrüßung eines Benutzers mit Typehints
def begruessung(name: str) -> str:
    return f"Hallo, {name}!"

# Funktion zur Berechnung des Flächeninhalts eines Rechtecks mit Typehints
def berechne_flaeche(laenge: float, breite: float) -> float:
    """
    Berechnet die Fläche eines Rechtecks.
    Parameters:
      laenge (float): Die Länge des Rechtecks.
      breite (float): Die Breite des Rechtecks.
    Returns:
      float: Die Fläche des Rechtecks.
    """
    
    return laenge * breite

# Aufruf der Funktionen
summe = addiere(10, 5)
print("Die Summe ist:", summe)

gruß = begruessung("Alice")
print(gruß)

flaeche = berechne_flaeche(10.5, 4.3)
print("Die Fläche des Rechtecks ist:", flaeche)

# Aufgabe:
# Schreiben Sie eine Funktion, die die Differenz zweier Zahlen berechnet und zurückgibt.
# Verwenden Sie Typehints, um sicherzustellen, dass beide Argumente und der Rückgabewert Integer sind.
# Was passiert, wenn Sie die Funktion mit Float-Werten aufrufen?
# Rufen Sie diese Funktion auf und geben Sie das Ergebnis aus.
# Tipp: https://code.visualstudio.com/docs/python/linting
#       https://peps.python.org/pep-0008/
