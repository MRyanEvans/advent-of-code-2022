import networkx
import numpy

from src.common import Solution


def build_grid(input):
    grid = numpy.array([[*x] for x in input.splitlines()])

    start = tuple(*numpy.argwhere(grid == 'S'))
    target = tuple(*numpy.argwhere(grid == 'E'))

    grid[start] = 'a'
    grid[target] = 'z'
    return grid, start, target


def find_paths_to_target(grid, target):
    neighbours_of_each_point = networkx.grid_2d_graph(*grid.shape)

    graph = networkx.DiGraph()
    for square in numpy.ndindex(grid.shape):
        for neighbour in neighbours_of_each_point.neighbors(square):
            if ord(grid[neighbour]) <= ord(grid[square]) + 1:
                graph.add_edge(square, neighbour)

    return networkx.shortest_path_length(graph, target=target)


class Day12(Solution):

    def part1(self, input: str) -> int:
        grid, start, target = build_grid(input)
        paths = find_paths_to_target(grid, target)
        return paths[start]

    def part2(self, input: str) -> int:
        grid, start, target = build_grid(input)
        paths = find_paths_to_target(grid, target)
        paths_from_lowest_elevation = [paths[p] for p in paths if grid[p] == 'a']
        return min(paths_from_lowest_elevation)
