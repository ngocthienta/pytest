points = [(0, 0), (3, 4), (-1, -1)]
if type(points) == type(None) or len(points) < 2 :
    raise ValueError("The list MUST contain at least 2 points")
import math
x_coors, y_coors = [], []
for i in points :
    x_coors.append(i[0])
    y_coors.append(i[1])
total_dis = 0
for i in range(len(x_coors)-1) :
    total_dis += math.sqrt((x_coors[i]-x_coors[i+1])**2 + (y_coors[i]-y_coors[i+1])**2)
print (total_dis)
