from __future__ import annotations
import dataclasses
from typing import List, Dict, Set, Tuple, Generator
from itertools import permutations


@dataclasses.dataclass
class Graph:
    nodes: List[str]
    edges: Dict[Tuple[str, str], int]

    @classmethod
    def create(cls, lines: List[str]) -> Graph:
        nodes = set()
        edges = {}
        for line in lines:
            line = line.strip()
            if not line:
                continue
            split1 = line.split(' = ')
            assert len(split1) == 2, f'Could not split line {line}'
            distance = int(split1[1])
            split2 = split1[0].split(' to ')
            a = split2[0]
            b = split2[1]
            nodes.add(a)
            nodes.add(b)
            edges[(a, b)] = distance
            edges[(b, a)] = distance
        return Graph(list(nodes), edges)

    def generate_all_paths(self) -> Generator[Tuple[List[str], int]]:
        for ordering in permutations(self.nodes):
            distance = 0
            for i in range(1, len(ordering)):
                distance += self.edges[(ordering[i - 1], ordering[i])]
            yield ordering, distance

    def find_shortest_path(self) -> int:
        minimum = None
        for path, length in self.generate_all_paths():
            if minimum is None or minimum > length:
                minimum = length
        return minimum


def part1(lines: List[str]):
    graph = Graph.create(lines)
    print(f'Day 9, part 1: The shortest route is {graph.find_shortest_path()}')


def main():
    with open('input09.txt') as f:
        lines = f.readlines()
        part1(lines)


if __name__ == '__main__':
    main()
