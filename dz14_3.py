import pytest
from dz14_1 import Person


def test_1_get_full_name():
    p1 = Person('Ivanov', 'Ivan', 'Ivanovich', 40)
    assert p1.get_full_name() == 'Ivanov Ivan Ivanovich', 'Тест один не пройден !'


def test_2_get_age():
    p1 = Person('Ivanov', 'Ivan', 'Ivanovich', 40)
    p1.birthday()
    assert p1.get_age() == 41, 'Тест один не пройден !'


def test_3_value():
    p1 = Person('ivanov', 'Ivan', 'Ivanovich', 40)
    with pytest.raises(ValueError, match=r'Первая буква {surname} должна быть заглавной'):
        p1.get_full_name()


def test_4_value():
    p1 = Person('Ivanov', '12van', 'Ivanovich', 40)
    with pytest.raises(ValueError, match=r'{name} должна состоять только из букв'):
        p1.get_full_name()


def test_5_value():
    p1 = Person('Ivanov', 'Ivan', 'Ivanovich', 4000)
    with pytest.raises(ValueError, match=r'Возраст {age} должен находиться между 18 и 100 годами'):
        p1.get_full_name()


if __name__ == '__main__':
    pytest.main(['--vv'])
