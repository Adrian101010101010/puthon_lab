from ua.lviv.iot.algo.aerial_vehicle import AerialVehicle


class MilitaryDrone(AerialVehicle):
    """
    this class describes a MilitaryDrone
    """
    def __init__(self, max_speed, manufacturer, max_flying_distance,
                 max_delivery_weight, name="MilitaryDrone"):
        super().__init__(max_speed, manufacturer, max_flying_distance, max_delivery_weight)
        self.name = name

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
