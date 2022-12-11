from src.common import Solution, multiply_elements


def look_around(y, x, trees):
    up = list(reversed([r[x] for r in trees][:y]))
    down = [r[x] for r in trees][y + 1:]
    left = list(reversed(trees[y][0:x]))
    right = trees[y][x + 1:]
    return [up, down, left, right]


def is_on_edge(lines_of_sight):
    return [] in lines_of_sight


class Day08(Solution):

    def part1(self, input: str) -> int:
        trees = [[int(n) for n in list(l)] for l in input.splitlines()]
        visible = []
        for y in range(len(trees[0])):
            for x in range(len(trees)):
                lines_of_sight = look_around(y, x, trees)
                if is_on_edge(lines_of_sight):
                    visible.append([y, x])
                    continue
                for los in lines_of_sight:
                    if trees[y][x] > max(los):
                        visible.append([y, x])
                        break

        return len(visible)

    def part2(self, input: str) -> int:
        trees = [[int(n) for n in list(l)] for l in input.splitlines()]
        scenic_scores = []
        for y in range(len(trees)):
            for x in range(len(trees[0])):
                lines_of_sight = look_around(y, x, trees)
                if is_on_edge(lines_of_sight):
                    continue

                viewing_distances = []
                for los in lines_of_sight:
                    viewing_distance = 0
                    for tree_in_los in los:
                        viewing_distance += 1
                        if tree_in_los >= trees[y][x]:
                            break
                    viewing_distances.append(viewing_distance)
                    pass
                scenic_scores.append(multiply_elements(viewing_distances) if viewing_distances != [] else 0)

        return max(scenic_scores)
