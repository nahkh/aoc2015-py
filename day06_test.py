import unittest
from day06 import *


class TestDay6(unittest.TestCase):

    def test_parse_instruction(self):
        self.assertEqual(Instruction.parse("turn on 0,0 through 999,999"),
                         Instruction(InstructionType.TURN_ON, PositionRange(0, 999, 0, 999)))
        self.assertEqual(Instruction.parse("toggle 0,0 through 999,0"),
                         Instruction(InstructionType.TOGGLE, PositionRange(0, 999, 0, 0)))
        self.assertEqual(Instruction.parse("turn off 499,499 through 500,500"),
                         Instruction(InstructionType.TURN_OFF, PositionRange(499, 500, 499, 500)))

    def test_light_state_apply_instruction(self):
        self.assertEqual(LightState.ON.apply(InstructionType.TURN_ON), LightState.ON)
        self.assertEqual(LightState.ON.apply(InstructionType.TURN_OFF), LightState.OFF)
        self.assertEqual(LightState.ON.apply(InstructionType.TOGGLE), LightState.OFF)
        self.assertEqual(LightState.OFF.apply(InstructionType.TURN_ON), LightState.ON)
        self.assertEqual(LightState.OFF.apply(InstructionType.TURN_OFF), LightState.OFF)
        self.assertEqual(LightState.OFF.apply(InstructionType.TOGGLE), LightState.ON)

    def test_position_range_values(self):
        self.assertEqual(set(PositionRange(499, 500, 499, 500).positions()), {Position(499, 499), Position(499, 500), Position(500, 499), Position(500, 500)})

    def test_light_field_apply_instruction(self):
        field = LightField.create(1000, 1000)
        self.assertEqual(field.count_lights(), 0)
        field.apply(Instruction(InstructionType.TURN_ON, PositionRange(0, 999, 0, 999)))
        self.assertEqual(field.count_lights(), 1000000)
        field.apply(Instruction(InstructionType.TOGGLE, PositionRange(0, 999, 0, 0)))
        self.assertEqual(field.count_lights(), 999000)
        field.apply(Instruction(InstructionType.TURN_OFF, PositionRange(499, 500, 499, 500)))
        self.assertEqual(field.count_lights(), 998996)

if __name__ == '__main__':
    unittest.main()
