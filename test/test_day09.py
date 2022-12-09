from src.day09 import Day09
from test.testcommon import SolutionTest


class TestDay09(SolutionTest):
    example = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''
    example2 = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
'''
    input = SolutionTest._read_file_to_string("day09_input.txt")

    def test_part1_example(self):
        assert Day09().part1(self.example) == 13

    def test_part1(self):
        assert Day09().part1(self.input) == 6090

    def test_part2_example(self):
        assert Day09().part2(self.example2) == 36

    def test_part2(self):
        assert Day09().part2(self.input) == 2566
