class ParkingSystem:




    def __init__(self, big: int, medium: int, small: int):
        self.bigSpots = 0 
        self.bigSpotsTaken = 0 
        self.mediumSpots = 0 
        self.mediumSpotsTaken = 0 
        self.smallSpots = 0 
        self.smallSpotsTaken = 0 

        self.bigSpots = big
        self.mediumSpots = medium
        self.smallSpots = small
    




        

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.bigSpotsTaken < self.bigSpots:
                self.bigSpotsTaken += 1
                return True
            else: 
                return False
        if carType == 2:
            if self.mediumSpotsTaken < self.mediumSpots:
                self.mediumSpotsTaken += 1
                return True
            else: 
                return False
        if carType == 3:
            if self.smallSpotsTaken < self.smallSpots:
                self.smallSpotsTaken += 1
                return True
            else: 
                return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)