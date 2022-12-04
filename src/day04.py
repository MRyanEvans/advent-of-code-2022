from src.common import Solution, split_into_chunks_of_size


def envelops(first, second):
    return min(first) <= min(second) and max(first) >= max(second)


def parse_pairs(input):
    return [
        split_into_chunks_of_size([int(n) for n in line.replace('-', ',').split(',')], 2)
        for line in input.splitlines()
    ]


class Day04(Solution):

    def part1(self, input: str) -> int:
        return len([
            (first, second) for first, second in parse_pairs(input)
            if envelops(first, second) or envelops(second, first)
        ])

    def part2(self, input: str) -> int:
        return len([
            (first, second) for first, second in parse_pairs(input)
            if not (max(second) < min(first) or min(second) > max(first))
        ])
