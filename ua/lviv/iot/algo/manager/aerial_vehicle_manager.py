"""
import class
"""
from datetime import datetime
from typing import Type

# pylint: disable=import-error
from ua.lviv.iot.algo.drone import Drone
from ua.lviv.iot.algo.helicopter import Helicopter
from ua.lviv.iot.algo.plane import Plane
from ua.lviv.iot.algo.military_drone import MilitaryDrone


def validate_method_name(func):
    """
    is a decorator that is designed to check the correct format of a method name
    :param func:as an argument and returns a nested wrapper function that validates the method
     name before calling it.
    :return: def wrapper()
    """

    def wrapper(*args, **kwargs):
        method_name = func.__name__
        if not method_name.islower() or "_" not in method_name:
            raise ValueError("Invalid method name. Method names should be in snake_case format")
        return func(*args, **kwargs)

    return wrapper


def log_method_calls(file_path):
    """
    is a decorator generator that adds logging to method calls
    :return: def decorator
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            method_name = func.__name__
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{timestamp} - {method_name}\n"

            with open(file_path, mode="a", encoding="utf-8") as log_file:
                log_file.write(log_entry)
            return func(*args, **kwargs)

        return wrapper

    return decorator


class AerialVehicleManager:
    """
    this class contains a list of classes and, thanks to the sheet,
     sucks the required objects
    """
    list = []

    @staticmethod
    def add_aerial_vehicle(aerial_vehicle):
        """
        this method creates pressure from objects of the parent
         class aerial_vehicle
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
        :return: item
        """
        filtered_list = list(filter(lambda a: a.get_max_flying_distance() > distance,
                                    AerialVehicleManager.list))
        for item in filtered_list:
            return item

    @staticmethod
    def filter_by_max_delivery_weight(weight):
        """
        this method set list and filter parameter on get_max_delivery_weight
        :param weight:
        :return: list
        """
        filtered_list = list(filter(lambda a: a.get_max_delivery_weight() > weight,
                                    AerialVehicleManager.list))
        for item in filtered_list:
            return item

    def __len__(self):
        """
         Returns the length of the AerialVehicleManager list
        :return:
        """
        return len(self.list)

    def __getitem__(self, item):
        """
        Returns the item at the given index from the AerialVehicleManager list
        :param item:
        :return: item
        """
        return self.list[item]

    def __iter__(self):
        """
        :return:an iterator for the AerialVehicleManager list
        """
        return iter(self.list)

    @validate_method_name
    def get_results_do_something(self, method: str):
        """
        :return:list of results from calling the do_something method
        on each object in the AerialVehicleManager list
        """
        return [getattr(obj, method)() for obj in self.list if hasattr(obj, method)]

    @log_method_calls("method_calls.log")
    def get_enumerated_list(self):
        """
        :return:a concatenation of the object and its index in the AerialVehicleManager list
        """
        return [[index, obj] for index, obj in enumerate(self.list)]

    @validate_method_name
    def get_zipped_results(self, method: str):
        """
        :return: a zip of the object and the result of the do_something method
        for each object in the AerialVehicleManager list
        """
        return zip(self.list, self.get_results_do_something(method))

    @validate_method_name
    def get_attributes_by_type(self, data_type: Type):
        """
        Returns a dictionary with keys and values of attributes from the object's __dict__
        where the values match the specified data_type
        """
        return {key: value for obj in self.list for key, value in obj.__dict__.items()
                if isinstance(value, data_type)}

    @validate_method_name
    def get_all_any_conditions(self, condition):
        """
        :param condition:  Checks if all objects in the AerialVehicleManager list satisfy
         a given condition,
        and if any object satisfies the condition
        :return: dictionary with "all" and "any" as keys and corresponding boolean values.
        """
        return {"all_true": all(condition(obj) for obj in self.list),
                "any_true": any(condition(obj) for obj in self.list)}


def main():
    """
    we check whether the values of the methods are output
    :return:
    """
    drone = Drone(10000, 10, 150, 250, "Turkey", 2566, 100, 100)
    helicopter = Helicopter(311, "Poland", 2899, 600, 100)
    military_drone = MilitaryDrone(300, "USA", 4000, 300, "military_drone")
    plane = Plane(350, 246, 700, "USAh", 10000, 2500, 124)

    AerialVehicleManager.add_aerial_vehicle(drone)
    AerialVehicleManager.add_aerial_vehicle(helicopter)
    AerialVehicleManager.add_aerial_vehicle(military_drone)
    AerialVehicleManager.add_aerial_vehicle(plane)

    for element in AerialVehicleManager.list:
        print(element)

    print("")
    print(AerialVehicleManager.filter_by_max_flying_distance(3000))

    print("")
    print(AerialVehicleManager.filter_by_max_delivery_weight(400))

    print("")
    manager = AerialVehicleManager()

    print(len(manager))

    print(manager[0])

    for element in manager:
        print(element)

    print(manager.get_results_do_something("do_something"))

    # Get the enumerated list
    print(manager.get_enumerated_list)

    # Get the zipped results of the do_something method
    print(manager.get_zipped_results("zipped_results"))

    # Get attributes of the objects with a specific data type
    print(manager.get_attributes_by_type(int))

    # Check if all objects satisfy a condition and if any object satisfies the condition
    print(manager.get_all_any_conditions(lambda obj: obj.get_max_flying_distance()))


if __name__ == '__main__':
    main()
