from src.day12 import Day12
from test.testcommon import SolutionTest


class TestDay12(SolutionTest):
    example = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
'''
    input = SolutionTest._read_file_to_string("day12_input.txt")

    def test_part1_example(self):
        assert Day12().part1(self.example) == 31

    def test_part1(self):
        assert Day12().part1(self.input) == 517

    def test_part2_example(self):
        assert Day12().part2(self.example) == 29

    def test_part2(self):
        assert Day12().part2(self.input) == 512
