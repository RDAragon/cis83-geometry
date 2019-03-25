"""
NAME: main.py
AUTHOR: Roger Aragon
DATE: 3/24/19
EMAIL: aragonr87056@student.vvc.edu
DESCRIPTION: calculates volume and surface areas
             of various geometric shapes
"""

import math

def sphere_volume (radius):
    sph_vol = ((4 / 3) * math.pi * math.pow(radius, 3))
    return sph_vol

def sphere_surface (radius):
    sph_sur = (4 * math.pi * math.pow(radius, 2))
    return sph_sur

def cyl_volume (radius, height):
    cyl_vol = (math.pi * math.pow(radius, 2) * height)
    return cyl_vol

def cyl_surface (radius, height):
    cyl_sur = (2 * math.pi * radius * (radius + height))
    return cyl_sur

def cone_volume (radius, height):
    cone_vol = ((1 / 3) * math.pi * math.pow(radius, 2) * height)
    return cone_vol

def cone_surface (radius, height):
    slope = (math.sqrt(math.pow(radius, 2) + math.pow (height, 2)))
    cone_sur = (math.pi * radius * (radius + slope))
    return cone_sur


radius = int(input('Enter radius: '))

height = int(input('Enter height: '))

print ('Sphere of radius', radius)
print ('volume:', sphere_volume(radius))
print ('Surface area:', sphere_surface(radius))
print (' ')

print ('cylinder of radius', radius, 'and height of', height)
print ('volume:', cyl_volume(radius, height))
print ('Surface area:', cyl_surface(radius, height))
print (' ')

print ('Cone of radius', radius,'and height of', height)
print ('volume:', cone_volume(radius, height))
print ('Surface area:', cone_surface(radius, height))
print (' ')
