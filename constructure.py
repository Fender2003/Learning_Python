class Point:
    def __init__(self,x,y):# this method is called as constructure which hepls to create an object
        self.x=x #here self lets create any object afterwards
        self.y=y
    def move(self):
        print("moving")


    def draw(self):
        print("drawing")

point=Point(10,20)
print(point.x)

point.x=11 #if we change the value to
print(point.x)
