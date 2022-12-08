from src.day08 import Day08
from test.testcommon import SolutionTest


class TestDay08(SolutionTest):
    example = '''30373
25512
65332
33549
35390
'''
    input = SolutionTest._read_file_to_string("day08_input.txt")

    def test_part1_example(self):
        assert Day08().part1(self.example) == 21

    def test_part1(self):
        assert Day08().part1(self.input) == 1763

    def test_part2_example(self):
        assert Day08().part2(self.example) == 8

    def test_part2(self):
        assert Day08().part2(self.input) == 671160
