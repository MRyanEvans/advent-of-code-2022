from src.day03 import Day03
from test.testcommon import SolutionTest


class TestDay03(SolutionTest):
    example = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''
    input = SolutionTest._read_file_to_string("day03_input.txt")

    def test_part1_example(self):
        assert Day03().part1(self.example) == 157

    def test_part1(self):
        assert Day03().part1(self.input) == 7597

    def test_part2_example(self):
        assert Day03().part2(self.example) == 70

    def test_part2(self):
        assert Day03().part2(self.input) == 2607
