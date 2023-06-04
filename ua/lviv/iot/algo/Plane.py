"""
class Plane
"""
# pylint: disable=import-error
from ua.lviv.iot.algo.aerial_vehicle import AerialVehicle
from ua.lviv.iot.algo.redundant_excessive_cargo_weight import RedundantExcessiveCargoWeight
from ua.lviv.iot.algo.redundant_excessive_cargo_weight import logged


class Plane(AerialVehicle):
    """
    this class describes a Plane
    """

    load_capacity = 1000
    mass_of_the_cargo = None

    # pylint: disable=too-many-arguments
    def __init__(self, new_speed, speed_now, max_speed, manufacturer,
                 max_flying_distance, max_delivery_weight, octane_number, name="Plane"):
        """
        :type name: this parameter shows name
        :param new_speed: this parameter shows new speed
        :param speed_now: this parameter shows speed now
        :param max_speed: this parameter shows max speed
        :param manufacturer: this parameter shows manufacturer
        :param max_flying_distance: this parameter shows max flying distance
        :param max_delivery_weight: this parameter shows max delivery weight
        """
        super().__init__(max_speed, manufacturer, max_flying_distance,
                         max_delivery_weight, octane_number)
        self.new_speed = new_speed
        self.speed_now = speed_now
        self.name = name
        self.octane_number = octane_number

    def __str__(self):
        return f"{self.name}, {self.new_speed}, {self.speed_now}"

    def fast(self, acceleration):
        """
              this method checks if the new speed is not greater than the
         maximum speed, if it is greater, then the new speed is
          the maximum speed
        :param acceleration: this parameter show by how much the speed increased
        :return: acceleration
        """
        # pylint: disable=attribute-defined-outside-init
        # pylint: disable=access-member-before-definition
        self.new_speed = self.speed_now + acceleration
        if self.new_speed > self.max_speed:
            self.new_speed = self.max_speed
            self.max_speed = 600

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
        return "flies like an f 777"

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
        try:
            raise RedundantExcessiveCargoWeight("Excessive cargo weight detected.")
        except RedundantExcessiveCargoWeight as ex:
            print(ex)

    @logged(RedundantExcessiveCargoWeight, mode="file")
    def cargo(self):
        """
        this method looks for errors in class
        :return:
        """
        self.loading_of_transport(1500)
