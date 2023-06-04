"""
import AerialVehicle
"""
# pylint: disable=import-error
from ua.lviv.iot.algo.aerial_vehicle import AerialVehicle


# pylint: disable=too-many-instance-attributes
class Drone(AerialVehicle):
    """
    this class describes a Drone
    """

    # pylint: disable=too-many-arguments
    def __init__(self, battery_capacity, charge_consumption_per_minute_of_flight,
                 speed, max_speed, manufacturer,
                 max_flying_distance, max_delivery_weight, octane_number, name="Drone"):
        """

        :param battery_capacity: this parameter shows battery capacity
        :param charge_consumption_per_minute_of_flight: this parameter
         shows charge consumption per minute of flight
        :param speed: this parameter shows now speed
        :param max_speed: this parameter shows max speed
        :param manufacturer: this parameter shows manufacturer
        :param max_flying_distance: this parameter shows max flying distance
        :param max_delivery_weight: this parameter shows max delivery weight
        :param octane_number: this parameter shows octane number
        """
        super().__init__(max_speed, manufacturer, max_flying_distance, max_delivery_weight,
                         octane_number)
        self.new_speed = None
        self.name = name
        self.max_speed = max_speed
        self.manufacturer = manufacturer
        self.max_flying_distance = max_flying_distance
        self.max_delivery_weight = max_delivery_weight
        self.speed = speed
        self.octane_number = octane_number
        self.battery_capacity = battery_capacity
        self.charge_consumption_per_minute_of_flight = charge_consumption_per_minute_of_flight

    def __str__(self):
        return f"{self.name}"

    def fast(self, acceleration):
        """
        this method checks if the new speed is not greater than the
         maximum speed, if it is greater, then the new speed is
          the maximum speed
        :param acceleration: this parameter show by how much the speed increased
        :return: acceleration
        """
        self.new_speed = self.speed + acceleration
        if self.new_speed > self.max_speed:
            self.new_speed = self.max_speed
        if self.battery_capacity == 50:
            self.max_speed = self.max_speed / 2
        if self.battery_capacity == 0:
            self.max_speed = 0

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
        return "flies like an f 16"
