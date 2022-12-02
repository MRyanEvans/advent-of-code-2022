from enum import Enum

from src.common import Solution


class Choice(Enum):
    rock = 1
    paper = 2
    scissors = 3

    @classmethod
    def parse(cls, value):
        return {
            'A': Choice.rock,
            'B': Choice.paper,
            'C': Choice.scissors,
            'X': Choice.rock,
            'Y': Choice.paper,
            'Z': Choice.scissors
        }.get(value)

    def beats(self, other):
        return self.wins_against() == other

    def draws_with(self, other):
        return self == other

    def wins_against(self):
        return {
            Choice.rock: Choice.scissors,
            Choice.paper: Choice.rock,
            Choice.scissors: Choice.paper
        }.get(self)

    def loses_against(self):
        return {
            Choice.scissors: Choice.rock,
            Choice.rock: Choice.paper,
            Choice.paper: Choice.scissors
        }.get(self)


class Outcome(Enum):
    lose = 1
    draw = 2
    win = 3

    @classmethod
    def parse(cls, value):
        return {
            'X': Outcome.lose,
            'Y': Outcome.draw,
            'Z': Outcome.win
        }.get(value)


def calc_score(opponent: Choice, me: Choice):
    if opponent.draws_with(me):
        return 3 + me.value
    elif me.beats(opponent):
        return 6 + me.value
    else:
        return me.value


def calc_score_for_outcome(opponent: Choice, outcome: Outcome):
    return {
        Outcome.lose: opponent.wins_against().value,
        Outcome.draw: 3 + opponent.value,
        Outcome.win: 6 + opponent.loses_against().value,
    }.get(outcome)


class Day02(Solution):

    def part1(self, input: str) -> int:
        total = 0
        for game in input.splitlines():
            opponent, my = game.split(' ')
            total += calc_score(Choice.parse(opponent), Choice.parse(my))
        return total

    def part2(self, input: str) -> int:
        total = 0
        for game in input.splitlines():
            opponent, outcome = game.split(' ')
            total += calc_score_for_outcome(Choice.parse(opponent), Outcome.parse(outcome))
        return total
