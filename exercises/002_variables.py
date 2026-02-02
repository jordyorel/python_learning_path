"""
EXERCISE: 002
TITLE: Variables et types
DIFFICULTY: 2
CONCEPTS: variables, int, string
---
En Python, on stocke des valeurs dans des variables avec = :

    age = 25           # nombre entier (int)
    nom = "Alice"      # chaîne de texte (string)
    taille = 1.75      # nombre décimal (float)

IMPORTANT :
- Les nombres n'ont PAS de guillemets
- Les textes DOIVENT avoir des guillemets (simples ou doubles)

Complète le code ci-dessous.
---
HINT: Remplace ??? par une valeur
HINT: Pour un texte, utilise des guillemets : "ton texte"
HINT: Pour un nombre, pas de guillemets : 25
HINT: Vérifie que 'nom' est bien un texte et 'age' un nombre
"""

# Complète ces variables
nom = ???
age = ???

# Ne touche pas au code de test
assert isinstance(nom, str), "nom doit être une chaîne de texte"
assert isinstance(age, int), "age doit être un nombre entier"
assert len(nom) > 0, "nom ne peut pas être vide"
assert age > 0, "age doit être positif"

print(f"Bravo ! Je m'appelle {nom} et j'ai {age} ans")