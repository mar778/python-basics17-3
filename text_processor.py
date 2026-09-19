python
"""
Обработчик текста на Python.
Демонстрирует работу со строками и списками.
"""

def count_words(text):
    """Считает количество слов в тексте."""
    words = text.split()
    return len(words)

def reverse_text(text):
    """Переворачивает текст задом наперёд."""
    return text[::-1]

if __name__ == "__main__":
    text = "Привет, мир!"
    print(count_words(text))   # 2
    print(reverse_text(text))  # !рим ,тевирП
