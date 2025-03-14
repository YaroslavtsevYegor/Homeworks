
from Homeworks.hw_2.base import Vehicle
from Homeworks.hw_2.engine import Engine


class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, started, engine):
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self._engine = None

    @property
    def engine(self):
        return self._engine

    def set_engine(self, engine: Engine):
        self._engine = engine