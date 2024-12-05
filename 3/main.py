from module.numeric_operations import write_numbers_to_file, calculate_difference
from module.text_operations import count_words_and_digits
import os

def main():
    # Задача 1: Работа с числовым файлом
    numeric_file = "numbers.txt"
    numbers = [3.5, 7.2, 10.0, 2.8]
    write_numbers_to_file(numeric_file, numbers)
    if os.path.exists(numeric_file):
        try:
            difference = calculate_difference(numeric_file)
            print(f"Разность первого и последнего числа: {difference:.2f}")
        except ValueError as e:
            print(f"Ошибка: {e}")

    # Задача 2: Работа с текстовым файлом
    text_file = "text.txt"
    with open(text_file, "w") as file:
        file.write("Привет мир 123! Python 3.9 - лучший инструмент.")
    if os.path.exists(text_file):
        words, digits = count_words_and_digits(text_file)
        print(f"Количество слов: {words}, Количество цифр: {digits}")

if __name__ == "__main__":
    main()
