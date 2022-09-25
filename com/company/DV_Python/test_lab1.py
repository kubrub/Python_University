import unittest
import com.company.DV_Python.lab1


class TestStringMethods(unittest.TestCase):

    def test_task_1(self):
        self.assertEqual(com.company.DV_Python.lab1.task1([3, 28, -4, 901, 666, -25, -25, 700, -1, 0]), (5, 4, -13.75))

    def test_task_3(self):
        self.assertEqual(com.company.DV_Python.lab1.task3('i love Ukraine'), 'i\nlove\nUkraine')

    def test_task_2_various_triangle(self):
        self.assertEqual(com.company.DV_Python.lab1.task_2(6, 5, 4), 'various')

    def test_task_2_isosceles_triangle(self):
        self.assertEqual(com.company.DV_Python.lab1.task_2(5, 5, 4), 'isosceles')

    def test_task_2_equilateral_triangle(self):
        self.assertEqual(com.company.DV_Python.lab1.task_2(3, 3, 3), 'equilateral')

    def test_task_2_impossible_triangle(self):
        self.assertEqual(com.company.DV_Python.lab1.task_2(1, 2, 4), 'impossible')

    def test_task_2_sides_less_zeros1(self):
        self.assertEqual(com.company.DV_Python.lab1.task_2(-1, 2, 3), 'do not mean sides')

    def test_task_2_sides_less_zeros2(self):
        self.assertEqual(com.company.DV_Python.lab1.task_2(1, -2, 3), 'do not mean sides')

    def test_task_2_sides_less_zeros3(self):
        self.assertEqual(com.company.DV_Python.lab1.task_2(1, 2, -3), 'do not mean sides')

    def test_task_2_sides_less_zeros4(self):
        self.assertEqual(com.company.DV_Python.lab1.task_2(-1, -2, -3), 'do not mean sides')

    def test_task_2_various_triangle_double(self):
        self.assertEqual(com.company.DV_Python.lab1.task_2(6.6, 5, 4), 'various')

    def test_task_2_isosceles_triangle_double(self):
        self.assertEqual(com.company.DV_Python.lab1.task_2(7.7, 7.7, 4), 'isosceles')

    def test_task_2_equilateral_triangle_double(self):
        self.assertEqual(com.company.DV_Python.lab1.task_2(3.1, 3.1, 3.1), 'equilateral')

    def test_task_2_impossible_triangle_double(self):
        self.assertEqual(com.company.DV_Python.lab1.task_2(1.1, 2.6, 4.9), 'impossible')

    def test_task_2_sides_less_zeros1_double(self):
        self.assertEqual(com.company.DV_Python.lab1.task_2(-1, 2, 3.4), 'do not mean sides')

    def test_task_2_sides_less_zeros2_double(self):
        self.assertEqual(com.company.DV_Python.lab1.task_2(1, -2.4, 3), 'do not mean sides')

    def test_task_2_sides_less_zeros3_double(self):
        self.assertEqual(com.company.DV_Python.lab1.task_2(1, 2, -3.1), 'do not mean sides')

    def test_task_2_sides_less_zeros4_double(self):
        self.assertEqual(com.company.DV_Python.lab1.task_2(-1.9, -2.1, -3), 'do not mean sides')

    def test_task_3(self):
        self.assertEqual(com.company.DV_Python.lab1.findMaxSum([[1, 2, -1, -4],
                                                                [-8, -3, 4, 2],
                                                                 [3, 8, 10, 1],
                                                                 [-4, -1, 1, 7]]),29)


if __name__ == '__main__':
    unittest.main()