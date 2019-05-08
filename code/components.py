# ------------------------------------------------------
# Imports
# ------------------------------------------------------

import math

# ------------------------------------------------------
# Class/components definitions
# ------------------------------------------------------

# Simple class for the Panel component of the redesign
# Constructor calculates properties which are getters+setters
class Panel:
    def __init__ (self, width, height, material):
        self.width  = width
        self.height = height
        self.material = material

        self.area = width*height
        self.neutralAxis = height/2
        self.momentOfInertia = 1/12*width*math.pow(height, 3)

    # Give a string representation of the Panel object
    def ToString (self):
        return "   + Type: Panel\n     - Width: " + str(self.width) + " [m]\n     - Height: " + str(self.height) + " [m]\n     - Material:\n" + self.material.ToString()

# Create a class for the LBracket, containing all of its properties
class Stringer:
    def __init__ (self, width, thickness, material):
        self.width = width
        self.thickness = thickness
        self.material = material

        # This calculation could also be performed with a method of a static object
        smallestRectangleMoment = 1/12*math.pow((width-thickness), 4)
        biggestRectangleMoment = 1/12*math.pow(width, 4)

        self.area = (2 * width-thickness) * thickness
        self.neutralAxis = 1 / self.area * (thickness / 2 * (math.pow(width, 2) + width * thickness - math.pow(thickness, 2)))
        self.momentOfInertia = biggestRectangleMoment - smallestRectangleMoment - math.pow((self.neutralAxis-thickness/2), 2) * (width-thickness)*thickness - math.pow((width / 2-self.neutralAxis), 2) * (width-thickness) * thickness

    def ToString (self):
        return "   + Type: Stringer\n     - Width: " + str(self.width) + " [m]\n     - Thickness: " + str(self.thickness) + " [m]\n     - Material:\n" + self.material.ToString()

class Design:
    def __init__ (self, panel, stringer, amountOfStringers, length):
        self.panel = panel
        self.stringer = stringer
        self.amountOfStringers = amountOfStringers
        self.length = length

        self.area = self.GetTotalArea()
        self.mass = self.CalculateMass()

    def GetTotalArea (self):
        return self.panel.area + self.amountOfStringers * self.stringer.area
    
    def CalculateMass (self):
        return self.length*((self.amountOfStringers * self.stringer.area) * self.stringer.material.density + self.panel.area * self.panel.material.density)
    
    # Returns a boolean regarding whether the design is sufficient or not
    def IsSufficient (self, ultimateLoad, limitLoad, kC, c, minRivetSpacing):

        # Verify that the panel doesn't buckle before the limit stress
        def IsPanelBucklingOkay ():
            sigmaCritical = kC * self.panel.material.eModulus * math.pow((self.panel.height/fStringerPitch), 2)

            if(sigmaCritical > fLimitStress):
                return True
            else:
                return None

        # Check that columns buckling occurs AFTER the ultimate load
        def IsColumnBucklingOkay ():
            fCriticalLoad = c * math.pow(math.pi, 2) * self.stringer.material.eModulus * self.stringer.momentOfInertia / math.pow(self.length, 2)
            
            if fCriticalLoad * self.amountOfStringers > ultimateLoad:
                return True
            else:
                return None

        # Check whether inter rivet buckling occurs between the limit stress and ultimate stress
        def IsInterRivetBucklingOkay ():
            fTauInterRivet = 0.9 * kC * self.panel.material.eModulus * math.pow((self.panel.height/minRivetSpacing), 2)

            if fTauInterRivet < fUltimateStress and fTauInterRivet > fLimitStress:
                return True
            else:
                return None

        # Create some constants which the various check functions need
        fUltimateStress = ultimateLoad/self.area
        fLimitStress = limitLoad/self.area
        fStringerPitch = self.panel.width/(self.amountOfStringers-1)

        if IsPanelBucklingOkay() == True and IsColumnBucklingOkay() == True and IsInterRivetBucklingOkay() == True:
            return True

        else:
            return None

    def ToString (self):
        return "Type: Design\n ~ Mass: "  + str(round(self.mass, 3)) + " [kg]\n ~ Length: " + str(self.length) + " [m]\n ~ Amount of stringers: " + str(self.amountOfStringers) + "\n ~ Panel: \n" + self.panel.ToString() + "\n ~ Stringer: \n" + self.stringer.ToString()


class Material:
    def __init__ (self, name, sigmaUltimate, eModulus, density):
        self.name = name
        self.sigmaUltimate = sigmaUltimate
        self.eModulus = eModulus
        self.density = density

    # Return a string representation of the material
    def ToString (self):
        return "       > Type: Material\n         * Name: " + self.name + "\n         * Sigma Ultimate: " + str(round(self.sigmaUltimate/math.pow(10, 6), 3)) + " [MPa]\n         * E Modulus: " + str(round(self.eModulus/math.pow(10, 9), 3)) + " [GPa]\n         * Density: " + str(self.density) + " [kg/m^3]"