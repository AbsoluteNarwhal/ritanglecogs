import math

# x is in hours!

def getVolume(x):
    print(f"big volume: {(4/3) * math.pi * (1000**3)} little volume: {(4/3) * math.pi * (1000 - (x / 24))**3} little radius: {1000 - (x/24)}")
    return ((4/3) * math.pi * (1000**3)) - ((4/3) * math.pi * (1000 - (x / 24))**3)

def getHeight(V):
    a = (6 * math.sqrt(2) * V) ** (1/3)
    return a * math.sqrt(2/3)

x0 = 10 * 24
x1 = (10 + 0.001) * 24

height_0 = getHeight(getVolume(x0))
height_1 = getHeight(getVolume(x1))

print(f"x0 volume: {getVolume(x0)} x1 volume: {getVolume(x1)}")
print((height_1 - height_0) / x1 - x0)