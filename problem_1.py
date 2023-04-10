
"""
Author: Laksha Karthikeyan
File Name: problem_1.py
for 1. Exercise 1, Page 36
Course Code: ECS 32B
Date completed: 04-09-2023

The sphere function created in this file uses the single radius parameter
(float) of a sphere, to calculate the diameter, circumference, surface area and volume
of a sphere. It returns a list of these values as float types in that particular
order.
"""
import math

def sphere(radius):
    # r = radius
    r = float(radius)
    # d = diameter = 2*radius
    d = float((2*r))
    # c = circumference = diameter(pi)
    c = float(d*(math.pi))
    # sa = surface area
    sa = float(4*math.pi*(r*r))
    # v = volume
    v = float((4/3)*(math.pi)*(r*r*r))
    # results list contains diameter, circumference, surface area and volume as floats
    results = [d, c, sa, v]
    print(results)

if __name__ == "__main__":
# Examples of sphere function calculations and output of list with radius of 2.56 and 6.119
    print("Example: List of the diameter, circumference, surface area, and volume of a sphere that has radius 2.56")
    sphere(2.56)
    print()
    print("list of diameter, circumference, surface area, and volume of a sphere that has radius 6.119")
    sphere(6.119)
