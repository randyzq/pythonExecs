import unittest

from lesson_3.point import Point

class MyTestCase(unittest.TestCase):
    def test_dist(self):
        p1 = Point((0, 1, 2))
        p2 = Point((1, 2, 3))
        dist = 3 ** 0.5
        result1 = p1.dist(p2)
        result2 = p2.dist(p1)

        self.assertTrue(dist == result1, 'point distance is error!,{0},{1}'.format(dist, result1))
        self.assertTrue(dist == result2, 'point distance is error!,{0},{1}'.format(dist, result2))


if __name__ == '__main__':
    unittest.main()
