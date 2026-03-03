from generators.exercise_generator import ExerciseGenerator


def main():
    # Создаем генератор
    gen = ExerciseGenerator(language='french')

    # Вариант 1: Если файлы уже существуют - просто передаем пути
    # Не нужно их предварительно читать!
    gen.load_texts(['Bafta_2026_«_Une_bataille_après_l’autre_»_triomphe_avec_six_récompenses.txt'])

    # Генерируем упражнения
    exercises = gen.generate_exercises(num_per_type=2)

    # Сохраняем результаты
    gen.save_exercises(exercises, 'exercises.docx')
    gen.save_answers(exercises, 'answers_key.docx')

    print("\n✓ Проект успешно выполнен!")


if __name__ == "__main__":
    main()