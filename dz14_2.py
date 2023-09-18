import unittest
from dz14_1 import Person
# from task10_3 import get_full_name
import task10_3


class TestCaseName(unittest.TestCase):
    def test_1_get_full_name(self):
        p1 = Person('Ivanov', 'Ivan', 'Ivanovich', 40)
        self.assertEqual(p1.get_full_name(), 'Ivanov Ivan Ivanovich')

    def test_1_get_age(self):
        p1 = Person('Ivanov', 'Ivan', 'Ivanovich', 40)
        p1.birthday()
        self.assertEqual(p1.get_age(), 41)

    def test_2_get_full_name(self):
        with self.assertRaises(ValueError):
            p1 = Person('ivanov', 'Ivan', 'Ivanovich', 40)
            p1.get_full_name()
            p1 = Person('Ivanov', 'Ivan', 'Ivanovich', 4000)
            p1.get_full_name()

    def test_3_get_full_name(self):
        with self.assertRaises(TypeError):
            p1 = Person('Ivanov', '12van', 'Ivanovich', 40)
            p1.get_full_name()


if __name__ == '__main__':
    unittest.main(verbosity=2)
