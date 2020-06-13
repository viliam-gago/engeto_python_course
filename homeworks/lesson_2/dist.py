import math

a = [0,0]
b = [0,0]

a[0] = int(input('Point A, X Coordinate: '))
a[1] = int(input('Point A, Y Coordinate: '))

b[0] = int(input('Point B, X Coordinate: '))
b[1] = int(input('Point B, Y Coordinate: '))

delta_x = abs(a[0]-b[0])
delta_y = abs(a[1]-b[1])

c = math.sqrt(delta_x**2 + delta_y**2)
print(round(c,2))