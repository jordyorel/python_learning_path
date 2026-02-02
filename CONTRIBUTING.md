# Contribuer à Python Learning Path

Merci de vouloir contribuer ! Voici comment ajouter des exercices ou améliorer le projet.

## 📋 Template pour un nouvel exercice

Crée un fichier `exercises/XXX_titre_court.py` en suivant ce template :

```python
"""
EXERCISE: XXX
TITLE: Titre de l'exercice
DIFFICULTY: 1
CONCEPTS: concept1, concept2, concept3
---
Description claire de ce que l'utilisateur doit faire.

Explique les concepts :
- Point 1
- Point 2

Donne un exemple :
    mon_exemple = "code ici"

Demande à l'utilisateur de compléter le code.
---
HINT: Premier indice (le plus vague)
HINT: Deuxième indice (un peu plus précis)
HINT: Troisième indice (très spécifique)
HINT: Solution finale : mon_code = "valeur"
"""

# Complète ces lignes
variable1 = ???
variable2 = ???

# Tests (ne pas modifier)
assert variable1 == "valeur_attendue", "Erreur message"
assert variable2 == 42, "Erreur message"

print("✓ Excellent ! Tu as réussi !")
```

## 📝 Règles pour le template

### Métadonnées

- **EXERCISE**: Numéro unique (003, 004, etc.)
  - Format: `XXX` (3 chiffres, ex: 001, 002, 010)
  - Les exercices 016-018 sont réservés aux quiz

- **TITLE**: Titre court et clair
  - Max 40 caractères
  - Format: "Concept: Description" (ex: "Boucles: For et While")

- **DIFFICULTY**: 1, 2 ou 3
  - 1 ⭐ = Basique / facile
  - 2 ⭐⭐ = Intermédiaire
  - 3 ⭐⭐⭐ = Avancé / quiz

- **CONCEPTS**: Tags séparés par des virgules
  - 2-4 concepts max
  - Format: "concept1, concept2, concept3"
  - Exemples: "loops, for, range" ou "functions, parameters"

### Description

- Doit être claire et progressive
- Explique le concept à apprendre
- Donne 1-2 exemples concrets
- Termine par une instruction claire

### Indices (HINT)

- **Minimum 3 indices**, idéalement 4
- **Ordre progressif**: du vague au spécifique
  1. Indice général (concept)
  2. Indice technique (syntaxe)
  3. Indice très spécifique (presque la réponse)
  4. Solution (optionnel)

### Code de l'exercice

- Utilise `???` pour marquer les parties à compléter
- **Chaque `???` = 1 élément à compléter** (ex: 1 variable, 1 expression)
- Include des commentaires pour guider
- Les tests doivent vérifier la solution complètement

### Tests

- Utilise `assert` pour valider
- Messages d'erreur clairs et utiles
- Min 2 assertions, idéalement 3-5
- Ne pas modifier les tests = règle du jeu

## Checklist avant de soumettre

- [ ] Numéro d'exercice unique (pas de doublon)
- [ ] EXERCISE, TITLE, DIFFICULTY, CONCEPTS remplis
- [ ] Description claire (5-10 lignes)
- [ ] Au moins 3 indices progressifs
- [ ] Au moins 2 assertions dans les tests
- [ ] Code testé localement et fonctionne
- [ ] Pas de `???` dans le docstring
- [ ] Pas de dépendances externes (juste Python standard)
- [ ] Format: `XXX_titre_court.py` (minuscules, underscores)

## 🧪 Tester ton exercice

```bash
# 1. Ajoute ton fichier dans exercises/
# 2. Teste manuellement que le template fonctionne
python3 exercises/XXX_mon_exercice.py

# 3. Teste avec le runner (exécute le précédent avant)
python3 main.py --reset

# 4. Complète les ??? et vérifie que ça passe
python3 main.py

## Gérer les templates

Après avoir créé ou modifié des exercices, les templates peuvent être mis à jour :

```bash
# Générer les fichiers templates
python3 generate_templates.py

# Réinitialiser un exercice spécifique (restaure depuis le template)
python3 main.py --reset-exercise 5
```

**Note**: Les fichiers dans `templates/` doivent rester "propres" (version d'origine avec `???`). Ne les modifie pas directement.
```

## Améliorer le framework (runner.py)

Tu veux améliorer le système ? Voici les zones clés:

- `_parse_metadata()`: Parser le docstring
- `_has_incomplete_code()`: Vérifier les `???`
- `_show_hints()`: Afficher les indices
- `run_exercise()`: Exécuter et vérifier
- `_show_victory()`: Écran de fin

## 📊 Niveaux de difficulté recommandés

| Difficulté | Concepts | Exemples |
|-----------|----------|----------|
| ⭐ | 1 concept simple | variables, print, types basiques |
| ⭐⭐ | 2-3 concepts ou 1 complexe | listes, conditions, boucles simples |
| ⭐⭐⭐ | Synthèse de concepts | quiz, functions complexes, logique |


Ouvre une issue ou fais une PR ! 🚀

---

Merci de contribuer à rendre Python Learning Path meilleur !
