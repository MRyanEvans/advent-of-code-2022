import re

from src.common import Solution, split_into_chunks_of_size


def load_init_stacks(init: str):
    stacks = {}
    for row in init.splitlines()[0:-1]:
        containers = [n[1] for n in split_into_chunks_of_size(row, 4)]
        for ci in range(1, len(containers) + 1):
            container = containers[ci - 1]
            if ci not in stacks:
                stacks[ci] = []
            if container != ' ':
                stacks[ci].insert(0, container)
    return stacks


def parse_input(input):
    init, instructions = input.split('\n\n')
    return load_init_stacks(init), [[int(n) for n in re.search(r"move (\d+) from (\d+) to (\d+)", i).groups()]
                                    for i in instructions.splitlines()]


def read_top_layer(stacks):
    return ''.join([stack[-1] for stack in stacks.values()])


class Day05(Solution):

    def part1(self, input: str) -> str:
        stacks, instructions = parse_input(input)
        for n, frm, to in instructions:
            stacks[to] += [stacks[frm].pop() for _ in range(n)]
        return read_top_layer(stacks)

    def part2(self, input: str) -> str:
        stacks, instructions = parse_input(input)
        for n, frm, to in instructions:
            stacks[to] += reversed([stacks[frm].pop() for _ in range(n)])
        return read_top_layer(stacks)
