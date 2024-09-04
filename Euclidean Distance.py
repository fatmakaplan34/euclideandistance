import math
#Defining 2D points.
points= [(1,2),(3,4),(5,8),(5,9),(6,7)]
#Calculation of Euclidean distance of points.
def euclideanDistance (point1,point2):
    x1,y1= point1
    x2,y2= point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#Calculation of distances
distances=[]
for i in range(len(points)):
    for j in range(i+1,len(points)):
        dist=euclideanDistance(points[i],points[j])
        distances.append(dist)

#Finding minimum distance.
min_distance=min(distances)

#Results.
print(f"Distances: {distances}")
print(f"Minimum distance: {min_distance}")


