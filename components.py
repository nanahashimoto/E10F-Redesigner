class Panel:
    def __init__ (self, width, height):
        self.width = width
        self.height = height

        self.neutralAxis = height/2

        self.momentOfInertia = 1/12*width*math.pow(height,3)

class LBracket:
    def __init__ (self, width, thickness):
        self.width = width
        self.thickness = thickness

        smallestRectangleMoment = 1/12*math.pow((width-thickness), 4)
        biggestRectangleMoment = 1/12*math.pow(width, 4)

        self.frontalArea = (2*width-thickness)*thickness

        self.neutralAxis = 1/self.frontalArea*(thickness/2*(math.pow(width, 2) + width*thickness - math.pow(thickness, 2)))

        self.momentOfInertia = biggestRectangleMoment-smallestRectangleMoment + (self.neutralAxis-thickness/2)*(width-thickness)*thickness + (width/2-self.neutralAxis)*(width-thickness)*thickness