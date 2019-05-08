# ------------------------------------------------------
# Imports
# ------------------------------------------------------

import math
import sys

from components import Panel, Stringer, Design, Material

# ------------------------------------------------------
# Terminal Setup
# ------------------------------------------------------

print("")
print("=============================")
print("| E10F - Offical Redesigner |")
print("=============================")

print("\nWritten by:\n")
print(" - Douwe den Blanken")
print(" - Stein Munting\n")
print("Last edited: 8 May 2019\n")

print("-----------------------------\n")

sStart = input("Do you want to start? (Y/n) ")

bStart = None

while True:
    if sStart == "Y":
        bStart = True
        break

    if sStart == "n":
        bStart = None
        break

    bStart = None

if bStart == None:
    print("\nOkay! Maybe see you later!\n")
    sys.exit()

else:
    print("\nAlrighty, let's go! 🚀\n")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# ------------------------------------------------------
# Property definitions [SI UNITS!]
# ------------------------------------------------------

# Load definitions
fUltimateLoad    = 30.0*math.pow(10, 3)
fLimitLoad       = 15.0*math.pow(10, 3)
fKC              = 3.6
fC               = 2.1
fRivetSpacing    = 0.07

# Panel properties
fPanelWidth = 0.4

# Set the maximum amount of stringers
iMaxAmountOfStringers = 8

# Create an array with the available materials
arrMaterials =  [
                    Material("Steel",       1275*math.pow(10, 6),  210*math.pow(10, 9),   7800),
                    Material("Aluminum",    100*math.pow(10, 6),   72.4*math.pow(10, 9),  2780)
                ]

# Define an array with the different panel thicknesses
arrPanelThicknesses =   [
                            0.8/1000,
                            1.0/1000,
                            1.2/1000
                        ]

# Create an array with the different stringer/l-bracket types we can choose from
arrStringers =  [
                    Stringer(20/1000, 1.5/1000, arrMaterials[1]),
                    Stringer(20/1000, 2.0/1000, arrMaterials[1]),
                    Stringer(15/1000, 1.0/1000, arrMaterials[1]),
                    Stringer(15/1000, 1.5/1000, arrMaterials[1]),
                    Stringer(15/1000, 1.5/1000, arrMaterials[0]),
                    Stringer(15/1000, 2.0/1000, arrMaterials[0])
                ]

# ------------------------------------------------------
# Designs creation
# ------------------------------------------------------

# Initialize empty array which will hold every design after looping through every possibility
arrSufficientDesigns = []

for currentPanelMaterial in arrMaterials:

    for currentPanelThickness in arrPanelThicknesses:

        currentPanel = Panel(fPanelWidth, currentPanelThickness, currentPanelMaterial)

        # Need to have a minimum of two stringers, else division by 0 occurs
        for currentNumberOfStringers in range(2, iMaxAmountOfStringers):
        
            for currentStringer in arrStringers:

                currentDesign = Design(currentPanel ,currentStringer, currentNumberOfStringers, 0.5)
                
                if(currentDesign.IsSufficient(fUltimateLoad, fLimitLoad, fKC, fC, fRivetSpacing) == True):
                    arrSufficientDesigns.append(currentDesign)
                    print("\n" + currentDesign.ToString() + "\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# ------------------------------------------------------
# Optimial Design Choosing
# ------------------------------------------------------

print("\nAmount of valid designs: " + str(len(arrSufficientDesigns)) + "\n")

# KC OFFICIAL 3.6
# b = stringer pitch

# 4 and 6 graph lines for K_c