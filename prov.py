PI = 3.141593
class BeachBall:   
    def __init__(self, diameter = 0):
        if diameter > 50:
             self.diameter = 50
        elif diameter < 0:
             self.diameter = 0
        else:
            self.diameter = float(diameter)
        self.__volume = self.__calculate_volume()

 
    def inflate(self, increase: int) -> None:
        if increase > 0:
            self.diameter += increase
            if self.diameter > 50:
                print('BANG!')
                self.diameter = 0
                self.__volume = 0
            else:
                self.__volume = self.__calculate_volume()

 
    def deflate(self, decrease: int) -> None:
           if decrease > 0:
                self.diameter -= decrease
                if self.diameter <= 0:
                   self.diameter = 0
                   self.__volume = 0
                   print('The beach ball is deflated')
                else:
                    self.__volume = self.__calculate_volume()
 
    def __calculate_volume(self) -> float:
        radius = self.diameter / 2
        volume_cm3 = (4 * PI * (radius**3)) / 3
        return volume_cm3 / 1000
 
    def __str__(self) -> str:
        return 'Beach ball with volume: {:.1f} liters'.format(self.__volume)

	
my_ball = BeachBall(30)
my_ball.inflate(10)
print(my_ball)