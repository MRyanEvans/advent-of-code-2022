import os
from abc import ABC, abstractmethod


class SolutionTest(ABC):

    @abstractmethod
    def test_part1_example(self):
        pass

    @abstractmethod
    def test_part1(self):
        pass

    @abstractmethod
    def test_part2_example(self):
        pass

    @abstractmethod
    def test_part2(self):
        pass

    @staticmethod
    def _find_file(name):
        for root, dirs, files in os.walk("."):
            if name in files:
                return os.path.join(root, name)

    @staticmethod
    def _read_file_to_string(name):
        path = SolutionTest._find_file(name)
        if path is None:
            raise "No file found with name " + name
        with open(path, 'r') as file:
            return file.read()
