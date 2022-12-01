#!/usr/bin/env bash

set -euo pipefail

if [ $# != 1 ]; then
  printf "Usage:\n\t%s <day>\n" "$0" 1>&2
  exit 1
fi

day="$1"

python_template=$(cat <<EOF
from src.common import Solution


class Day${day}(Solution):

    def part1(self, input: str) -> int:
        return -1

    def part2(self, input: str) -> int:
        return -1


EOF
)

python_test_template=$(cat <<EOF
from src.day${day} import Day${day}
from test.testcommon import SolutionTest


class TestDay${day}(SolutionTest):
    example = '''
'''
    input = SolutionTest._read_file_to_string("day${day}_input.txt")

    def test_part1_example(self):
        assert Day${day}().part1(self.example) == 0

    def test_part1(self):
        assert Day${day}().part1(self.input) == 0

    def test_part2_example(self):
        assert Day${day}().part2(self.example) == 0

    def test_part2(self):
        assert Day${day}().part2(self.input) == 0

EOF
)

rootdir="$(dirname "${BASH_SOURCE[0]}")"
cd "$rootdir"

if [ -e "src/day${day}.py" ]; then
  printf "Day %s already exists.\n" "$day" 1>&2
  exit 1
fi

echo "$python_template" > "src/day${day}.py"
echo "$python_test_template" > "test/test_day${day}.py"
touch "test/resources/day${day}_input.txt"
