"""
EXERCISE: 007
TITLE: Conditions if/else
DIFFICULTY: 3
CONCEPTS: if, else, elif, conditionals
---
Les conditions permettent d'exécuter du code selon une condition :

Structure de base :
    if condition:
        # code si la condition est vraie
    else:
        # code si la condition est fausse

Avec plusieurs conditions :
    if age < 18:
        statut = "mineur"
    elif age < 65:
        statut = "adulte"
    else:
        statut = "senior"

IMPORTANT : L'indentation (4 espaces) est OBLIGATOIRE en Python !

Complète le code pour déterminer si un nombre est positif, négatif ou zéro.
---
HINT: Utilise if, elif, else pour tester les conditions
HINT: Teste d'abord si nombre > 0, puis si nombre < 0
HINT: N'oublie pas les deux-points : après chaque condition
HINT: Indente le code avec 4 espaces après les :
"""

nombre = 15

# Complète cette structure conditionnelle
if ???:
    resultat = "positif"
elif ???:
    resultat = "négatif"
else:
    resultat = "zéro"

# Tests avec différentes valeurs
def tester_nombre(n):
    if n > 0:
        return "positif"
    elif n < 0:
        return "négatif"
    else:
        return "zéro"

assert resultat == "positif", f"Pour 15, le résultat devrait être 'positif'"

# Test avec d'autres valeurs
nombre = -5
if nombre > 0:
    resultat = "positif"
elif nombre < 0:
    resultat = "négatif"
else:
    resultat = "zéro"
assert resultat == "négatif", f"Pour -5, le résultat devrait être 'négatif'"

nombre = 0
if nombre > 0:
    resultat = "positif"
elif nombre < 0:
    resultat = "négatif"
else:
    resultat = "zéro"
assert resultat == "zéro", f"Pour 0, le résultat devrait être 'zéro'"

print("Excellent ! Tu maîtrises les conditions !")
print(f"Les tests avec différents nombres sont tous corrects !")