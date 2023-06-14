"""
import  AerialVehicle
"""
# pylint: disable=import-error
import logging
from ua.lviv.iot.algo.aerial_vehicle import AerialVehicle
from ua.lviv.iot.algo.redundant_excessive_cargo_weight import RedundantExcessiveCargoWeight
from ua.lviv.iot.algo.redundant_excessive_cargo_weight import logged

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])


# pylint: disable=too-many-instance-attributes
class Helicopter(AerialVehicle):
    """
    this class succinctly describes the helicopter speed, the height of the remaining fuel
    """
    max_altitude = 100
    id_is = 345
    __instance = None
    load_capacity = 1000
    mass_of_the_cargo = None

    # pylint: disable=too-many-arguments
    def __init__(self, max_speed, manufacturer, max_flying_distance, octane_number,
                 max_delivery_weight, current_altitude=1000, name="Helicopter",
                 new_altitude=1000, fuel_updated=50, id_is=100, max_altitude=1000,
                 fuel_capacity=30, current_fuel=10):
        """
        In this method we add all the common fields of the application
        :param current_altitude: this field shows at what height the plane is at the moment
        :param new_altitude: this field shows the new speed of the helicopter
        :param fuel_updated: this field shows how much the fuel volume has increased
        :param id_is: this field shows id helicopter
        :param max_altitude: this field max altitude helicopter
        :param fuel_capacity: this field shows max fuel capacity
        :param current_fuel: this field fuel volume new
        """

        super().__init__(max_speed, manufacturer, max_flying_distance, max_delivery_weight,
                         octane_number)
        self.id_is = id_is
        self.name = name
        self.fuel_updated = fuel_updated
        self.current_altitude = current_altitude
        self.new_altitude = new_altitude
        self.max_altitude = max_altitude
        self.fuel_capacity = fuel_capacity
        self.current_fuel = current_fuel
        self.octane_number = octane_number

    def __str__(self):
        return f"{self.current_altitude}, {self.new_altitude}," \
               f" {self.fuel_updated}, {self.id_is}, " \
               f"{self.max_altitude}, {self.fuel_capacity}, " \
               f"{self.current_fuel}, {self.name},"

    @staticmethod
    def get_instance():
        """
        crate new odict
        :return: __instance
        """
        if not Helicopter.__instance:
            Helicopter.__instance = Helicopter(1000, 1000, 50, 150, 1500,
                                               100, "we is helicopter", 50, 20)
        return Helicopter.__instance

    # pylint: disable=invalid-name
    @staticmethod
    def plays(a, b):
        """
        plays a + b
        """
        var = a + b
        return var

    def ascend(self, altitude):
        """
        this method checks if the new height is not higher than
         the maximum height, if not then creates a new current height
        :param altitude: by how much should the height change
        :return: altitude
        """
        self.new_altitude = self.current_altitude + altitude

        if self.new_altitude > self.max_altitude:
            corrent_altitude = self.max_altitude
        else:
            corrent_altitude = self.new_altitude
        print("Ascended to altitude", corrent_altitude)

    def take_off(self):
        """
        take off helicopter
        :return: current_altitude
        """
        self.current_altitude = 100
        print("Corrent altitude is", self.current_altitude)

    def descend(self, altitude):
        """
        this method checks if the new altitude is lower than sea level,
         if not, it decrements the current altitude
        :param altitude: by how much should the height change
        :return: altitude
        """
        self.new_altitude = self.current_altitude - altitude
        if self.new_altitude < 0:
            self.current_altitude = 0
        else:
            self.current_altitude = self.new_altitude
        print("Descended to altitude", self.current_altitude)

    def refuel(self, fuel):
        """
        this method checks whether the refueling of the helicopter
         does not continue when the tank is full, if not,
          then we simply update the current fuel supply
        :param fuel: new fuels
        :return: fuel
        """
        self.fuel_updated = self.current_fuel + fuel
        if self.fuel_updated > self.fuel_capacity:
            print("The tank is full")
        else:
            self.current_fuel = self.fuel_updated
        print("fuel updated = ", self.current_fuel)

    def get_max_delivery_weight(self):
        """
        this method takes the max delivery weight value
         from the constructor
        :return: max delivery weight
        """
        return self.max_delivery_weight

    def get_max_flying_distance(self):
        """
        this method takes the max flying distance value
         from the constructor
        :return: max_flying_distance
        """
        return self.max_flying_distance

    def fly(self):
        """
        :return: string
        """
        return "flies like an I"

    @logged(RedundantExcessiveCargoWeight, mode="file")
    def loading_of_transport(self, mass_of_the_cargo):
        """
        this method tells how many planes are loaded or overloaded
        :param mass_of_the_cargo: this value shows the mass of the cargo
        :return: mass_of_the_cargo
        """
        self.mass_of_the_cargo = mass_of_the_cargo
        if mass_of_the_cargo < self.load_capacity:
            self.mass_of_the_cargo = mass_of_the_cargo
        else:
            self.mass_of_the_cargo = self.load_capacity

            raise RedundantExcessiveCargoWeight("Excessive cargo weight detected.")


if __name__ == '__main__':

    h = Helicopter(1000, 1000, 50, 150, 1500, 100, "we is helicopter", 346, 50, 20)
    h.loading_of_transport(521444)
    print(Helicopter.plays(5, 7))

    hel_list = [
        Helicopter(1000, 1000, 50, 150, 1500, 100, "we is helicopter", 346, 50, 20),
        Helicopter.get_instance(),
        Helicopter.get_instance(),
    ]

    for helicopter in hel_list:
        print(helicopter)

    numbers = [-1 * x for x in range(21) if x % 2 != 0]
    print(numbers)
