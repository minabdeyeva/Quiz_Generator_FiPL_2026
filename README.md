exercise_generator/
│
├── core/
│   ├── __init__.py
│   ├── text_processor.py    # Обработка текстов
│   └── document_loader.py   # Загрузка разных форматов
│
├── exercises/
│   ├── __init__.py
│   ├── base.py              # Базовый класс упражнения
│   ├── word_order.py        # Перестановки слов
│   ├── fill_blanks.py       # Вставка слов
│   ├── multiple_choice.py   # Множественный выбор
│   ├── matching.py          # Соответствие
│   └── true_false.py        # Верно/Неверно
│
├── generators/
│   ├── __init__.py
│   └── exercise_generator.py # Основной класс генератора
│
├── formatters/
│   ├── __init__.py
│   └── docx_formatter.py    # Форматирование в docx
