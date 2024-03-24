'''
WORK IN PROGRESS
'''

import math
import numpy as np
import pandas as pd
from tabulate import tabulate

n = 4
d = 200000
totalNumberUnitCubes=math.pow(n,3)

probUnitCubeWithThreeRedFaces = 8/totalNumberUnitCubes
probUnitCubeWithTwoRedFaces = (n-2)*12/totalNumberUnitCubes
probUnitCubeWithOneRedFaces = 6*(math.pow((n-2),2))/totalNumberUnitCubes
probUnitCubeWithZeroRedFaces = math.pow((n-2),3)/totalNumberUnitCubes

probRedFaceZero = 0
probRedFaceOne = 1/6
probRedFacesTwo = 1/3
probRedFacesThree = 1/2

totalProbRedZeroFaces = probUnitCubeWithZeroRedFaces*probRedFaceZero
totalProbRedOneFace = probUnitCubeWithOneRedFaces*probRedFaceOne
totalProbRedTwoFaces = probUnitCubeWithTwoRedFaces*probRedFacesTwo
totalProbRedThreeFaces = probUnitCubeWithThreeRedFaces*probRedFacesThree
totalProbRedFace = totalProbRedZeroFaces + totalProbRedOneFace + totalProbRedTwoFaces + totalProbRedThreeFaces

totalProbNonRedZeroFaces = (probUnitCubeWithZeroRedFaces)*(1-probRedFaceZero)
totalProbNonRedOneFace = (probUnitCubeWithOneRedFaces)*(1-probRedFaceOne)
totalProbNonRedTwoFaces = (probUnitCubeWithTwoRedFaces)*(1-probRedFacesTwo)
totalProbNonRedThreeFaces = (probUnitCubeWithThreeRedFaces)*(1-probRedFacesThree)
totalProbabilityNonRedFace = totalProbNonRedZeroFaces + totalProbNonRedOneFace + totalProbNonRedTwoFaces + totalProbNonRedThreeFaces

numberRedFacesDrawnCube = [0, 1, 2, 3]
probabilities = [probUnitCubeWithZeroRedFaces, 
                 probUnitCubeWithOneRedFaces, 
                 probUnitCubeWithTwoRedFaces, 
                 probUnitCubeWithThreeRedFaces]
numberOfRedFacesOfDrawnCubes = (np.random.choice(numberRedFacesDrawnCube, d, p=probabilities)).tolist()
dfAbsoluteFrequencies = pd.DataFrame(columns=['Cubes with 0 red faces','Cubes with 1 red face',
                           'Cubes with 2 red faces','Cubes with 3 red faces'],
                 index=['Red face','Non-red face'])
for col in dfAbsoluteFrequencies.columns:
    dfAbsoluteFrequencies[col].values[:] = 0

for i in range(0,d):
    bernoulliVar = None
    if numberOfRedFacesOfDrawnCubes[i] == 0: 
            dfAbsoluteFrequencies.at['Non-red face', 'Cubes with 0 red faces'] += 1
    elif numberOfRedFacesOfDrawnCubes[i] == 1: 
        bernoulliVar = ((np.random.binomial(1, probRedFaceOne, 1)).tolist())[0]
        if bernoulliVar == 1:
            dfAbsoluteFrequencies.at['Red face', 'Cubes with 1 red face'] += 1
        else:
            dfAbsoluteFrequencies.at['Non-red face', 'Cubes with 1 red face'] += 1
    elif numberOfRedFacesOfDrawnCubes[i] == 2:
        bernoulliVar = ((np.random.binomial(1, probRedFacesTwo, 1)).tolist())[0]
        if bernoulliVar == 1:
            dfAbsoluteFrequencies.at['Red face', 'Cubes with 2 red faces'] += 1
        else:
            dfAbsoluteFrequencies.at['Non-red face', 'Cubes with 2 red faces'] += 1
    else:
        bernoulliVar = ((np.random.binomial(1, probRedFacesThree, 1)).tolist())[0]
        if bernoulliVar == 1:
            dfAbsoluteFrequencies.at['Red face', 'Cubes with 3 red faces'] += 1
        else:
            dfAbsoluteFrequencies.at['Non-red face', 'Cubes with 3 red faces'] += 1

dfAbsoluteFrequencies.loc[:,'Sum'] = dfAbsoluteFrequencies.sum(axis=1)
dfAbsoluteFrequencies.loc['Sum',:] = dfAbsoluteFrequencies.sum(axis=0)
dfRelativeFrequencies=(dfAbsoluteFrequencies/d).round(2)
dfTheoreticalFrequencies = pd.DataFrame([
    [totalProbRedZeroFaces, totalProbRedOneFace, totalProbRedTwoFaces, totalProbRedThreeFaces],
    [totalProbNonRedZeroFaces, totalProbNonRedOneFace, totalProbNonRedTwoFaces, totalProbNonRedThreeFaces]
        ], columns=['Cubes with 0 red faces','Cubes with 1 red face',
                           'Cubes with 2 red faces','Cubes with 3 red faces'],
                 index=['Red face','Non-red face'])
dfTheoreticalFrequencies.loc[:,'Sum'] = dfTheoreticalFrequencies.sum(axis=1)
dfTheoreticalFrequencies.loc['Sum',:] = dfTheoreticalFrequencies.sum(axis=0)

print('Here is the table with the absolute frequencies:\n')
print(tabulate(dfAbsoluteFrequencies, headers=['Cubes with 0 red faces','Cubes with 1 red face','Cubes with 2 red faces','Cubes with 3 red faces', 'Sum']))
print('\nHere is the table with the corresponding relative frequencies:\n')
print(tabulate(dfRelativeFrequencies, headers=['Cubes with 0 red faces','Cubes with 1 red face','Cubes with 2 red faces','Cubes with 3 red faces', 'Sum']))
print('\nHere is the table with the theoretical frequencies:\n')
print(tabulate(dfTheoreticalFrequencies, headers=['Cubes with 0 red faces','Cubes with 1 red face','Cubes with 2 red faces','Cubes with 3 red faces', 'Sum']))

    
