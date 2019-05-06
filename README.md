**Written by [Douwe den Blanken](https://www.linkedin.com/in/douwedenblanken/) and [Stein Munting](https://www.linkedin.com/in/stein-munting-009301185/)**

# E10F Redesigner

This piece of Python code was developed to calculate the optimal top panel configuration for the AE-1110-I project, part 8. The file `components.py` contains the various classes used in the program. The file `redesigner.py` contains the UI, the values used in the calculation and the final result.

## Checks being run

The following formulas are being calculated per design:

### Panel Buckling

![Panel Buckling Equation](https://latex.codecogs.com/gif.latex?%5Csigma_%7Bcr%7D%20%3D%20K_c*E*%5Cbigg%28%5Cfrac%7Bt%7D%7Bs%7D%5Cbigg%29%5E2)

The critical sigma value should be bigger than the stress at the limit load of, in our case 15.0 kN.

### Column Buckling

![Column Buckling Equation](https://latex.codecogs.com/gif.latex?F_%7Bcr%7D%3D%5Cfrac%7Bc%5Cpi%5E2EI%7D%7BL%5E2%7D)

The critical load value times the amount of stringers should be bigger than the ultimate load, which was 30.0 kN in our case.

### Inter Rivet Buckling

![Inter Rivet Buckling Equation](https://latex.codecogs.com/gif.latex?%5Ctau_%7Bir%7D%20%3D%200.9K_cE%5Cbigg%28%5Cfrac%7Bt%7D%7Bs%7D%5Cbigg%29%5E2)

The inter rivet tau should be between the stress at the ultimate load and at the limit load, so between the stress from 30.0 kN and 15.0 kN of load.

## How to use

Click on the green 'Clone or Download button' and hit 'Download ZIP'. Unzip the package and navigate into the `code` folder. Open your terminal/command prompt in this folder and type the following:

```bash
python3 redesigner.py
```
