# Python Learning Path

Un projet éducatif interactif pour apprendre Python en résolvant des exercices progressifs. Inspiré par [Ziglings](https://codeberg.org/ziglings)

## Objectifs

- Apprendre les concepts fondamentaux de Python
- Progresser graduellement du basique au intermédiaire
- Apprendre en pratiquant (learn by doing)
- Recevoir des indices progressifs en cas d'erreur
- Tracker ta progression

## Démarrage rapide

### Prérequis

- Python 3.7+

### Installation

```bash
git clone https://github.com/jordyorel/python_learning_path.git
cd python_learning_path
```

### Lancer les exercices

```bash
# Démarre le premier exercice non-complété
python3 main.py

# Recommencer à zéro (réinitialise la progression)
python3 main.py --reset

# Réinitialiser un exercice spécifique (ex: exercice 5)
python3 main.py --reset-exercise 1
```

## Comment utiliser

### 1 Résoudre un exercice

Quand tu lances `python3 main.py`, tu vois le premier exercice non-complété :

```

L'exercice contient du code avec des marqueurs `???` à remplacer.

### 2 Éditer le fichier

Ouvre le fichier indiqué (ex: `exercises/001_hello.py`) et remplace les `???` par ta solution :

### 3 Vérifier ta solution

Relance le programme pour vérifier :

```bash
python3 main.py
```

## Suivi de progression

Ta progression est sauvegardée dans `progress.json` :

```json
{
  "1": true,
  "2": true,
  "3": false
}
```

**Avantage**: Si tu modifies accidentellement un exercice ou veux recommencer, tu peux utiliser `--reset-exercise N` pour restaurer la version propre du template. Ou utilise `--reset` pour tout recommencer depuis zéro !

## Bonnes pratiques

1. **Progresse en ordre** - Les exercices doivent être faits dans l'ordre
2. **Lis les descriptions** - Chaque exercice enseigne un concept
3. **Utilise les indices** - Ils te guident progressivement

## Prochaines étapes après les exercices

Après avoir complété tous les exercices, tu es prêt pour :

- Lire un tutoriel Python complet
- Faire des petits projets (calculatrice, jeu, scraper web)
- Consulter la [documentation officielle Python](https://docs.python.org/3/)
- Essayer des défis sur [Exercism.org](https://exercism.org/), [LeetCode](https://leetcode.com/), [HackerRank](https://www.hackerrank.com/)

## Licence

MIT - Tu peux utiliser ce projet librement !

## Contribution

Des suggestions ou corrections ? Ouvert aux contributions !

---

**Bon apprentissage ! Happy coding! **
