from src.common import Solution


def move_towards_knot(tail, head):
    dx = abs(tail[0] - head[0])
    dy = abs(tail[1] - head[1])
    if dx > 1 or dy > 1:
        if tail[0] != head[0]:
            head[0] += 1 if tail[0] > head[0] else -1
        if tail[1] != head[1]:
            head[1] += 1 if tail[1] > head[1] else -1
    return head


def move_in_direction(direction, knot):
    if direction == 'R':
        return [knot[0] + 1, knot[1]]
    if direction == 'L':
        return [knot[0] - 1, knot[1]]
    if direction == 'U':
        return [knot[0], knot[1] + 1]
    if direction == 'D':
        return [knot[0], knot[1] - 1]
    return None


def move_knots_in_dir(knots, direction):
    knots[0] = move_in_direction(direction, knots[0])
    for ki in range(1, len(knots)):
        knots[ki] = move_towards_knot(knots[ki - 1], knots[ki])


def record_tail_positions(knots, instructions):
    tails = []
    for direction, times in instructions:
        for i in range(times):
            move_knots_in_dir(knots, direction)
            tails.append(tuple(knots[-1]))
    return len(set(tails))


class Day09(Solution):

    def part1(self, input: str) -> int:
        knots = [[0, 0], [0, 0]]
        instructions = [[line.split()[0], int(line.split()[1])] for line in input.splitlines()]
        return record_tail_positions(knots, instructions)

    def part2(self, input: str) -> int:
        knots = [[0, 0] for _ in range(10)]
        instructions = [[line.split()[0], int(line.split()[1])] for line in input.splitlines()]
        return record_tail_positions(knots, instructions)
