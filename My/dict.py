person = {
  "name": "Vlad",
  "alter": "26",
  "stadt": "Duesseldorf"
}
#Wert ändern
person["name"] = "Vladyslav"

#Wert hinzufügen
person["hobby"] = "tennis"
person["LVL"] = "20"

print("Name:", person["name"], "Alter:", person["alter"], "Kommt aus:", person["stadt"], person["hobby"], person["LVL"])

# Wert löschen

del person["LVL"]
print(person)