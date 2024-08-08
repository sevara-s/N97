#Ne'matullayeva Sevara 1-misol:
class spaceAircraft:
    def __init__(self,model,height,fuel):
        self.model=model
        self.heigth=height
        self.fuel=fuel
    def launch(self,km):
        if self.fuel>km:
            self.fuel-=km
            print(f"remaining fuel= {self.fuel} ")
        else:
            print(f"No fuel")

    def land(self,km):
        if self.fuel > km:
            print("enough fuel to land")
        else:
            print("No fuel")
model=input("model=")
height=int(input("height="))
fuel=int(input("fuel="))
aircraft=spaceAircraft(model,height,fuel)
land=int(input("land(km)="))
launch=int(input("launch(km)="))
aircraft.launch(launch)
aircraft.land(land)

