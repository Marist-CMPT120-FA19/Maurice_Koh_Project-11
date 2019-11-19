#Maurice Koh
#zhi.koh1@marist.edu
#Convert Radius into Volume and Area

from math import *

class Sphere:
    #r = radius
    #s = self

    #creates the sphere with the radius input by the user
    def __init__(s,r):
        s.radius= r
        s.volume = ((4/3)*pi*(r**3))
        s.area = (4*pi*(r**2))

    #return radius
    def getRadius (s):
        return s.radius

    #return surface area
    def surfaceArea(s):
        return s.area

    #return the volume 
    def volume(s):
        return s.volume 
       

def main():
    r = float(input("Please enter your radius: "))
    sphere = Sphere(r)

    volume = ((4/3)*pi*(r**3))
    area = (4*pi*(r**2))
    
    print("The volume of the sphere is: ", volume)
    print("The area of the sphere is: ", area)

main()
