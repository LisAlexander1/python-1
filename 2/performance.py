class Performance:
    def __init__(self, title, n1, n2):
        """
        Конструктор класса Performance.
        :param title: Название спектакля
        :param n1: Число зрителей в начале
        :param n2: Число зрителей в конце
        """
        self.title = title
        self.n1 = n1
        self.n2 = n2

    def quality(self):
        """
        Вычисление качества спектакля Q.
        :return: Q = (n2 - n1) / n1
        """
        if self.n1 == 0:
            raise ValueError("Число зрителей в начале (n1) не может быть равно нулю.")
        return (self.n2 - self.n1) / self.n1

    def __str__(self):
        """
        Вывод информации об объекте.
        """
        return f"Спектакль: {self.title}, Зрители: начало={self.n1}, конец={self.n2}, Качество (Q)={self.quality():.2f}"
