from ua.lviv.iot.algo.Drone import Drone
from ua.lviv.iot.algo.Helicopter import Helicopter
from ua.lviv.iot.algo.Plane import Plane
from ua.lviv.iot.algo.MilitaryDrone import MilitaryDrone


class AerialVehicleManager:
    """
    this class contains a list of classes and, thanks to the sheet, sucks the required objects
    """
    list = []

    @staticmethod
    def add_aerial_vehicle(aerial_vehicle):
        """
        this method creates pressure from objects of the parent class aerial_vehicle
        :param aerial_vehicle: objects class AerialVehicle
        :return: aerial_vehicle
        """
        AerialVehicleManager.list.append(aerial_vehicle)
        return aerial_vehicle

    @staticmethod
    def filter_by_max_flying_distance(distance):
        """
        this method set list and filter parameter on get_max_flying_distance
        :param distance:
        :return: list
        """
        filtered_list = list(filter(lambda a: a.get_max_flying_distance() > distance, AerialVehicleManager.list))
        for item in filtered_list:
            print(item)

    @staticmethod
    def filter_by_max_delivery_weight(weight):
        """
        this method set list and filter parameter on get_max_delivery_weight
        :param weight:
        :return: list
        """
        filtered_list = list(filter(lambda a: a.get_max_delivery_weight() > weight, AerialVehicleManager.list))
        for item in filtered_list:
            print(item)


if __name__ == '__main__':
    drone = Drone(10000, 10, 150, 250, "Turkey", 2566, 100)
    helicopter = Helicopter(311, "Poland", 2899, 600)
    military_drone = MilitaryDrone(300, "USA", 4000, 300)
    plane = Plane(350, 246, 700, "USAh", 10000, 2500)

    AerialVehicleManager.add_aerial_vehicle(drone)
    AerialVehicleManager.add_aerial_vehicle(helicopter)
    AerialVehicleManager.add_aerial_vehicle(military_drone)
    AerialVehicleManager.add_aerial_vehicle(plane)

    for element in AerialVehicleManager.list:
        print(element)

    print("")
    AerialVehicleManager.filter_by_max_flying_distance(3000)

    print("")
    AerialVehicleManager.filter_by_max_delivery_weight(400)
