from src.day11 import Day11
from test.testcommon import SolutionTest


class TestDay11(SolutionTest):
    example = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''
    input = SolutionTest._read_file_to_string("day11_input.txt")

    def test_part1_example(self):
        assert Day11().part1(self.example) == 10605

    def test_part1(self):
        assert Day11().part1(self.input) == 51075

    def test_part2_example(self):
        assert Day11().part2(self.example) == 2713310158

    def test_part2(self):
        assert Day11().part2(self.input) == 11741456163
