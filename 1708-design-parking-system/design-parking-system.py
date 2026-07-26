class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.max_size = [big, medium, small]
        self.filled = [0] * 3

    def addCar(self, carType: int) -> bool:
        if self.filled[carType - 1] == self.max_size[carType - 1]:
            return False
        self.filled[carType - 1] += 1
        return True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)