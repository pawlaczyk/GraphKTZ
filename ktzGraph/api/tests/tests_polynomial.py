#coding=utf-8
import unittest
import numpy as np
from sympy import symbols
import pytest

from ktzGraph.api.adjacency_matrix.implmentation.polynomial import PolynomialCalculator


class PolynomialCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.symbol = symbols('x')

    def test_proper_matrix_should_pass(self):
        matrix = np.array([[0, 1], [1, 0]])
        polynomial_calculator = PolynomialCalculator(matrix)
        polynomial = polynomial_calculator.calculate_polynomial()
        expected_result = 1.0 * self.symbol**2 -1
        self.assertEqual(polynomial, expected_result)

        matrix = np.array([[1, 0], [0, 1]])
        polynomial_calculator = PolynomialCalculator(matrix)
        polynomial = polynomial_calculator.calculate_polynomial()
        expected_result = (1.0*self.symbol - 1)**2
        self.assertEqual(polynomial, expected_result)
