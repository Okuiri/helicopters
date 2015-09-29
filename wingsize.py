# This script allows you to quickly tweak values for  


#------------------------------------------
# Coefficient of lift calculator for 
#    helicopters in a C-130J cargobay
# Inputs: Stall speed in kts,
#         chord in feet,
#         and gross weight of A/C in lbs
# Output the Stall C_L
#------------------------------------------


import math
from tabulate import tabulate

def calcStallCl(stallV, chord, weight):
    rho = 0.001756 #slugs/ft^3
    span = 103.0/12 #span in ft
    S = chord * span    #for rectangular planforms
    v = stallV * 1.6878 #convert from kts to ft/s

    return 2*weight/(rho*v**2*S)


#------------------------------------------
# Calculates the required chord of a 
# rectangular wing planform
# Inputs: Stall speed in kts,
#         coeficient of lift
#         span in feet,
#         and gross weight of A/C in lbs
# Output the Stall C_L
#------------------------------------------

def findReqdChord(stallV, cl, span, weight):
    rho = 0.001756 #slugs/ft^3 (density at 15000 ft ISA)
    v = stallV * 1.6878 #stallV converted to ft/s
    return (2*weight/(rho*(v**2)*cl*span))

print('Enter the following values in kts of airspeed')
maxStall = input(' Enter max stall speed: ')
minStall = input(' Enter minimum stall speed: ')
step = input(' Enter a step size: ')

speeds = range(minStall, maxStall+step, step)
results= [['Speed','chord']]

#Calculates the chord for each speed in the array
for speed in reversed(speeds):
     cl = 1.2
     span = 103.0/12
     weight = 2000
     results.append([speed, round(findReqdChord(speed,cl,span,weight),2)])
#------------------------------

print tabulate(results, headers="firstrow",tablefmt="fancy_grid")
    
    

