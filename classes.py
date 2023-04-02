class Point:
    def move(self):
        print("moving")

    def draw(self):
        print("drawing")

point1=Point() #This makes point1 an object of Point class i.e. a variable that we can onnly define in Point class
point1.x=10 #this is defining as attribute to point1 named x
point1.y=20
print(point1.x)
point1.draw()

point2=Point()
#print(point2.x) this gives an error cause point2 doesnot have an attribute of x
