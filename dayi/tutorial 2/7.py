import math
def Volume(R):
    V = (4*math.pi*R*R*R)/3
    return V
R = float(input("sphere radius:"))
print("volume is:",Volume(R))
