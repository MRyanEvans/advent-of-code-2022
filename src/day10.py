from src.common import Solution


def record_instruction_ticks(instructions):
    x = 1
    tick = 0
    x_at_tick = {}
    for instruction in instructions:
        tick += 1
        x_at_tick[tick] = x
        if instruction.startswith("addx"):
            tick += 1
            x_at_tick[tick] = x
            x += int(instruction.split()[1])
    return x_at_tick


class Day10(Solution):

    def part1(self, input: str) -> int:
        x_at_tick = record_instruction_ticks(input.splitlines())
        ticks = [20, 60, 100, 140, 180, 220]
        return sum([x_at_tick[t] * t for t in ticks])

    def part2(self, input: str) -> str:
        x_at_tick = record_instruction_ticks(input.splitlines())
        readout = ''
        for y in range(6):
            for x in range(40):
                tick = (y * 40) + x
                sprite_value = x_at_tick[tick + 1]
                on_sprite = abs(sprite_value - x) < 2
                readout += '\u2589' if on_sprite else ' '
            readout += '\n'
        return readout[:-1]
