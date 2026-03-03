import os
from pathlib import Path
from typing import List, Union
import chardet


class DocumentLoader:
    """Класс для загрузки документов разных форматов"""

    @staticmethod
    def load_text(file_path: Union[str, Path]) -> str:
        """Загружает текст из файла"""
        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"Файл {file_path} не найден")

        # Определяем кодировку
        with open(file_path, 'rb') as f:
            raw_data = f.read()
            encoding = chardet.detect(raw_data)['encoding'] or 'utf-8'

        # Загружаем в зависимости от расширения
        if file_path.suffix.lower() == '.txt':
            return DocumentLoader._load_txt(file_path, encoding)
        elif file_path.suffix.lower() == '.md':
            return DocumentLoader._load_md(file_path, encoding)
        elif file_path.suffix.lower() == '.docx':
            return DocumentLoader._load_docx(file_path)
        else:
            raise ValueError(f"Неподдерживаемый формат файла: {file_path.suffix}")

    @staticmethod
    def _load_txt(file_path: Path, encoding: str) -> str:
        """Загружает текстовый файл"""
        with open(file_path, 'r', encoding=encoding) as f:
            return f.read()

    @staticmethod
    def _load_md(file_path: Path, encoding: str) -> str:
        """Загружает markdown файл (просто читаем как текст)"""
        with open(file_path, 'r', encoding=encoding) as f:
            return f.read()

    @staticmethod
    def _load_docx(file_path: Path) -> str:
        """Загружает docx файл"""
        try:
            from docx import Document
            doc = Document(file_path)
            return '\n'.join([paragraph.text for paragraph in doc.paragraphs])
        except ImportError:
            raise ImportError("Для загрузки docx файлов установите python-docx")