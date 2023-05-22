from abc import ABC, abstractmethod


class AerialVehicle(ABC):
    """
    this class is the parent abstract class for the Helicopter, Drone, MilitaryDrone,
     Plain classes, and he has  fields max_speed, manufacturer, 2 method  get_max_flying_distance,
     get_max_delivery_weight
    """

    def __init__(self, max_speed, manufacturer, max_flying_distance, max_delivery_weight):
        self.max_speed = max_speed
        self.manufacturer = manufacturer
        self.max_flying_distance = max_flying_distance
        self.max_delivery_weight = max_delivery_weight

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
