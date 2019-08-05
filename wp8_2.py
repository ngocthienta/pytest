import math
def calculate_euclidean_distance_between_2_points(p1, p2):
    if not isinstance(p1,tuple) or not isinstance(p2,tuple):
        raise TypeError('A tuple is expected')
    for i in range(len(p1)):
        if not isinstance(p1[i],int) or not isinstance(p2[i],int):
            raise ValueError('Coordinates must be integers')
    euclid_dis = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    return euclid_dis

def calculate_euclidean_distance_between_points(points):
    if not isinstance(points,list):
        raise ValueError
    if len(points) < 2:
        raise ValueError("The list MUST contain at least 2 points")
    total_dis = 0
    for i in zip(points,points[1:]):
        total_dis += calculate_euclidean_distance_between_2_points(i[0],i[1])
    return total_dis
print(calculate_euclidean_distance_between_2_points((0, 0),(3, 4)))
