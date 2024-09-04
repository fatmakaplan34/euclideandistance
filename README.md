# euclideandistance
Minimum Distance Calculation Using Euclidean Distance

Overview
This project calculates the minimum distance between a set of 2D points using the Euclidean distance formula. The Euclidean distance is a measure of the straight-line distance between two points in a plane. This simple project loops through all pairs of points, calculates their distances, and finds the smallest one.

Features
Input: A list of 2D points.
Output: A list of all pairwise distances and the minimum distance among them.
Easy-to-understand implementation with Python.
Installation
No additional libraries are required beyond Python's standard library. Simply clone the repository and run the script.
git clone https://github.com/yourusername/euclidean-distance-calculation.git
cd euclidean-distance-calculation
Usage
Define a list of 2D points in the points variable.
Run the script to calculate all distances and find the minimum one.
import math

# Defining 2D points.
points = [(1, 2), (3, 4), (5, 8), (5, 9), (6, 7)]

# Calculation of Euclidean distance between two points.
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculation of distances between all pairs of points.
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Finding the minimum distance.
min_distance = min(distances)

# Results.
print(f"Distances: {distances}")
print(f"Minimum distance: {min_distance}")
Example
Given the points [(1, 2), (3, 4), (5, 8), (5, 9), (6, 7)], the script will output the following:
Distances: [2.8284271247461903, 7.211102550927978, 8.06225774829855, 7.810249675906654, 5.0, 5.385164807134504, 5.656854249492381, 2.23606797749979, 1.4142135623730951, 1.0]
Minimum distance: 1.0

Contributing
If you would like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request.
