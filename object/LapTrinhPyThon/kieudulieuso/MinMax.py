from cmath import pi, sqrt
from math import degrees, hypot, radians
from random import random, randrange, uniform


z = min(1,2,0,4)
print(z)

z = max(9,8,0,1)
print(z)

## ra so ngau nhien trpng khoang 2 -> 20
z = randrange(6,20)
print(z)

## ra ngau nhien mot so thuc
z = uniform(2,5)
print(z)

### doi sang do
z = degrees(pi)
print(z)

### radians
z = radians(180)
print(z)

### tra ve sqrt(x*x+y*y)
z = hypot(3,4)
print(z)