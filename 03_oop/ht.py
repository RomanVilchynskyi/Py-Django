from abc import ABC, abstractmethod

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



class Airplane:
    def __init__(self, model, max_passengers, current_passengers=0):
        self.model = model
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        return self.model == other.model

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers


    def __add__(self, amount):
        return Airplane(self.model, self.max_passengers, self.current_passengers + amount)

    def __sub__(self, amount):
        return Airplane(self.model, self.max_passengers, self.current_passengers - amount)

    # +=  -=
    def __iadd__(self, amount):
        self.current_passengers += amount
        return self

    def __isub__(self, amount):
        self.current_passengers -= amount
        return self

    def __int__(self):
        return self.current_passengers

    def __str__(self):
        return self.model


a1 = Airplane("Boeing 737", 200, 120)
a2 = Airplane("Airbus A320", 180, 90)
a3 = Airplane("Boeing 737", 200, 50)

print(a1 == a3)          

a1 += 50
print(int(a1))

a2 = a2 + 20
print(int(a2)) 

print(a1 > a2)         
print(str(a1))        
