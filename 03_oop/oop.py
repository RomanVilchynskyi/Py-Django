from abc import ABC, abstractmethod

class Passport:
    def __init__(self, name, surname, nationality):
        self.name = name
        self.surname = surname
        self.nationality = nationality

    def __str__(self):
        return f"Passport: {self.name} {self.surname}, Nationality: {self.nationality}"

class ForeignPassword(Passport):
    def __init__(self, name, surname, nationality, passportNum):
        super().__init__(name, surname, nationality)
        self.passportNum = passportNum
        self.visas = []
    def addVisa(self, visa):
        if visa not in self.visas:
            self.visas.append(visa)
        
    def removeVisa(self, visa):
        if visa in self.visas:
            self.visas.remove(visa)

    def __str__(self) -> str:
        return f"{super().__str__()}, Foreign Passport No: {self.passportNum}, Visas: {self.visas if self.visas else 0}"

passw = ForeignPassword("Vika", "Vikadaf", "ukraine", 21)

passw.addVisa("USA")
passw.addVisa("Germany")

passw.removeVisa("USA")
print(passw)


class TemperatureConverter:
    counter = 0

    @staticmethod
    def to_fahrenheit(celsius):
        TemperatureConverter.counter += 1
        return (celsius * 9/5) + 32

    @staticmethod
    def to_celsius(fahrenheit):
        TemperatureConverter.counter += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_count():
        return TemperatureConverter.counter


print(TemperatureConverter.to_fahrenheit(100))
print(TemperatureConverter.to_celsius(43))
print("Conversions:", TemperatureConverter.get_count())


class Ship(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fire(self):
        pass

    def __str__(self):
        return f"Ship name: {self.name}"
        
class Frigate(Ship):
    def fire(self):
        return f"{self.name} fires light weapons!"


class Destroyer(Ship):
    def fire(self):
        return f"{self.name} launches missiles!"


class Cruiser(Ship):
    def fire(self):
        return f"{self.name} fires heavy artillery!"
    
ships = [
    Frigate("Horizon"),
    Destroyer("Thunder"),
    Cruiser("Ocean King")
]

for ship in ships:
    print(ship) 
    print(ship.fire()) 
