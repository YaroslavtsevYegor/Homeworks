class LowFuelError(Exception):

    def __str__(self):
        return 'Низкий уровень топлива'


class NotEnoughFuel(Exception):

    def __str__(self):
        return 'Недостаточно топлива'


class CargoOverload(Exception):

    def __str__(self):
        return 'Перегруз'
