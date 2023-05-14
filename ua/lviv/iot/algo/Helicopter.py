class Helicopter:
    """
    this class succinctly describes the helicopter speed, the height of the remaining fuel
    """
    def __init__(self, current_altitude, new_altitude, fuel_updated,
                 id_is=100, max_altitude=1000, fuel_capacity=30,
                 current_fuel=10):
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

        self.id_is = id_is
        self.fuel_updated = fuel_updated
        self.current_altitude = current_altitude
        self.new_altitude = new_altitude
        self.max_altitude = max_altitude
        self.fuel_capacity = fuel_capacity
        self.current_fuel = current_fuel

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


if __name__ == '__main__':
    helicopter = Helicopter(1000, 1000, 50)
    helicopter.refuel(15)
    helicopter.descend(123)
    helicopter.take_off()
    helicopter.ascend(5000)
