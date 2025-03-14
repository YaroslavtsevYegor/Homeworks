from abc import ABC

from Homeworks.hw_2.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self._weight = weight
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption
        self._started = False

    @property
    def weight(self):
        return self._weight

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self,fuel_level):
        if fuel_level < 0:
            raise LowFuelError
        self._fuel = fuel_level

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self,fuel_level):
        if fuel_level > self._fuel :
            raise NotEnoughFuel
        self._fuel_consumption = fuel_level

    @property
    def started(self):
        return self._started

    def start(self):
        if not self._started:
            if self._fuel > 0:
                self._started = True
            else:
                raise LowFuelError
        else:
            raise ValueError

    def move(self, distance):
        if self._started:
            required_fuel = (distance / 100) * self._fuel_consumption
            if required_fuel <= self._fuel:
                self._fuel -= required_fuel
            else:
                raise NotEnoughFuel
        else:
            raise ValueError

