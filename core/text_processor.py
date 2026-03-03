import re
import nltk
from typing import List, Tuple, Optional
import pymorphy3

# Скачиваем необходимые ресурсы NLTK
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    nltk.download('punkt_tab')


class TextProcessor:
    """Класс для обработки и нормализации текста"""

    def __init__(self, language: str = 'russian'):
        self.language = language
        self.morph = pymorphy3.MorphAnalyzer() if language == 'russian' else None

    def tokenize_sentences(self, text: str) -> List[str]:
        """Разбивает текст на предложения"""
        # Используем NLTK для токенизации предложений
        sentences = nltk.sent_tokenize(text, language='russian')
        return [s.strip() for s in sentences if s.strip()]

    def tokenize_words(self, text: str) -> List[str]:
        """Разбивает текст на слова"""
        # Простая токенизация через регулярные выражения
        words = re.findall(r'\b[а-яА-ЯёЁ]+\b', text)
        return words

    def normalize_text(self, text: str) -> str:
        """Базовая нормализация текста"""
        # Приводим к нижнему регистру
        text = text.lower()
        # Убираем лишние пробелы
        text = re.sub(r'\s+', ' ', text)
        # Убираем спецсимволы (оставляем буквы, цифры и базовую пунктуацию)
        text = re.sub(r'[^\w\s.,!?;:()-]', '', text)
        return text.strip()

    def lemmatize_word(self, word: str) -> str:
        """Лемматизация слова (приведение к нормальной форме)"""
        if self.morph:
            return self.morph.parse(word)[0].normal_form
        return word

    def get_sentences_with_metadata(self, text: str) -> List[dict]:
        """Получает предложения с метаданными"""
        sentences = self.tokenize_sentences(text)
        result = []

        for i, sentence in enumerate(sentences):
            words = self.tokenize_words(sentence)
            lemmas = [self.lemmatize_word(w) for w in words]

            result.append({
                'id': i,
                'text': sentence,
                'words': words,
                'lemmas': lemmas,
                'word_count': len(words)
            })

        return result