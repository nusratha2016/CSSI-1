class SpaceShip:
  def __init__(self, SpaceShip_name, SpaceShip_style, SpaceShip_speed):
    self.name = SpaceShip_name
    self.style= SpaceShip_style
    self.speed= SpaceShip_speed

  def features(self):
    print " Space Ship color is %s , style is %s and speed is %s" % (self.name, self.style, self.speed)

Flash = SpaceShip ( 'Flash','Built for racing', 19730)
smooth = SpaceShip ('Smooth', 'classical', 1256)

print (Flash.name + ': ' + Flash.style)
print (smooth.name + ': ' + str(smooth.speed))

smooth.features()
