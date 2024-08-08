# Ne'matullayeva Sevara 2-misol:
class MinutesConverter:
    def __init__(self,minutes):
        self.minutes=minutes
    def toHours(self):
        self.hours=self.minutes//60
        print(f"hours= {self.hours} hr")
    def toSeconds(self):
        self.seconds=self.minutes*60
        print(f"seconds= {self.seconds} sec")
    def toDays(self):
        self.days=self.hours//24
        print(f"days= {self.days} days")
minutes=int(input("minutes ="))
convert=MinutesConverter(minutes)
convert.toHours()
convert.toSeconds()
convert.toDays()


    
