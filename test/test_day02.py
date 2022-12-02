from src.day02 import Day02
from test.testcommon import SolutionTest


class TestDay02(SolutionTest):
    example = '''A Y
B X
C Z
'''
    input = SolutionTest._read_file_to_string("day02_input.txt")

    def test_part1_example(self):
        assert Day02().part1(self.example) == 15

    def test_part1(self):
        assert Day02().part1(self.input) == 11150

    def test_part2_example(self):
        assert Day02().part2(self.example) == 12

    def test_part2(self):
        assert Day02().part2(self.input) == 8295
