import math
def distance(p1,p2):
    px,py = p1
    px2,py2 = p2
    return math.sqrt(math.pow(px2-px,2)+ math.pow(py2-py,2))

print("Distance: ",distance((0,0),(3,4)))