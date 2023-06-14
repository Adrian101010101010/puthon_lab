"""
class MilitaryDrone
"""
# pylint: disable=import-error
from ua.lviv.iot.algo.aerial_vehicle import AerialVehicle
from ua.lviv.iot.algo.redundant_excessive_cargo_weight import RedundantExcessiveCargoWeight
from ua.lviv.iot.algo.redundant_excessive_cargo_weight import logged


class MilitaryDrone(AerialVehicle):
    """
    this class describes a MilitaryDrone
    """

    load_capacity = 1000
    mass_of_the_cargo = None

    # pylint: disable=too-many-arguments
    def __init__(self, max_speed, manufacturer, max_flying_distance,
                 max_delivery_weight, octane_number, name="MilitaryDrone"):
        super().__init__(max_speed, manufacturer, max_flying_distance, max_delivery_weight,
                         octane_number)
        self.name = name
        self.octane_number = octane_number

    def __str__(self):
        return f"{self.name}"

    @staticmethod
    def ppo_see(percentage_of_invisibility):
        """
        this method checks if ppo_see it can be seen
        :param percentage_of_invisibility:
        :return:
        """
        if percentage_of_invisibility == 100:
            print("the drone won")
        if percentage_of_invisibility == 50:
            print("drone is a draw")
        if percentage_of_invisibility == 0:
            print("drone loss")

    def get_max_flying_distance(self):
        """
        this method takes the max flying distance value
         from the constructor
        :return: max_flying_distance
        """
        return self.max_flying_distance

    def get_max_delivery_weight(self):
        """
        this method takes the max delivery weight value
         from the constructor
        :return: max delivery weight
        """
        return self.max_delivery_weight

    def fly(self):
        """

        :return: string
        """
        return "flies like an f 19"

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

