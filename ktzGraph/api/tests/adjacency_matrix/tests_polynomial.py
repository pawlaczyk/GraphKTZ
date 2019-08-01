# coding=utf-8
import unittest
import numpy as np
from sympy import symbols

from ktzGraph.api.adjacency_matrix.implmentation.polynomial import PolynomialCalculator, EigenvaluesCalculator


class PolynomialCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.symbol = symbols('x')
        self.k1 = np.array([[0, 1], [1, 0]])

    def test_proper_matrix_should_pass(self):
        polynomial_calculator = PolynomialCalculator(self.k1)
        polynomial = polynomial_calculator.get_polynomial()
        expected_result = 1.0 * self.symbol**2 -1
        self.assertEqual(polynomial, expected_result)

        matrix = np.array([[1, 0], [0, 1]])
        polynomial_calculator = PolynomialCalculator(matrix)
        polynomial = polynomial_calculator.get_polynomial()
        expected_result = (1.0*self.symbol - 1)**2
        self.assertEqual(polynomial, expected_result)


class EigenvaluesCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.k1 = np.array([[0, 1], [1, 0]])

    def test_proper_matrix_should_pass(self):
        eigenvalues_calculator = EigenvaluesCalculator(self.k1)

        result = eigenvalues_calculator.get_eigenvalues()
        expected_result = [1.0, -1.0]
        self.assertEqual(expected_result, result)

        result = eigenvalues_calculator.get_unique_eigenvalues()
        expected_result = [1.0, -1.0]
        self.assertEqual(expected_result, result)
