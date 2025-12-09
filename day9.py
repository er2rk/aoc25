points = []
with open("day9input") as data:
    for line in data:
        point_string = line.strip()
        point_string = point_string.split(",")
        x = int(point_string[0])
        y = int(point_string[1])
        point = [x, y]
        points.append(point)

#part1
#easiest way to do this requires n^2 time complexity. maybe there's a better solution.

max_area = 0
point_count = len(points)

for i in range(point_count):
    point1 = points[i]
    for j in range(i+1, point_count):
        point2 = points[j]
        #The plus ones are there because if two points are on the same line it counts as 1.
        width = abs(point2[0]-point1[0]) + 1
        length = abs(point2[1]-point1[1]) + 1
        area = width*length
        if area > max_area:
            max_area = area


#part2
#The idea goes i first find the horizontal connections, then the vertical connections.
#Afterwards i can go perpendicular to the horizontal connections then the vertical connections.

