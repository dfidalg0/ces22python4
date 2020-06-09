from q1 import Car, Truck, Bus
from q1 import Eletric, Hybrid, Combustion

class VehicleFactory:
    @staticmethod
    def create(vehicle_type, engine_type):
        Engine = None
        Vehicle = None

        if vehicle_type == 'car':
            Vehicle = Car
        elif vehicle_type == 'truck':
            Vehicle = Truck
        elif vehicle_type == 'bus':
            Vehicle = Bus

        if engine_type == 'eletric':
            Engine = Eletric
        if engine_type == 'hybrid':
            Engine = Hybrid
        if engine_type == 'combustion':
            Engine = Combustion

        if Engine and Vehicle:
            return Vehicle(Engine())
        else:
            return None

# Demonstration
def main():
    for vehicle_type in ['car','truck','bus']:
        for engine_type in ['eletric', 'hybrid', 'combustion']:
            vehicle = VehicleFactory.create(vehicle_type,engine_type)
            vehicle.run()

if __name__ == '__main__':
    main()
