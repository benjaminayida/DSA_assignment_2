import unittest
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius**2


# Unit Test Class
class TestCircleMethods(unittest.TestCase):
    def test_calculate_perimeter(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.calculate_perimeter(), 2 * math.pi * 5, places=2)

    def test_calculate_area(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.calculate_area(), math.pi * 3**2, places=2)


if __name__ == '__main__':
    unittest.main()
