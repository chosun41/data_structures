class ParkingSystem:
    
    def __init__(self, big: int, medium: int, small: int):
        self.parking_spaces = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if not self.parking_spaces[carType]: 
            return False
        if self.parking_spaces[carType]>0:
            self.parking_spaces[carType] -= 1
            return True

if __name__=='__main__':

    # Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

    # Implement the ParkingSystem class:

    # ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
    # bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.
    

    # Example 1:

    # Input
    # ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
    # [[1, 1, 0], [1], [2], [3], [1]]
    # Output
    # [null, true, true, false, false]

    # Explanation
    parkingSystem = ParkingSystem(1, 1, 0)
    print(parkingSystem.addCar(1)) # // return true because there is 1 available slot for a big car
    print(parkingSystem.addCar(2)) # // return true because there is 1 available slot for a medium car
    print(parkingSystem.addCar(3)) #// return false because there is no available slot for a small car
    print(parkingSystem.addCar(1)) # // return false because there is no available slot for a big car. It is already occupied.