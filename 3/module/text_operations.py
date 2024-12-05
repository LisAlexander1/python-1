def count_words_and_digits(filename):
    """
    Считает количество слов и цифр в текстовом файле.
    :param filename: Имя файла для анализа.
    :return: Кортеж (количество слов, количество цифр).
    """
    with open(filename, "r") as file:
        text = file.read()
    words = text.split()
    word_count = len(words)
    digit_count = sum(c.isdigit() for c in text)
    return word_count, digit_count