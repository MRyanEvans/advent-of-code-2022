from src.day04 import Day04
from test.testcommon import SolutionTest


class TestDay04(SolutionTest):
    example = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''
    input = SolutionTest._read_file_to_string("day04_input.txt")

    def test_part1_example(self):
        assert Day04().part1(self.example) == 2

    def test_part1(self):
        assert Day04().part1(self.input) == 644

    def test_part2_example(self):
        assert Day04().part2(self.example) == 4

    def test_part2(self):
        assert Day04().part2(self.input) == 926
