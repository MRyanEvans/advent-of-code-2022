from src.common import Solution


class Day01(Solution):

    def part1(self, input: str) -> int:
        return max(count_calories(input))

    def part2(self, input: str) -> int:
        return sum(sorted(count_calories(input), reverse=True)[0:3])


def count_calories(input: str):
    return [sum([int(meal) for meal in elf.splitlines()]) for elf in input.split("\n\n")]
