class Person:
  def __init__(self, name, alter, stadt):
    self.name = name
    self.alter = alter
    self.stadt = stadt

  def vorstellen(self):
     print(f"Ich heiße {self.name}, bin {self.alter} Jahre alt und wohne in {self.stadt}.")
  def geburstag(self):
    self.alter += 1
    print(f"Happy Birthday, {self.name}! Du bist jetzt {self.alter}.")


vlad = Person("Vlad", 26, "Duesseldorf")
vlad.vorstellen()
vlad.geburstag()