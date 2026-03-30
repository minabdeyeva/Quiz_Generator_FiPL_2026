# Архитектура проекта
## Структура
```
exercise_generator/
├── README.md                    # Пользовательская документация
├── requirements.txt             
├── .gitignore                   
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml             
│
├── src/
│   └── exercise_generator/
│       │
│       ├── core/
│       │   ├── __init__.py
│       │   ├── text_processor.py        # Обработка текстов
│       │   └── document_loader.py       # Загрузка разных форматов
│       │
│       ├── exercises/
│       │   ├── __init__.py
│       │   ├── base.py                 # Базовый класс упражнения
│       │   ├── word_order.py           # Перестановки слов
│       │   ├── fill_blanks.py          # Вставка слов
│       │   ├── multiple_choice.py      # Множественный выбор
│       │   ├── matching.py             # Соответствие
│       │   └── true_false.py           # Верно/Неверно
│       │
│       ├── generators/
│       │   ├── __init__.py
│       │   └── exercise_generator.py   # Основной класс генератора
│       │
│       ├── formatters/
│       │   ├── __init__.py
│       │   └── docx_formatter.py       # Форматирование в docx
│       │
│       └── web/
│           ├── app.py                  # Запуск локального сервера
│           └── templates/
│               ├── about.html          # Страница с информацией
│               └── index.html          # Основная страница с карточками
│
├── tests/
│   ├── __init__.py
│   ├── test_base_module.py             # Тесты для base.py
│   ├── test_document_loader.py         # Тесты для document_loader.py
│   ├── test_docx_formatter.py          # Тесты для docx_formatter.py
│   ├── test_exercise_generator.py      # Тесты для exercise_generator.py
│   ├── test_fill_blanks_exercise.py    # Тесты для fill_blanks.py
│   ├── test_matching_exercise.py       # Тесты для matching.py
│   ├── test_run_generator.py           # Тесты для run_generator.py
│   ├── test_synonyms_exercise.py       # Тесты для synonyms.py
│   ├── test_text_processor.py          # Тесты для text_processor
│   ├── test_true_false_exercise.py     # Тесты для true_false.py
│   ├── test_word_order.py              # Тесты для word_order.py 
│   └── test_word_vectorizer.py         # Тесты для word_vectorizer.py
│
└── docs/
    ├── README.md                       # Техническая документация
    └── ARCHITECTURE.md                 # Архитектура проекта
```
[описание классов и модулей]
## Диаграммы
[UML или текстовые диаграммы]
## Взаимодействие компонентов
[описание как работают части]
