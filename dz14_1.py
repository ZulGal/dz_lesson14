# Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
# 2-5 тестов на задание в трёх вариантах:
# - doctest,
# - unittest,
# - pytest.

class Person:
    """
    Класс хранит инфо о человеке
    >>> p1 = Person('Ivanov','Ivan','Ivanovich', 40)
    >>> p1.birthday()
    >>> p1.get_age()
    41
    >>> p1.get_full_name()
    'Ivanov Ivan Ivanovich'
    >>> p1 = Person('ivanov','12van','Ivanovich', 40)
    Traceback (most recent call last):
    ...
    ValueError: Первая буква ivanov должна быть заглавной

    >>> p1 = Person('Ivanov','12van','Ivanovich', 40)
    Traceback (most recent call last):
    ...
    TypeError: 12van должна состоять только из букв

    >>> p1 = Person('Ivanov','Ivan','Ivanovich', 4000)
     Traceback (most recent call last):
    ...
    ValueError: Возраст 4000 должен находиться между 18 и 100 годами

    """

    def __init__(self, surname, name, patronymic, age):
        if not surname.isalpha():
            raise ValueError(f'{surname} должна состоять только из букв')
        elif not surname[0].isupper():
            raise ValueError(f'Первая буква {surname} должна быть заглавной')
        self.surname = surname
        if not name.isalpha():
            raise TypeError(f'{name} должна состоять только из букв')
        elif not name[0].isupper():
            raise ValueError(f'Первая буква {name} должна быть заглавной')
        self.name = name
        if not patronymic.isalpha():
            raise TypeError(f'{patronymic} должна состоять только из букв')
        elif not patronymic[0].isupper():
            raise ValueError(f'Первая буква {patronymic} должна быть заглавной')
        self.patronymic = patronymic
        if 18 < age < 100:
            self.__age = age
        else:
            raise ValueError(f'Возраст {age} должен находиться между 18 и 100 годами')

    def get_age(self):
        """Получает текущий возраст"""
        return self.__age

    def birthday(self):
        """Увеличивает возраст на год"""
        self.__age += 1

    def get_surname(self):
        return self.surname

    def get_name(self):
        return self.name

    def get_patronymic(self):
        return self.patronymic

    def get_full_name(self):
        """Выводит полное ФИО"""
        return f'{self.get_surname()} {self.get_name()} {self.get_patronymic()}'


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
