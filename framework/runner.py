#!/usr/bin/env python3
import os
import sys
import subprocess
import glob
import json
import re
import argparse
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional

EXERCISES_DIR = "exercises"
TEMPLATES_DIR = "templates"
PROGRESS_FILE = "progress.json"
MARKER = "???"

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

@dataclass
class ExerciseMetadata:
    """Métadonnées extraites du docstring"""
    number: int
    title: str
    difficulty: int
    concepts: List[str]
    description: str
    hints: List[str]
    
class ExerciseRunner:
    def __init__(self):
        self.exercises = []
        
        self.progress = self._load_progress()
    
    def _load_progress(self):
        if os.path.exists(PROGRESS_FILE):
            with open(PROGRESS_FILE, 'r') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    if 'completed' in data:
                        return data.get('completed', {})
                    else:
                        return data
        return {}
    
    def _save_progress(self, exercise_num: int, score: Optional[int] = None):
        if score is not None:
            self.progress[str(exercise_num)] = score
        else:
            self.progress[str(exercise_num)] = True
        with open(PROGRESS_FILE, 'w') as f:
            json.dump(self.progress, f, indent=2)
    
    
    def _reset_exercise_file(self, exercise_num: int) -> bool:
        template_files = sorted(glob.glob(os.path.join(TEMPLATES_DIR, "*.py")))
        for template_file in template_files:
            template_path = Path(template_file)
            match = re.search(r'(\d+)', template_path.stem)
            if match and int(match.group(1)) == exercise_num:
                ex_files = sorted(glob.glob(os.path.join(EXERCISES_DIR, "*.py")))
                for ex_file in ex_files:
                    ex_path = Path(ex_file)
                    ex_match = re.search(r'(\d+)', ex_path.stem)
                    if ex_match and int(ex_match.group(1)) == exercise_num:
                        try:
                            with open(template_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                            with open(ex_path, 'w', encoding='utf-8') as f:
                                f.write(content)
                            return True
                        except Exception as e:
                            print(f"{Colors.RED}Erreur lors de la réinitialisation: {e}{Colors.RESET}")
                            return False
        
        return False
    
    def _reset_all_exercises(self) -> bool:
        template_files = sorted(glob.glob(os.path.join(TEMPLATES_DIR, "*.py")))
        if not template_files:
            print(f"{Colors.RED}Aucun template trouvé dans {TEMPLATES_DIR}/{Colors.RESET}")
            return False
        
        count = 0
        for template_file in template_files:
            template_path = Path(template_file)
            ex_files = sorted(glob.glob(os.path.join(EXERCISES_DIR, "*.py")))
            for ex_file in ex_files:
                ex_path = Path(ex_file)
                if template_path.name == ex_path.name:
                    try:
                        with open(template_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        with open(ex_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        count += 1
                    except Exception as e:
                        print(f"{Colors.RED}Erreur lors de la restauration de {ex_path}: {e}{Colors.RESET}")
                        return False
        
        if count > 0:
            print(f"{Colors.GREEN} {count} exercices restaurés depuis les templates !{Colors.RESET}")
            return True
        return False
    
    def _parse_metadata(self, file_path: Path) -> Optional[ExerciseMetadata]:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"{Colors.RED}Erreur lecture {file_path}: {e}{Colors.RESET}")
            return None
        
        if '"""' not in content:
            print(f"{Colors.YELLOW}  Pas de docstring dans {file_path}{Colors.RESET}")
            return None
        
        start = content.find('"""') + 3
        end = content.find('"""', start)
        if end == -1:
            print(f"{Colors.YELLOW}  Docstring incomplet dans {file_path}{Colors.RESET}")
            return None
        
        docstring = content[start:end]
        
        lines = docstring.split('\n')
        metadata = {}
        description_lines = []
        hints = []
        in_description = False
        
        for line in lines:
            line = line.strip()
            
            try:
                if line.startswith('EXERCISE:'):
                    metadata['number'] = int(line.split(':')[1].strip())
                elif line.startswith('TITLE:'):
                    metadata['title'] = line.split(':', 1)[1].strip()
                elif line.startswith('DIFFICULTY:'):
                    metadata['difficulty'] = int(line.split(':')[1].strip())
                elif line.startswith('CONCEPTS:'):
                    concepts = line.split(':', 1)[1].strip()
                    metadata['concepts'] = [c.strip() for c in concepts.split(',')]
                elif line == '---':
                    in_description = not in_description
                elif line.startswith('HINT:'):
                    hints.append(line.split(':', 1)[1].strip())
                elif in_description and line:
                    description_lines.append(line)
            except (ValueError, IndexError) as e:
                print(f"{Colors.YELLOW}  Format invalide dans {file_path}: {e}{Colors.RESET}")
                continue
        
        if 'number' not in metadata:
            match = re.search(r'(\d+)', file_path.stem)
            if match:
                metadata['number'] = int(match.group(1))
            else:
                print(f"{Colors.RED}Impossible d'extraire le numéro d'exercice de {file_path}{Colors.RESET}")
                return None
        
        if 'title' not in metadata:
            print(f"{Colors.RED} TITLE manquant dans {file_path}{Colors.RESET}")
            return None
        
        return ExerciseMetadata(
            number=metadata.get('number', 0),
            title=metadata.get('title', file_path.stem),
            difficulty=metadata.get('difficulty', 1),
            concepts=metadata.get('concepts', []),
            description='\n'.join(description_lines),
            hints=hints
        )
    
    def _has_incomplete_code(self, file_path: Path) -> bool:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '"""' in content:
            start = content.find('"""')
            end = content.find('"""', start + 3)
            if end != -1:
                content = content[:start] + content[end + 3:]
        
        return MARKER in content
    
    def _print_header(self, metadata: ExerciseMetadata, current: int, total: int):
        print(f"\n{'='*70}")
        print(f"{Colors.BOLD} Exercice {current}/{total}: {metadata.title}{Colors.RESET}")
        print(f"   Difficulté: {'⭐' * metadata.difficulty}")
        if metadata.concepts:
            print(f"   Concepts: {Colors.CYAN}{', '.join(metadata.concepts)}{Colors.RESET}")
        
        completed = sum(1 for ex_num in self.progress.values() if ex_num)
        progress_pct = (completed / total * 100) if total > 0 else 0
        bar_length = 20
        filled = int(bar_length * completed / total) if total > 0 else 0
        bar = '█' * filled + '░' * (bar_length - filled)
        
        print(f"   Progression: [{bar}] {completed}/{total} ({progress_pct:.0f}%)")
        print('='*70)
    
    
    def run_exercise(self, file_path: Path, metadata: ExerciseMetadata) -> bool:
        if self._has_incomplete_code(file_path):
            print(f"{Colors.YELLOW}  Le code contient encore des '{MARKER}' à compléter{Colors.RESET}")
            return False

        print(f"\n{Colors.BOLD}  Exécution de ton code...{Colors.RESET}\n")
        try:
            result = subprocess.run(
                [sys.executable, str(file_path)],
                capture_output=True,
                text=True,
                timeout=10
            )
        except subprocess.TimeoutExpired:
            print(f"{Colors.RED} Timeout: Le code a mis trop de temps à s'exécuter (>10s){Colors.RESET}")
            return False

        # Affiche la sortie
        if result.stdout:
            print(result.stdout)

        if result.returncode != 0:
            print(f"\n{Colors.RED} Erreur détectée :{Colors.RESET}")
            print(result.stderr)
            return False

        # Succès !
        print(f"\n{Colors.GREEN}{Colors.BOLD} PARFAIT ! Exercice réussi !{Colors.RESET}")
        self._save_progress(metadata.number)
        return True
    
    def run_all(self, reset: bool = False):
        
        if reset:
            self._reset_all_exercises()
            self.progress = {}
            with open(PROGRESS_FILE, 'w') as f:
                json.dump({}, f, indent=2)
            print(f"{Colors.GREEN} Progression réinitialisée !{Colors.RESET}")
        
        print(f"\n{Colors.BOLD}{Colors.BLUE}🐍 Python Learning Path{Colors.RESET}")
        
        pattern = os.path.join(EXERCISES_DIR, "*.py")
        exercise_files = sorted(glob.glob(pattern))
        
        if not exercise_files:
            print(f"{Colors.RED}Aucun exercice trouvé dans {EXERCISES_DIR}/{Colors.RESET}")
            return
        
        total = len(exercise_files)
        
        
        completed_count = len(self.progress)
        
        if completed_count > 0:
            print(f"{Colors.GREEN} {completed_count}/{total} exercices déjà complétés{Colors.RESET}\n")
        
        for i, ex_file in enumerate(exercise_files, 1):
            ex_path = Path(ex_file)
            metadata = self._parse_metadata(ex_path)
        
            if not metadata:
                continue
            
            if self.progress.get(str(metadata.number)):
                continue
            
            self._print_header(metadata, i, total)
            
            success = self.run_exercise(ex_path, metadata)
            
            if not success:
                print(f"\n{Colors.YELLOW} Édite le fichier : {Colors.BOLD}{ex_path}{Colors.RESET}")
                print(f"{Colors.BLUE}   Puis relance : {Colors.BOLD}python3 main.py{Colors.RESET}\n")
                return
        
        self._show_victory(total)
    
    def _show_victory(self, total: int):
        print(f"\n{'='*70}")
        print(f"{Colors.GREEN}{Colors.BOLD}")
        print("   🎉 FÉLICITATIONS ! 🎉")
        print(f"{Colors.RESET}")
        print(f"{Colors.GREEN}Tu as complété tous les {total} exercices !{Colors.RESET}")
        print('='*70)
        
        quiz_scores = {}
        for key, value in self.progress.items():
            try:
                num = int(key)
                if 16 <= num <= 18:
                    if isinstance(value, int):
                        quiz_scores[num] = value
                    else:
                        quiz_scores[num] = 5
            except (ValueError, TypeError):
                pass
        
        if quiz_scores:
            print(f"\n{Colors.CYAN}📊 Scores des quiz :{Colors.RESET}")
            total_quiz_score = 0
            for quiz_num in sorted(quiz_scores.keys()):
                score = quiz_scores[quiz_num]
                if isinstance(score, int):
                    total_quiz_score += score
                    print(f"   • Quiz {quiz_num - 15}: {score}/5 ⭐")
            
            if len(quiz_scores) == 3:
                avg_score = total_quiz_score / 3
                rating = "🌟 Parfait !" if avg_score >= 4.5 else "✨ Très bien !" if avg_score >= 4 else "👍 Bien !"
                print(f"\n   Moyenne: {avg_score:.1f}/5 {rating}")
        
        concepts_count = {}
        for ex_file in glob.glob(os.path.join(EXERCISES_DIR, "*.py")):
            metadata = self._parse_metadata(Path(ex_file))
            if metadata:
                for concept in metadata.concepts:
                    concepts_count[concept] = concepts_count.get(concept, 0) + 1
        
        if concepts_count:
            print(f"\n{Colors.CYAN}📚 Concepts maîtrisés :{Colors.RESET}")
            for concept, count in sorted(concepts_count.items(), key=lambda x: -x[1]):
                print(f"   • {concept}: {count} exercice{'s' if count > 1 else ''}")
        
        print(f"\n{Colors.BOLD}Tu es maintenant prêt(e) pour des projets plus avancés ! 🚀{Colors.RESET}\n")

def main():
    parser = argparse.ArgumentParser(description=' Python Learning Path - Exercices progressifs')
    parser.add_argument('--reset', action='store_true',
                        help='Réinitialise la progression (remet tous les exercices comme non-complétés)')
    parser.add_argument('--reset-exercise', type=int, metavar='N',
                        help='Réinitialise l\'exercice N et le retire de la progression')
    
    args = parser.parse_args()
    
    runner = ExerciseRunner()
    
    if args.reset_exercise:
        if runner._reset_exercise_file(args.reset_exercise):
            if str(args.reset_exercise) in runner.progress:
                del runner.progress[str(args.reset_exercise)]
                with open(PROGRESS_FILE, 'w') as f:
                    json.dump(runner.progress, f, indent=2)
            print(f"{Colors.GREEN} Exercice {args.reset_exercise:03d} réinitialisé !{Colors.RESET}")
            print(f"{Colors.CYAN}Édite {EXERCISES_DIR}/{args.reset_exercise:03d}_*.py pour recommencer{Colors.RESET}\n")
        else:
            print(f"{Colors.RED} Impossible de trouver l'exercice {args.reset_exercise:03d}{Colors.RESET}\n")
        return
    
    runner.run_all(reset=args.reset)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Programme interrompu{Colors.RESET}")
        sys.exit(0)
