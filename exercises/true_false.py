import random
from typing import Dict, Any, List
from .base import BaseExercise


class TrueFalseExercise(BaseExercise):
    """Упражнение Верно/Неверно - определить корректность утверждений о тексте"""

    def __init__(self, exercise_id: str):
        super().__init__(exercise_id, "Определите, верны ли следующие утверждения (Верно/Неверно)")
        self.statements: List[
            Dict[str, Any]] = []  # Каждое утверждение: {'text': str, 'is_true': bool, 'explanation': str}

    def generate(self, context: Dict[str, Any]) -> None:
        """Генерирует утверждения на основе текста"""
        sentence = context.get('sentence', '')
        words = context.get('words', [])

        if not sentence:
            raise ValueError("Нет предложения для создания утверждений")

        # Создаем несколько утверждений на основе предложения
        self.statements = self._generate_statements(sentence, words)

        # Формируем вопрос
        self.question = f"Прочитайте предложение и определите, верны ли утверждения:\n\n\"{sentence}\"\n"

        # Добавляем утверждения в вопрос
        for i, stmt in enumerate(self.statements, 1):
            self.question += f"\n{i}. {stmt['text']}"

        # Формируем ответ (все правильные ответы)
        self.answer = [stmt['is_true'] for stmt in self.statements]
        self.options = ['Верно', 'Неверно']

    def _generate_statements(self, sentence: str, words: List[str]) -> List[Dict[str, Any]]:
        """Генерирует набор утверждений (правдивых и ложных) на основе предложения"""
        statements = []

        # Разбиваем предложение на части
        sentence_lower = sentence.lower()

        # 1. Правдивое утверждение - копируем часть предложения
        if len(words) >= 3:
            # Берем первые 3-4 слова как правдивое утверждение
            true_stmt = ' '.join(words[:min(4, len(words))])
            statements.append({
                'text': f"В тексте говорится: \"{true_stmt}...\"",
                'is_true': True,
                'explanation': f"Это верно, так как в предложении есть эти слова"
            })

        # 2. Ложное утверждение - меняем ключевое слово
        if words:
            # Выбираем случайное слово и заменяем его
            word_to_replace = random.choice(words)
            opposite_words = {
                "большой": "маленький",
                "хороший": "плохой",
                "новый": "старый",
                "есть": "нет",
                "любит": "ненавидит",
                "всегда": "никогда",
                "можно": "нельзя",
                "да": "нет"
            }

            # Ищем противоположность
            replacement = opposite_words.get(word_to_replace.lower(), f"не {word_to_replace}")

            false_stmt = sentence.replace(word_to_replace, replacement, 1)
            statements.append({
                'text': false_stmt,
                'is_true': False,
                'explanation': f"Это неверно, потому что в оригинале сказано \"{word_to_replace}\", а не \"{replacement}\""
            })

        # 3. Правдивое утверждение о сути предложения
        # Извлекаем главную мысль (упрощенно)
        main_idea = self._extract_main_idea(sentence, words)
        if main_idea:
            statements.append({
                'text': main_idea,
                'is_true': True,
                'explanation': "Это верно, так как отражает основную мысль предложения"
            })

        # 4. Ложное утверждение с противоположным смыслом
        if len(words) >= 2:
            # Создаем отрицание или противопоставление
            if 'не' in sentence_lower:
                # Если есть "не", убираем его для ложного утверждения
                false_stmt = sentence.replace('не', '', 1)
                statements.append({
                    'text': false_stmt,
                    'is_true': False,
                    'explanation': f"Это неверно, так как в оригинале есть отрицание"
                })
            else:
                # Добавляем "не" для создания ложного утверждения
                if len(words) > 1:
                    # Вставляем "не" перед глаголом (упрощенно)
                    verb_position = self._find_verb_position(words)
                    if verb_position >= 0:
                        words_copy = words.copy()
                        words_copy.insert(verb_position, "не")
                        false_stmt = ' '.join(words_copy)
                        statements.append({
                            'text': false_stmt,
                            'is_true': False,
                            'explanation': "Это неверно, так как в оригинале нет отрицания"
                        })

        # Ограничиваем количество утверждений (максимум 5)
        return statements[:5]

    def _extract_main_idea(self, sentence: str, words: List[str]) -> str:
        """Извлекает основную мысль предложения (упрощенно)"""
        if len(words) < 3:
            return sentence

        # Берем подлежащее и сказуемое (упрощенно)
        # В реальном проекте здесь должен быть синтаксический анализ
        potential_subjects = ["я", "ты", "он", "она", "оно", "мы", "вы", "они", "это", "кто", "что"]

        subject = None
        for word in words:
            if word.lower() in potential_subjects:
                subject = word
                break

        if subject and len(words) > 2:
            # Берем подлежащее и следующие 2-3 слова
            subject_index = words.index(subject)
            end_index = min(subject_index + 3, len(words))
            return ' '.join(words[subject_index:end_index])

        return sentence

    def _find_verb_position(self, words: List[str]) -> int:
        """Находит позицию глагола в списке слов (упрощенно)"""
        # Список частотных глаголов для демо
        common_verbs = ["есть", "быть", "стал", "является", "находится", "работает", "учится",
                        "говорит", "думает", "знает", "хочет", "может", "должен", "любит"]

        for i, word in enumerate(words):
            if word.lower() in common_verbs or word.lower().endswith(('ть', 'ет', 'ит', 'ют', 'ут')):
                return i

        return -1

    def validate_answer(self, user_answer: List[bool]) -> bool:
        """Проверяет ответы на утверждения"""
        if not isinstance(user_answer, list) or len(user_answer) != len(self.statements):
            return False

        return user_answer == self.answer

    def get_explanations(self) -> List[str]:
        """Возвращает пояснения к каждому утверждению"""
        return [stmt['explanation'] for stmt in self.statements]