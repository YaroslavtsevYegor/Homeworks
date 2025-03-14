
from Homeworks.hw_2.base import Vehicle
from Homeworks.hw_2.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, started, cargo, max_cargo):
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self._cargo = cargo
        self._max_cargo = max_cargo

    @property
    def cargo(self):
        return self._cargo

    @property
    def max_cargo(self):
        return self._max_cargo

    def load_cargo(self, add_cargo):
        if add_cargo + self._cargo > self._max_cargo:
            raise CargoOverload
        else:
            self._cargo += add_cargo

    def remove_all_cargo(self):
        current_cargo = self._cargo
        self._cargo = 0
        return current_cargo
