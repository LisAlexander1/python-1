from complex import ComplexNumber

class ComplexNumberPair(ComplexNumber):
    # Конструктор
    def __init__(self, real1=0, imag1=0, real2=0, imag2=0):
        # Создаем два объекта ComplexNumber
        self.first = ComplexNumber(real1, imag1)
        self.second = ComplexNumber(real2, imag2)
        print(f"ComplexNumberPair created with {self.first} and {self.second}")

    # Деструктор
    def __del__(self):
        print(f"ComplexNumberPair destroyed with {self.first} and {self.second}")

    # Вычислить произведение двух комплексных чисел
    def multiply(self):
        real_part = self.first.real * self.second.real - self.first.imag * self.second.imag
        imag_part = self.first.real * self.second.imag + self.first.imag * self.second.real
        return ComplexNumber(real_part, imag_part)

    # Формирование строки информации об объекте
    def __str__(self):
        return f"First: {self.first}, Second: {self.second}"

# Демонстрация работы
if __name__ == "__main__":
    pair = ComplexNumberPair(1, 2, 3, 4)
    print("Класс-потомок (Пара комплексных чисел):", pair)
    product = pair.multiply()
    print("Произведение двух чисел:", product)
