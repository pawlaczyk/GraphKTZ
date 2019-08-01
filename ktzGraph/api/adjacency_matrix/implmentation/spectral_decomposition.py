# coding=utf-8
from itertools import combinations
from typing import List, Dict
#TODO Logi do debugowania

import numpy as np

from ktzGraph.api.adjacency_matrix.graph_constants import GraphConstants
from ktzGraph.api.adjacency_matrix.implmentation.polynomial import EigenvaluesCalculator


class SpectralDecompositionCalculator:  # TODO czy juz nie ma za dużo odpowiedzialnosci [open-closed]?
    def __init__(self, adjacency_matrix: np.array):
        self.adjacency_matrix = adjacency_matrix

    def get_projections(self):
        """Utworzenie wszystkich projekcji poprzez kolejne usuwanie wierzchołka -
        w każdym kroku brana jest macierz oryginalna i usuwany jest kolejny jeden wierzchołek
        Liczba projekcji wynosi n; gdzie n to liczba wierzchołków"""

        projections = []
        for i in range(self.adjacency_matrix.shape[0]):
            arr = np.delete(self.adjacency_matrix, i, axis=0)
            arr2 = np.delete(arr, i, axis=1)
            eigenvalues_calculator = EigenvaluesCalculator(arr2)  # TODO zastanowić się nad obiektem EigenvaluesCalculator
            projections.append({"vertex": i, "matrix": arr2, "spectrum": eigenvalues_calculator.get_eigenvalues()})

        return projections

    def get_strong_projections(self)->np.array:
        """Utworzenie wszystkich projekcji poprzez kolejne usuwanie wierzchołka -
        w każdym kroku brana jest macierz oryginalna i usuwany jest kolejny jeden wierzchołek
        Liczba projekcji wynosi n; gdzie n to liczba wierzchołków"""
        indexes = list(combinations([n for n in range(self.adjacency_matrix.shape[0])], 2))

        strong_projections = []
        for i,j in indexes:
            arr = np.delete(self.adjacency_matrix, i, axis=0)
            arr = np.delete(arr, i, axis=0)

            arr2 = np.delete(arr, i, axis=1)
            arr2 = np.delete(arr2, i, axis=1)

            eigenvalues_calculator = EigenvaluesCalculator(arr2)  # TODO zastanowić się nad obiektem EigenvaluesCalculator
            strong_projections.append(
                {"vertex_i": i, "vertex_j": j, "matrix": arr2, "spectrum": eigenvalues_calculator.get_eigenvalues(arr2)})
        return strong_projections

    @staticmethod
    def compare_spectral_list(l1: List, l2: List) -> bool:
        """Porównywanie spektrum macierzy"""
        l1.sort()
        l2.sort()
        for i in range(len(l1)):
            if abs(l1[i] - l2[i]) > GraphConstants.EPSILON.value:
                return 0
        return 1

    def get_cospectral_matrix(self)->Dict:
        """Zwraca binarną macierz kospektralności grafu
        Uwaga: Każdy wierzchołek jest kospektralny sam ze sobą"""
        projections = self.get_strong_projections()  # słownik: macierz, wierzchołek, SP
        spectral_matrix = np.identity(self.adjacency_matrix.shape[0])

        for i in projections:
            vertex_i = i["vertex"]
            for j in projections:
                vertex_j = j["vertex"]
                spectral_matrix[vertex_i][vertex_j] = self.compare_spectral_list(i["spectrum"], j["spectrum"])

        return spectral_matrix

    def strong_cospectral_matrix(self)->Dict:
        strong_projections = self.get_strong_projections()
        strong_spectral_matrix = np.identity(self.adjacency_matrix.shape[0])

        for i in strong_projections:
            vertex_i = i["vertex"]
            for j in strong_projections:
                vertex_j = j["vertex"]
                strong_spectral_matrix[vertex_i][vertex_j] = self.compare_spectral_list(i["spectrum"], j["spectrum"])
        return strong_spectral_matrix
