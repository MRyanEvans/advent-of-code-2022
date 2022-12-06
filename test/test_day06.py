from src.day06 import Day06
from test.testcommon import SolutionTest


class TestDay06(SolutionTest):
    example = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'''
    input = SolutionTest._read_file_to_string("day06_input.txt")

    def test_part1_example(self):
        assert Day06().part1(self.example) == [7, 5, 6, 10, 11]

    def test_part1(self):
        assert Day06().part1(self.input) == [1361]

    def test_part2_example(self):
        assert Day06().part2(self.example) == [19, 23, 23, 29, 26]

    def test_part2(self):
        assert Day06().part2(self.input) == [3263]
