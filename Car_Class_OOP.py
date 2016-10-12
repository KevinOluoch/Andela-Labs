
class Car(object):
    """This class can be used to instantiate various vehicles.
    It takes in arguments that depict the type, model, and name of the vehicle,
    provided they are set
    It has methods for driving and stopping the vehicle
    """


    def __init__(self, name="General", model="GM", type_of_vehicle="saloon"):
        """This method initializes the objecct"""
        self.name =name
        self.model = model
        self.speed = 0
        self.num_of_doors = 4
        self.num_of_wheels = 4
        self.type_of_vehicle = type_of_vehicle

        #For Porshe and Koenigsegg the number of  doors is reduced to 2
        if name in ("Porshe", "Koenigsegg"): self.num_of_doors = 2
        #For trailers the number of wheels has to be increased to 8
        if type_of_vehicle is "trailer": self.num_of_wheels = 8

    def is_saloon(self):
        """This method confirms if a vehicle is a salon car"""
        if self.type_of_vehicle is "trailer":
            return False
        return True

    def drive(self, gear):
        """This method drives the car by changing the speed from zero"""
        if self.type_of_vehicle == "saloon":
            self.speed = 50*gear
        else:
            self.speed = 20*gear
        return self

    def stop(self):
        """This method is used to stop the car"""
        self.speed = 0



