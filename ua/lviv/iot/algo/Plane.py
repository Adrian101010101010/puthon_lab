from ua.lviv.iot.algo.AerialVehicle import AerialVehicle


class Plane(AerialVehicle):
    """
    this class describes a Plane
    """

    def __init__(self, new_speed, speed_now, max_speed, manufacturer,
                 max_flying_distance, max_delivery_weight, name="Plane"):
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
                         max_delivery_weight)
        self.new_speed = new_speed
        self.speed_now = speed_now
        self.name = name

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
