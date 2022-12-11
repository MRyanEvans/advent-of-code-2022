import re

from src.common import Solution, multiply_elements


class Scenario:
    def __init__(self, monkeys, rounds, divide_by_three):
        self.monkeys = monkeys
        self.rounds = rounds
        self.divide_by_three = divide_by_three
        self.mod = multiply_elements([m.divisible_by for m in self.monkeys])

    def run(self):
        for _ in range(self.rounds):
            for monkey in self.monkeys:
                while len(monkey.items) > 0:
                    item = monkey.items.pop()

                    arg = item if monkey.operator_and_oparg[1] == 'old' else int(monkey.operator_and_oparg[1])
                    if monkey.operator_and_oparg[0] == '+':
                        worry_level = item + arg
                    else:
                        worry_level = item * arg
                    worry_level = int(worry_level / 3) if self.divide_by_three else worry_level % self.mod

                    is_divisible = (worry_level % monkey.divisible_by == 0)
                    pass_to = monkey.throw_to_if_true if is_divisible else monkey.throw_to_if_false
                    self.monkeys[pass_to].items.insert(0, worry_level)

                    monkey.items_inspected += 1
        return self.monkeys


class Monkey:
    def __init__(self, number, items, operator_and_oparg, divisible_by, throw_to_if_true, throw_to_if_false):
        self.number = number
        self.items = items
        self.operator_and_oparg = operator_and_oparg
        self.divisible_by = divisible_by
        self.throw_to_if_true = throw_to_if_true
        self.throw_to_if_false = throw_to_if_false
        self.items_inspected = 0

    def num_items_inspected(self):
        return self.items_inspected

    def inspect_items(self, monkeys, divide_worry_level=True, modulo=None):
        while len(self.items) > 0:
            item = self.items.pop()
            arg = item if self.operator_and_oparg[1] == 'old' else int(self.operator_and_oparg[1])
            if self.operator_and_oparg[0] == '+':
                new_worry_level = item + arg
            else:
                new_worry_level = item * arg
            new_worry_level = int(new_worry_level / 3) if divide_worry_level else new_worry_level % modulo
            is_divisible = (new_worry_level % self.divisible_by == 0)
            pass_to = self.throw_to_if_true if is_divisible else self.throw_to_if_false
            monkeys[pass_to].items.insert(0, new_worry_level)
            self.items_inspected += 1


def parse_monkeys(input):
    monkeys = []
    for block in input.split('\n\n'):
        statements = block.splitlines()
        monkeys.append(
            Monkey(
                int(re.match(r".*(\d+):", statements[0]).groups()[0]),
                list(reversed([int(n) for n in statements[1].split(':')[1].split(', ')])),
                re.match(r"\s+Operation: new = old ([*+]) (\w+)$", statements[2]).groups(),
                int(re.match(r"\s+Test: divisible by (\d+)$", statements[3]).groups()[0]),
                int(re.match(r"\s+If true: throw to monkey (\d+)$", statements[4]).groups()[0]),
                int(re.match(r"\s+If false: throw to monkey (\d+)$", statements[5]).groups()[0])
            )
        )
    return monkeys


class Day11(Solution):

    def part1(self, input: str) -> int:
        monkeys = Scenario(parse_monkeys(input), 20, True).run()
        return multiply_elements(list(reversed(sorted([m.num_items_inspected() for m in monkeys])))[0:2])

    def part2(self, input: str) -> int:
        monkeys = Scenario(parse_monkeys(input), 10000, False).run()
        return multiply_elements(list(reversed(sorted([m.num_items_inspected() for m in monkeys])))[0:2])
