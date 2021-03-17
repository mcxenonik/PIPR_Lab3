def centre_of_points(point1, point2):
    x = point1[0] + point2[0] / 2
    y = point1[1] + point2[1] / 2

    return x, y

print(centre_of_points((0, 0), (6,6)))