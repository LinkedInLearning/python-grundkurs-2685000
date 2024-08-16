#!/usr/bin/env python3

# Einführung in Klassen in Python

class Buch:
    """Eine einfache Klasse zur Darstellung eines Buches im Bücherregal."""

    def __init__(self, titel: str, autor: str):
        """Initialisiert das Buch mit einem Titel und einem Autor."""
        self.titel = titel  # Öffentliches Attribut
        self.autor = autor  # Öffentliches Attribut
        self._status = "verfügbar"  # Privates Attribut, das den Ausleihstatus des Buches angibt

    def ausleihen(self):
        """Markiert das Buch als ausgeliehen, wenn es verfügbar ist."""
        if self._status == "verfügbar":
            self._status = "ausgeliehen"
            print(f"Das Buch '{self.titel}' wurde ausgeliehen.")
        else:
            print(f"Das Buch '{self.titel}' ist bereits ausgeliehen.")

    def zurückgeben(self):
        """Markiert das Buch als verfügbar."""
        if self._status == "ausgeliehen":
            self._status = "verfügbar"
            print(f"Das Buch '{self.titel}' wurde zurückgegeben.")
        else:
            print(f"Das Buch '{self.titel}' ist bereits verfügbar.")

    def get_status(self) -> str:
        """Gibt den aktuellen Ausleihstatus des Buches zurück."""
        return self._status

class Bücherregal:
    """Eine Klasse zur Verwaltung eines Bücherregals."""

    def __init__(self):
        """Initialisiert das Bücherregal als leeres Regal."""
        self._bücher = []  # Privates Attribut, das eine Liste von Büchern speichert

    def buch_hinzufügen(self, buch: Buch):
        """Fügt ein Buch zum Bücherregal hinzu."""
        self._bücher.append(buch)
        print(f"Das Buch '{buch.titel}' wurde dem Regal hinzugefügt.")

    def buch_entfernen(self, buch: Buch):
        """Entfernt ein Buch aus dem Bücherregal."""
        if buch in self._bücher:
            self._bücher.remove(buch)
            print(f"Das Buch '{buch.titel}' wurde aus dem Regal entfernt.")
        else:
            print(f"Das Buch '{buch.titel}' ist nicht im Regal.")

    def alle_bücher_anzeigen(self):
        """Zeigt alle Bücher im Bücherregal an."""
        if self._bücher:
            print("Bücher im Regal:")
            for buch in self._bücher:
                status = buch.get_status()
                print(f" - {buch.titel} von {buch.autor} (Status: {status})")
        else:
            print("Das Bücherregal ist leer.")

# Erstellung von Büchern
buch1 = Buch("Der Hobbit", "J.R.R. Tolkien")
print("Titel lautet", buch1.titel)  # Zugriff auf das öffenliche Attribut 'titel'
buch2 = Buch("1984", "George Orwell")
print("Autor lautet", buch2.autor)  # Zugriff auf das öffenliche Attribut 'autor'
print("Status lautet", buch2.get_status())  # Zugriff auf das private Attribut 'status' durch eine Methode
print("Status lautet", buch2._status)  # 'Fehler': Zugriff auf ein privates Attribut

# Erstellung eines Bücherregals und Hinzufügen von Büchern
regal = Bücherregal()
regal.buch_hinzufügen(buch1)
regal.buch_hinzufügen(buch2)

# Anzeige aller Bücher im Regal
regal.alle_bücher_anzeigen()

# Ausleihen eines Buches
buch1.ausleihen()

# Versuch, dasselbe Buch erneut auszuleihen
buch1.ausleihen()

# Rückgabe eines Buches
buch1.zurückgeben()

# Anzeige des Status der Bücher
regal.alle_bücher_anzeigen()

# Aufgabe:
# Erstellen Sie eine Klasse 'Ebike', die die Eigenschaften 'marke', 'modell' und 'reichweite' hat.
# - Implementieren Sie eine Methode 'tanken', die die Reichweite um einen gegebenen Wert erhöht.
# - Stellen Sie sicher, dass der Tankinhalt privat ist und nur über eine Methode abgefragt werden kann.
# - Instanzieren Sie ein Elektrofahrrad und testen Sie die Methoden.

class Ebike:
    """Eine Klasse zur Darstellung eines Elektrofahrrads."""

    def __init__(self, marke: str, modell: str, reichweite: int):
        """Initialisiert das Elektrofahrrad mit Marke, Modell und Reichweite."""
        self.marke = marke  # Öffentliches Attribut
        self.modell = modell  # Öffentliches Attribut
        self.__reichweite = reichweite  # Privates Attribut, das die aktuelle Reichweite speichert

    def tanken(self, zusätzliche_reichweite: int):
        """Erhöht die Reichweite des Elektrofahrrads um einen gegebenen Wert."""
        self.__reichweite += zusätzliche_reichweite
        print(f"Die Reichweite des Elektrofahrrads wurde um {zusätzliche_reichweite} km erhöht.")

    def get_reichweite(self) -> int:
        """Gibt die aktuelle Reichweite des Elektrofahrrads zurück."""
        return self.__reichweite
    
# Instanzieren eines Elektrofahrrads
ebike = Ebike("MyFancyBike", "Active Cruiser", 50)
print("Marke:", ebike.marke)
print("Modell:", ebike.modell)
print("Reichweite:", ebike.get_reichweite())
ebike.tanken(20)
print("Neue Reichweite:", ebike.get_reichweite())