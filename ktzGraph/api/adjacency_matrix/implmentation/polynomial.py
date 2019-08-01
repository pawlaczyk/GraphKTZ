#coding=utf-8
import numpy as np
import sympy

from ktzGraph.api.adjacency_matrix.graph_constants import GraphConstants


class PolynomialCalculator:
    def __init__(self, adjacency_matrix:np.array)->None:
        self.adjacency_matrix = adjacency_matrix

    def get_polynomial(self):
        """Calculates polynomial of adjaency matrix"""

        symbol = sympy.Symbol('x')  # Zmienna symboliczna 'x'
        I = np.identity(self.adjacency_matrix.shape[0])  # Utworzenie macierzy jednostkowej
        AI = symbol * I
        P = sympy.Matrix(AI - self.adjacency_matrix)
        polynomial = P.det()  # wyznacznik macierzy symbolicznej
        return polynomial


class EigenvaluesCalculator:
    def __init__(self, adjacency_matrix:np.array)->None:
        self.adjacency_matrix = adjacency_matrix

    def get_eigenvalues(self):
        """[UWAGA!!!] Liczenie wartosci ze stałą epsilon
        Wartości własne macierzy sąsiedztwa grafu"""
        Sp = []
        for i in np.linalg.eig(self.adjacency_matrix)[0]:  # [0] - wartości własne, [1] - wektory własne
            if isinstance(i, complex):
                Sp.append(i)
            if abs(i - round(i)) < GraphConstants.EPSILON.value:
                i = round(i)
                Sp.append(round(i))
            else:
                Sp.append(i)
        Sp.sort(reverse=True)

        return Sp

    def get_unique_eigenvalues(self):
        """Unikalne wartości własne"""
        Sp = self.get_eigenvalues()
        USp = list(set(Sp))
        USp.sort(reverse=True)
        return USp
