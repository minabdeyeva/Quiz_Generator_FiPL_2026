import random
from typing import Dict, Any
from exercises.base import BaseExercise


class MultipleChoiceExercise(BaseExercise):
    """Упражнение с множественным выбором"""

    def __init__(self, exercise_id: str):
        super().__init__(exercise_id, "Выберите правильный вариант ответа")

    def generate(self, context: Dict[str, Any]) -> None:
        """Генерирует вопрос с вариантами ответов"""
        sentence = context.get('sentence', '')
        words = context.get('words', [])

        if not words:
            words = sentence.split()

        # Выбираем слово для вопроса (например, найти синоним)
        target_word = random.choice(words)

        # Формируем вопрос
        self.question = f"Какое слово является синонимом к слову '{target_word}'?"

        # В реальном проекте здесь должен быть словарь синонимов
        # Для демо используем заглушку
        correct_answer = target_word  # В реальности это должен быть синоним

        # Создаем варианты ответов
        self.options = [
            correct_answer,
            "вариант 1",
            "вариант 2",
            "вариант 3"
        ]
        random.shuffle(self.options)

        self.answer = correct_answer

    def validate_answer(self, user_answer: str) -> bool:
        """Проверяет выбранный вариант"""
        return user_answer == self.answer
