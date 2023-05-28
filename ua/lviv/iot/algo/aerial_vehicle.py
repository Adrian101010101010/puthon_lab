"""
import Abstract Base Class
"""
from abc import ABC, abstractmethod


class AerialVehicle(ABC):
    """
    this class is the parent abstract class for the Helicopter,
     Drone, MilitaryDrone,
     Plain classes, and he has  fields max_speed, manufacturer,
      2 method  get_max_flying_distance,
     get_max_delivery_weight
    """

    # pylint: disable=too-many-arguments
    def __init__(self, max_speed, manufacturer, max_flying_distance,
                 max_delivery_weight, octane_number):
        """

        :param max_speed: create a parameter max_speed
        :param manufacturer: create a parameter manufacturer
        :param max_flying_distance: create a parameter max_flying_distance
        :param max_delivery_weight: create a parameter max_delivery_weight
        :param octane_number: create a parameter octane_number
        """
        self.max_speed = max_speed
        self.manufacturer = manufacturer
        self.max_flying_distance = max_flying_distance
        self.max_delivery_weight = max_delivery_weight
        self.octane_number = octane_number

    def __iter__(self):
        """
        :return: an iterator for the octane_number attribute
        """
        return iter(self.octane_number)

    @abstractmethod
    def fly(self):
        """
        make a replacement in the descendants string
        :return: string
        """

    @abstractmethod
    def get_max_flying_distance(self):
        """
        this method accepts a value max_flying_distance
        :return: max_flying_distance
        """
        return self.max_flying_distance

    @abstractmethod
    def get_max_delivery_weight(self):
        """
        this method accepts a value max_delivery_weight
        :return:
        """
        return self.max_delivery_weight

    def get_info(self):
        """

        :return:
        """
        return f"Aerial Vehicle\nMax Speed: {self.max_speed}\nManufacturer: {self.manufacturer}\n"
