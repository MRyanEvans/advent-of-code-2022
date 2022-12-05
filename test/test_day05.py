from src.day05 import Day05
from test.testcommon import SolutionTest


class TestDay05(SolutionTest):
    example = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
    input = SolutionTest._read_file_to_string("day05_input.txt")

    def test_part1_example(self):
        assert Day05().part1(self.example) == "CMZ"

    def test_part1(self):
        assert Day05().part1(self.input) == "FRDSQRRCD"

    def test_part2_example(self):
        assert Day05().part2(self.example) == "MCD"

    def test_part2(self):
        assert Day05().part2(self.input) == "HRFTQVWNN"
