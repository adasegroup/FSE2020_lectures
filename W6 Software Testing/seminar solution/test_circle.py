#!/usr/bin/env python3

import unittest

import circle


class CircleAreaTestCase(unittest.TestCase):
    def test_valid_input(self):
        valid_radius = 5.1
        valid_area = 81.7128249

        output = circle.compute_area(valid_radius)

        self.assertAlmostEqual(output, valid_area, places=6)

    def test_invalid_input(self):
        invalid_radius = -1
        self.assertRaises(ValueError, circle.compute_area, invalid_radius)

    def test_boundary(self):
        valid_radius = 0.0
        valid_area = 0.0
        output = circle.compute_area(valid_radius)
        self.assertAlmostEqual(output, valid_area, places=6)


from io import StringIO
import sys


class CircleMainTestCase(unittest.TestCase):
    def test_valid_input(self):
        valid_radius = 5.1
        valid_area = 81.7128249

        stdin = sys.stdin
        sys.stdin = StringIO()
        sys.stdin.write(str(valid_radius))
        sys.stdin.flush()
        sys.stdin.seek(0)

        stdout = sys.stdout
        sys.stdout = StringIO()

        circle.main()

        output = float(sys.stdout.getvalue())
        self.assertAlmostEqual(output, valid_area, places=6)

        sys.stdin, sys.stdout = stdin, stdout


class CircleMainTestCaseWithSetUp(unittest.TestCase):
#   def run_tests(self):
#       for name in self.__dict__.keys():
#           if name.startswith('test_'):
#               self.tests.append(name)
#       for test in self.tests:
#           self.setUp()
#           test()
#           self.tearDown()

    def setUp(self):
        self.stdin = sys.stdin
        sys.stdin = StringIO()

        self.stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdin, sys.stdout = self.stdin, self.stdout

    def test_valid_input(self):
        valid_radius = 5.1
        valid_area = 81.7128249

        sys.stdin.write(str(valid_radius))
        sys.stdin.flush()
        sys.stdin.seek(0)

        circle.main()

        output = float(sys.stdout.getvalue())
        self.assertAlmostEqual(output, valid_area, places=6)


from unittest.mock import patch


class CircleMainTestCaseWithMock(unittest.TestCase):
    def test_valid_input(self):
        with patch('sys.stdin', StringIO()) as stdin, \
                patch('sys.stdout', new_callable=StringIO) as stdout:

            valid_radius = 5.1
            valid_area = 81.7128249

            stdin.write(str(valid_radius))
            stdin.flush()
            stdin.seek(0)

            circle.main()

            output = float(stdout.getvalue())
            self.assertAlmostEqual(output, valid_area, places=6)

        print(sys.stdout)


if __name__ == '__main__':
    unittest.main()

