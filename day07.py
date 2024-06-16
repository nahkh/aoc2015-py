from __future__ import annotations
import dataclasses
from enum import Enum
from typing import Tuple, Dict, List

MAX_16 = 65535


class Operator(Enum):
    INPUT = 1
    AND = 2
    OR = 3
    LSHIFT = 4
    RSHIFT = 5
    NOT = 6
    REMAP = 7


@dataclasses.dataclass(frozen=True)
class Operation:
    operator: Operator
    operands: Tuple[str, ...]
    output: str

    @classmethod
    def parse(cls, line: str):
        line = line.strip()
        parts = line.split(' -> ')
        assert len(parts) == 2
        output = parts[1]
        operation_string = parts[0]
        if ' RSHIFT ' in operation_string:
            operands = tuple(operation_string.split(' RSHIFT '))
            operator = Operator.RSHIFT
        elif ' LSHIFT ' in operation_string:
            operands = tuple(operation_string.split(' LSHIFT '))
            operator = Operator.LSHIFT
        elif ' OR ' in operation_string:
            operands = tuple(operation_string.split(' OR '))
            operator = Operator.OR
        elif ' AND ' in operation_string:
            operands = tuple(operation_string.split(' AND '))
            operator = Operator.AND
        elif operation_string.startswith('NOT '):
            operands = operation_string[4:],
            operator = Operator.NOT
        elif operation_string.isnumeric():
            operands = operation_string,
            operator = Operator.INPUT
        elif operation_string.isalpha():
            operands = operation_string,
            operator = Operator.REMAP
        else:
            assert False, f'Could not parse line "{line}"'
        return Operation(operator, operands, output)

    def evaluate_operand(self, context: ExecutionGraph, index: int) -> int:
        assert len(self.operands) > index
        operand = self.operands[index]
        if operand.isnumeric():
            return int(operand)
        else:
            return context.evalute(operand)

    def evaluate(self, context: ExecutionGraph) -> int:
        if self.operator == Operator.INPUT:
            return int(self.operands[0])
        elif self.operator == Operator.AND:
            left = self.evaluate_operand(context, 0)
            right = self.evaluate_operand(context, 1)
            return left & right
        elif self.operator == Operator.OR:
            left = self.evaluate_operand(context, 0)
            right = self.evaluate_operand(context, 1)
            return left | right
        elif self.operator == Operator.NOT:
            source = self.evaluate_operand(context, 0)
            return source ^ MAX_16
        elif self.operator == Operator.REMAP:
            return self.evaluate_operand(context, 0)
        elif self.operator == Operator.LSHIFT:
            source = context.evalute(self.operands[0])
            n = int(self.operands[1])
            return source << n
        elif self.operator == Operator.RSHIFT:
            source = context.evalute(self.operands[0])
            n = int(self.operands[1])
            return source >> n


@dataclasses.dataclass
class ExecutionGraph:
    source_operations: Dict[str, Operation]
    computed_values: Dict[str, int]

    @classmethod
    def create(cls, operations: List[Operation]):
        source_operations = {op.output: op for op in operations}
        return ExecutionGraph(source_operations, {})

    def evalute(self, wire: str) -> int:
        assert wire in self.source_operations, f'{wire=} not defined'
        if wire not in self.computed_values:
            self.computed_values[wire] = self.source_operations[wire].evaluate(self)
        return self.computed_values[wire]

    def evaluate_all(self):
        for wire in self.source_operations.keys():
            self.evalute(wire)

    def get_calculated_values(self) -> List[Tuple[str, int]]:
        keys = list(self.computed_values.keys())
        keys.sort()
        output = []
        for key in keys:
            output.append((key, self.computed_values[key]))
        return output


def part1(lines: List[str]):
    operations = [Operation.parse(line) for line in lines]
    execution_graph = ExecutionGraph.create(operations)
    wire = 'a'
    print(f'Day 7, part 1: The value on wire "{wire}" is {execution_graph.evalute(wire)}')


def part2(lines: List[str]):
    operations = [Operation.parse(line) for line in lines]
    execution_graph = ExecutionGraph.create(operations)
    wire = 'a'
    value_of_a = execution_graph.evalute(wire)
    execution_graph.computed_values = {'b': value_of_a}
    print(
        f'Day 7, part 2: The value on wire "{wire}" is {execution_graph.evalute(wire)} after overriding "b" with {value_of_a}')


def main():
    with open('input07.txt') as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)


if __name__ == '__main__':
    main()
