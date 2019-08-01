#coding=utf-8
import numpy as np
import sympy


class PolynomialCalculator:
    def __init__(self, adjacency_matrix:np.array)->None:
        self.adjacency_matrix = adjacency_matrix

    def calculate_polynomial(self):
        """Calculates polynomial of adjaency matrix"""

        symbol = sympy.Symbol('x')  # Zmienna symboliczna 'x'
        I = np.identity(self.adjacency_matrix.shape[0])  # Utworzenie macierzy jednostkowej
        AI = symbol * I
        P = sympy.Matrix(AI - self.adjacency_matrix)
        polynomial = P.det()  # wyznacznik macierzy symbolicznej
        return polynomial
