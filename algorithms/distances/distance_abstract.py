from abc import ABCMeta, abstractmethod


class DistanceAbstract(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def measure(cls, list1, list2):
        pass
