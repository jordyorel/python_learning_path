"""
EXERCISE: 008
TITLE: Entrée utilisateur
DIFFICULTY: 1
CONCEPTS: input, interaction
---
La fonction input() permet de demander une saisie :

    nom = input("Quel est ton nom ? ")
    print(f"Bonjour {nom}!")

ATTENTION : input() retourne toujours une chaîne de texte.

Pour ce test, on simule l'entrée utilisateur.
---
HINT: input() affiche un message et attend une saisie
HINT: Pour convertir en nombre : int(input("..."))
HINT: reponse = input("Question ?")
HINT: nombre = int(reponse)
"""

# Simule une saisie (ne modifie pas cette ligne)
saisie = "25"

# Convertis la saisie en nombre entier
age = ???

# Tests
assert isinstance(age, int), "age doit être un entier"
assert age == 25, "age doit être 25"

print(f"✓ Tu as {age} ans !")