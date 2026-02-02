"""
EXERCISE: 004
TITLE: Manipulation de chaînes
DIFFICULTY: 2
CONCEPTS: strings, concatenation, f-strings
---
En Python, on peut manipuler les chaînes de plusieurs façons :

Concaténation (coller des chaînes) :
    prenom = "Marie"
    nom = "Dupont"
    complet = prenom + " " + nom  → "Marie Dupont"

F-strings (formatage moderne) :
    age = 25
    message = f"J'ai {age} ans"  → "J'ai 25 ans"

Complète les variables ci-dessous.
---
HINT: Pour concaténer, utilise + entre les chaînes
HINT: N'oublie pas l'espace : " " entre prénom et nom
HINT: Les f-strings commencent par f" et utilisent {variable}
HINT: salutation = prenom + " " + nom, presentation = f"Je suis {prenom}"
"""

# Variables à compléter
prenom = ???
nom = ???

# Concatène prénom et nom avec un espace
salutation = ???  # ex: prenom + " " + nom

# Utilise une f-string pour créer une phrase
age = ???
presentation = ???  # ex: f"Je suis {prenom} et j'ai {age} ans"

# Tests
assert salutation == "Alice Martin", f"salutation incorrect : {salutation}"
assert presentation == "Je suis Alice et j'ai 28 ans", f"presentation incorrect : {presentation}"

print(f"Bravo !")
print(f"  Salutation : {salutation}")
print(f"  Présentation : {presentation}")