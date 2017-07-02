from math import sqrt
from .distance_abstract import DistanceAbstract


class EuclideanDistance(DistanceAbstract):
    def measure(cls, list1, list2):
        distance = 0
        min_len = min(len(list1), len(list2))

        for i in range(0, min_len):
            distance += sqrt(abs(list1[i]**2 - list2[i]**2))

        return distance
