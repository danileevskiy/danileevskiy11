class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def name(self) -> str:
        self._name = self._name
        return self._name

    def author(self) -> str:
        self._author = self._author
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = None
        self.pages = pages

    def pages(self):
        return self._pages

    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self._pages = value

    def __str__(self):
        return super().__str__() + f". Количество страниц {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = None
        self.duration = duration

    def duration(self):
        return self._duration

    def duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def __str__(self):
        return super().__str__() + f". Продолжительность {self.duration}"
