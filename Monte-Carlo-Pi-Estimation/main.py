import random 

"""
Monte Carlo methods are a broad class of computational algorithms that rely on 
repeated random sampling to obtain numerical results. 

IDEA BEHIND ESTIMATION OF PI:
Simulate random (x, y) points in a 2-D plane with a domain of a square of side 2r 
units centered on (0, 0). Imagine a circle inscribed inside this square with radius r. 
We calculate the ratio of number of points on the inside of the circle ot the total 
number of points

Area of a square is 4r^2. 
Area of a circle is pi*r^2

Area of circle / area of the square = pi/4
pi = ( Area of circle / area of square ) * 4
"""

INTERVAL = 1000000 

circle_points = 0
square_points = 0

# Total Random numbers = possible x vals * possible y vals 
# 1000 * 1000 = 1000 ^ 2
# Radius is 1, with origin at the center of the circle
for i in range( INTERVAL * 2 ):
    rand_x = random.uniform( -1, 1 )
    rand_y = random.uniform( -1, 1 )

    # Distance between point and the origin to figure out if it's in the circle
    origin_distance = ( rand_x ** 2 + rand_y ** 2 ) ** 0.5

    if origin_distance <= 1: # less than radius
        circle_points += 1
    
    square_points += 1

    # Pi Estimation 
    pi = 4 * circle_points / square_points 

print( "Estimation of Pi =", pi )
