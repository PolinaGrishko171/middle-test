import re
from collections import Counter

def read_file(file_path):
    """Зчитує вміст текстового файлу."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def clean_text(text):
    """Очищує текст від пунктуації та приводить до нижнього регістру."""
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower()

def count_words(text):
    """Підраховує кількість входжень кожного слова у тексті."""
    words = text.split()
    return Counter(words)

def get_top_words(word_counts, n=10):
    """Повертає список із n найпопулярніших слів."""
    return word_counts.most_common(n)

def save_results(results, output_file):
    """Записує результати у файл у форматі слово-кількість."""
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in results:
            file.write(f"{word}-{count}\\n")

if __name__ == "__main__":
    input_file = "input.txt"  # Вхідний файл
    output_file = "output.txt"  # Файл для результатів

    text = read_file(input_file)
    cleaned_text = clean_text(text)
    word_counts = count_words(cleaned_text)
    top_words = get_top_words(word_counts)
    save_results(top_words, output_file)
    print("Результати збережено у output.txt")
 
