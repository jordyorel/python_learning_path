"""
EXERCISE: 013
TITLE: Méthodes de listes
DIFFICULTY: 1
CONCEPTS: list methods, append, remove
---
Méthodes pour modifier les listes :

    .append(element)  → ajoute à la fin
    .remove(element)  → enlève la première occurrence
    .pop()            → enlève et retourne le dernier

Exemples :
    fruits = ["pomme"]
    fruits.append("banane")  → ["pomme", "banane"]
    fruits.remove("pomme")   → ["banane"]
---
HINT: .append() ajoute un élément à la fin
HINT: .remove() enlève un élément spécifique
HINT: animaux.append("chat")
HINT: animaux.remove("oiseau")
"""

animaux = ["chien", "oiseau"]

# Ajoute "chat" à la liste
???

# Enlève "oiseau" de la liste
???

# Tests
assert animaux == ["chien", "chat"], f"Attendu ['chien', 'chat'], reçu {animaux}"

print("Tu sais modifier les listes !")