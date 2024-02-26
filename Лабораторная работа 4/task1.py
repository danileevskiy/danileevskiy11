from typing import List

class Animal:
    """Базовый класс, представляющий животное."""

    def __init__(self, name: str, species: str, age: int):
        """
        Инициализация объекта Animal.

        Args:
            name: Имя животного.
            species: Вид животного.
            age: Возраст животного.
        """
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self) -> str:
        """Издать звук, характерный для данного животного."""
        pass

    def __str__(self) -> str:
        """Возвращает строковое представление животного."""
        return f"{self.species} по имени {self.name}"

    def __repr__(self) -> str:
        """Возвращает строковое представление для отладки."""
        return f"{self.__class__.__name__}(name={self.name}, species={self.species}, age={self.age})"

class Dog(Animal):
    """Класс, представляющий собаку, наследующий от Animal."""

    def __init__(self, name: str, age: int, breed: str):
        """
        Инициализация объекта Dog.

        Args:
            name: Имя собаки.
            age: Возраст собаки.
            breed: Порода собаки.
        """
        super().__init__(name, "Собака", age)
        self.breed = breed

    def make_sound(self) -> str:
        """Собака лает."""
        return "Гав-гав!"

    def __str__(self) -> str:
        """
        Возвращает строковое представление собаки.

        Перегружено для добавления информации о породе.
        """
        return f"{super().__str__()}, порода: {self.breed}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление для отладки.

        Перегружено для более информативного вывода.
        """
        return f"{self.__class__.__name__}(name={self.name}, age={self.age}, breed={self.breed})"

class Cat(Animal):
    """Класс, представляющий кошку, наследующий от Animal."""

    def __init__(self, name: str, age: int, color: str):
        """
        Инициализация объекта Cat.

        Args:
            name: Имя кошки.
            age: Возраст кошки.
            color: Окрас кошки.
        """
        super().__init__(name, "Кошка", age)
        self.color = color

    def make_sound(self) -> str:
        """Кошка мяукает."""
        return "Мяу!"

    def __str__(self) -> str:
        """
        Возвращает строковое представление кошки.

        Перегружено для добавления информации об окрасе.
        """
        return f"{super().__str__()}, окрас: {self.color}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление для отладки.

        Перегружено для более информативного вывода.
        """
        return f"{self.__class__.__name__}(name={self.name}, age={self.age}, color={self.color})"
