from src.common import Solution


def index_of_distinct_marker_size(marker_length, buffer):
    for i in range(marker_length, len(buffer) + 1):
        last_n = buffer[i - marker_length:i]
        if len(set(last_n)) == len(last_n):
            return i


class Day06(Solution):

    def part1(self, input: str) -> [int]:
        return [index_of_distinct_marker_size(4, buffer) for buffer in input.splitlines()]

    def part2(self, input: str) -> [int]:
        return [index_of_distinct_marker_size(14, buffer) for buffer in input.splitlines()]
