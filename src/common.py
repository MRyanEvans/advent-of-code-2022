from abc import ABC, abstractmethod


def split_into_chunks_of_size(thing, chunk_size):
    return [thing[i:i + chunk_size] for i in range(0, len(thing), chunk_size)]


def halve_list(lst):
    return lst[:len(lst) // 2], lst[len(lst) // 2:]


def find_common_element(lists):
    common = None
    for current in lists:
        if common is None:
            common = current
        common = set(common) & set(current)
    return list(common)[0]


class Solution(ABC):

    @abstractmethod
    def part1(self, input):
        pass

    @abstractmethod
    def part2(self, input):
        pass
