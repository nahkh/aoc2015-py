from __future__ import annotations
from functools import  cache
import dataclasses
from typing import List, Generator, Tuple


@dataclasses.dataclass(frozen=True)
class Character:
    hp: int
    attack: int
    defense: int

    @classmethod
    def parse_boss(cls, lines: List[str]) -> Character:
        hp = int(lines[0][12:].strip())
        attack = int(lines[1][8:].strip())
        defense = int(lines[2][7:].strip())
        return Character(hp, attack, defense)

    def damage_received(self, attacker: Character) -> int:
        return max(1, attacker.attack - self.defense)


@cache
def does_player_win(player: Character, boss: Character) -> bool:
    player_turn = True
    current_player_hp = player.hp
    current_boss_hp = boss.hp
    while True:
        if player_turn:
            damage = boss.damage_received(player)
            current_boss_hp -= damage
            if current_boss_hp <= 0:
                return True
        else:
            damage = player.damage_received(boss)
            current_player_hp -= damage
            if current_player_hp <= 0:
                return False
        player_turn = not player_turn


@dataclasses.dataclass(frozen=True)
class Item:
    name: str
    cost: int
    attack: int
    defense: int


WEAPONS = (
    Item('Dagger', 8, 4, 0),
    Item('Shortsword', 10, 5, 0),
    Item('Warhammer', 25, 6, 0),
    Item('Longsword', 40, 7, 0),
    Item('Greataxe', 74, 8, 0),
)

ARMORS = (
    Item('Leather', 13, 0, 1),
    Item('Chainmail', 31, 0, 2),
    Item('Splintmail', 53, 0, 3),
    Item('Bandedmail', 75, 0, 4),
    Item('Platemail', 102, 0, 5),
)

RINGS = (
    Item('Damage +1', 25, 1, 0),
    Item('Damage +2', 50, 2, 0),
    Item('Damage +3', 100, 3, 0),
    Item('Defense +1', 20, 0, 1),
    Item('Defense +2', 40, 0, 2),
    Item('Defense +3', 80, 0, 3),
)

NO_ITEM = Item('None', 0, 0, 0)


def all_armor_options() -> Generator[Item]:
    yield NO_ITEM
    for armor in ARMORS:
        yield armor


def all_ring_options() -> Generator[Tuple[Item, Item]]:
    yield NO_ITEM, NO_ITEM
    for ring in RINGS:
        yield ring, NO_ITEM
    for ring1 in RINGS:
        for ring2 in RINGS:
            if ring1 == ring2:
                continue
            yield ring1, ring2


@dataclasses.dataclass(frozen=True)
class EquipmentLoadout:
    weapon: Item
    armor: Item
    ring1: Item
    ring2: Item

    def items(self):
        yield self.weapon
        yield self.armor
        yield self.ring1
        yield self.ring2

    def cost(self) -> int:
        return sum(map(lambda x: x.cost, self.items()))

    def as_combatant(self) -> Character:
        attack = sum(map(lambda x: x.attack, self.items()))
        defense = sum(map(lambda x: x.defense, self.items()))
        return Character(100, attack, defense)

    @classmethod
    def all_options(cls) -> Generator[EquipmentLoadout]:
        for weapon in WEAPONS:
            for armor in all_armor_options():
                for ring1, ring2 in all_ring_options():
                    yield EquipmentLoadout(weapon, armor, ring1, ring2)


def find_cheapest_equipment_that_beats(boss: Character) -> EquipmentLoadout:
    best_loadout = None
    for loadout in EquipmentLoadout.all_options():
        if best_loadout and best_loadout.cost() < loadout.cost():
            continue
        if does_player_win(loadout.as_combatant(), boss) and (not best_loadout or best_loadout.cost() > loadout.cost()):
            best_loadout = loadout
    return best_loadout


def part1(lines: List[str]):
    boss = Character.parse_boss(lines)
    equipment = find_cheapest_equipment_that_beats(boss)
    print(f'Day 21, part 1: The cheapest equipment that beats the boss is {equipment.cost()}')
    print(f'Items: {", ".join(map(lambda x: x.name, equipment.items()))}')


def main():
    with open('input21.txt') as f:
        lines = f.readlines()
        part1(lines)


if __name__ == '__main__':
    main()