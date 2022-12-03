from src.common import Solution, split_into_chunks_of_size, halve_list, find_common_element


def calc_priority(char):
    if ord(char) >= 96:
        return ord(char) - 96
    else:
        return ord(char) - 38


class Day03(Solution):

    def part1(self, input: str) -> int:
        rucksacks = [halve_list(list(rucksack)) for rucksack in input.splitlines()]
        common_elements = [find_common_element(rucksack) for rucksack in rucksacks]
        priorities = [calc_priority(common) for common in common_elements]
        return sum(priorities)

    def part2(self, input: str) -> int:
        groups = split_into_chunks_of_size(input.splitlines(), 3)
        common_elements = [find_common_element(group) for group in groups]
        priorities = [calc_priority(common) for common in common_elements]
        return sum(priorities)
