from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def work(self):
        pass

class Eletric (Engine):
    def work(self):
        print('eletricity.')

class Hybrid(Engine):
    def work(self):
        print('hybrid engine.')

class Combustion(Engine):
    def work(self):
        print('combustion.')


class Vehicle(ABC):
    def __init__(self, engine : Engine):
        self._engine = engine

    @abstractmethod
    def run(self):
        pass

class Car(Vehicle):
    def __init__(self, engine : Engine):
        super().__init__(engine)

    def run(self):
        print('Car running on', end=' ')
        self._engine.work()

class Truck(Vehicle):
    def __init__(self, engine : Engine):
        super().__init__(engine)

    def run(self):
        print('Truck running on', end=' ')
        self._engine.work()

class Bus(Vehicle):
    def __init__(self, engine : Engine):
        super().__init__(engine)

    def run(self):
        print('Bus running on', end=' ')
        self._engine.work()

# Demonstration
def main():
    for vehicle_type in [Car,Truck,Bus]:
        for engine_type in [Eletric, Hybrid, Combustion]:
            vehicle = vehicle_type(engine_type())
            vehicle.run()

if __name__ == '__main__':
    main()
