import math
#(cx-px)^2 -+(cy-py)^2 <= r^2
def contains(c,p):

    # Task: Unpack the values and print them
    # Expected Output:
    cx,cy,r = c
    px,py = p

    # cx: 3.0, cy: 4.0, r: 2.0
    # px: 5.0, py: 6.0
    print("cx: ", cx, "cy: ",cy, "r: ", r)
    print("px: ", px, "py: ", py)

    # Using values from Challenge 1
    # Task: Compute dx and dy 
    # Print dx and dy
    dx = cx-px
    dy = cy-py
    print("dx: ", dx)
    print("dy: ", dy)

    distance_squared = dx*dx + dy*dy
    print("Distance squared: ", distance_squared)

    if math.pow((cx-px),2) - math.pow((cy-py),2) <= math.pow(r,2):
        print("true")
    else:
        print("false")

contains(3.0,4.0)