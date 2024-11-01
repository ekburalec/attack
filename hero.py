from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name: str, health=100, attack_power=20):
        self._name = name
        self._health = health
        self._attack_power = attack_power

    @abstractmethod
    def attack(self, other):
        pass

    def is_alive(self):
        return self._health > 0

    def get_health(self):
        return self._health

    def get_name(self):
        return self._name


class Player(Hero):
    def attack(self, other):
        other._health -= self._attack_power
        print(f"{self._name} атакует {other.get_name()} и наносит {self._attack_power} урона!")


class Computer(Hero):
    def attack(self, other):
        other._health -= self._attack_power
        print(f"{self._name} атакует {other.get_name()} и наносит {self._attack_power} урона!")