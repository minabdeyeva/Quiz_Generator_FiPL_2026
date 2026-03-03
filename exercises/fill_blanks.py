import random
from typing import Dict, Any, List
from exercises.base import BaseExercise


class FillBlanksExercise(BaseExercise):
    """Упражнение на заполнение пропусков"""

    def __init__(self, exercise_id: str):
        super().__init__(exercise_id, "Заполните пропуски подходящими словами")
        self.word_bank: List[str] = []

    def generate(self, context: Dict[str, Any]) -> None:
        """Генерирует упражнение с пропусками"""
        sentence = context.get('sentence', '')
        words = context.get('words', [])

        if len(words) < 3:
            raise ValueError("Предложение слишком короткое для создания пропусков")

        # Выбираем случайное слово для пропуска
        blank_index = random.randint(0, len(words) - 1)
        blank_word = words[blank_index]

        # Создаем банк слов (правильное слово + случайные из контекста)
        self.word_bank = [blank_word]

        # Добавляем случайные слова из других предложений
        other_words = context.get('other_words', [])
        if other_words:
            # Берем до 3 случайных слов
            random_words = random.sample(other_words, min(3, len(other_words)))
            self.word_bank.extend(random_words)

        # Перемешиваем банк слов
        random.shuffle(self.word_bank)

        # Формируем вопрос с пропуском
        words_with_blank = words.copy()
        words_with_blank[blank_index] = '_____'
        self.question = ' '.join(words_with_blank)

        self.answer = blank_word
        self.options = self.word_bank

    def validate_answer(self, user_answer: str) -> bool:
        """Проверяет, правильно ли заполнен пропуск"""
        return user_answer.lower().strip() == self.answer.lower()