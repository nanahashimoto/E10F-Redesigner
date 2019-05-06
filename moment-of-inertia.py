import math

from components import Panel, LBracket

print("-------------------------")
print("E10F - Offical Redesigner")
print("-------------------------")

print("\nWritten by:\n")
print(" - Douwe den Blanken")
print(" - Stein Munting\n")

print("-------------------------\n")

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
    print("\nOkay! Maybe see you later!")

else:
    print("\nAlrighty, let's go!")


# 6 stringers
# thickness
# material (steel/material
# 288 options

# 4 and 6 graph lines for K_c