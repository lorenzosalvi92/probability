'''
WORK IN PROGRESS
'''

import math


def n_cubes_with_red_faces(n):
    threeRedFaces = 8
    twoRedFaces = (n-2)*12
    oneRedFace = 6*(math.pow((n-2),2))
    zeroRedFaces = math.pow((n-2),3)
    sumOfSmallCubes = threeRedFaces + twoRedFaces + oneRedFace + zeroRedFaces
    if math.pow(n,3) == sumOfSmallCubes:
        print('All good.')
        return sumOfSmallCubes
    else:
        print('Something in the calculation is wrong.')
        return 

n_cubes_with_red_faces(3)

    
