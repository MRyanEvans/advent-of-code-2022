from src.day01 import Day01
from test.testcommon import SolutionTest


class TestDay01(SolutionTest):
    example = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''
    input = SolutionTest._read_file_to_string("day01_input.txt")

    def test_part1_example(self):
        assert Day01().part1(self.example) == 24000

    def test_part1(self):
        assert Day01().part1(self.input) == 72718

    def test_part2_example(self):
        assert Day01().part2(self.example) == 45000

    def test_part2(self):
        assert Day01().part2(self.input) == 213089
