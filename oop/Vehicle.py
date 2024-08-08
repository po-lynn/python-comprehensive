from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print(f"{self.make} {self.model} ({self.year}) starting...")

    def stop(self):
        print(f"{self.make} {self.model} ({self.year}) stopping...")

class Motorcycle(Vehicle):
    def start(self):
        print(f"{self.make} {self.model} ({self.year}) starting...")

    def stop(self):
        print(f"{self.make} {self.model} ({self.year}) stopping...")

class ElectricVehicle(ABC):
    @abstractmethod
    def charge(self):
        pass

class ElectricCar(Car, ElectricVehicle):
    def charge(self):
        print(f"{self.make} {self.model} ({self.year}) charging...")

class ElectricMotorcycle(Motorcycle, ElectricVehicle):
    def charge(self):
        print(f"{self.make} {self.model} ({self.year}) charging...")

class VehicleShelter:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def list_vehicles(self):
        for vehicle in self.vehicles:
            print(f"{vehicle.make} {vehicle.model} ({vehicle.year})")

    def start_all_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.start()

    def stop_all_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.stop()

    def charge_all_electric_vehicles(self):
        for vehicle in self.vehicles:
            if isinstance(vehicle, ElectricVehicle):
                vehicle.charge()


shelter = VehicleShelter()
shelter.add_vehicle(Car("Toyota", "Camry", 2021))
shelter.add_vehicle(Motorcycle("Honda", "CBR600RR", 2022))
shelter.add_vehicle(ElectricCar("Tesla", "Model S", 2023))
shelter.add_vehicle(ElectricMotorcycle("Zero", "SR/F", 2024))
shelter.list_vehicles()
# Output: "Toyota Camry (2021)", "Honda CBR600RR (2022)", "Tesla Model S (2023)", "Zero SR/F (2024)"
shelter.start_all_vehicles()
# Output: "Toyota Camry (2021) starting...", "Honda CBR600RR (2022) starting...", "Tesla Model S (2023) starting...", "Zero SR/F (2024) starting..."
shelter.stop_all_vehicles()
# Output: "Toyota
