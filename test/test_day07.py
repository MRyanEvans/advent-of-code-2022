from src.day07 import Day07
from test.testcommon import SolutionTest


class TestDay07(SolutionTest):
    example = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''
    input = SolutionTest._read_file_to_string("day07_input.txt")

    def test_part1_example(self):
        assert Day07().part1(self.example) == 95437

    def test_part1(self):
        assert Day07().part1(self.input) == 1723892

    def test_part2_example(self):
        assert Day07().part2(self.example) == 24933642

    def test_part2(self):
        assert Day07().part2(self.input) == 8474158
