def is_inside_square(square, point):
    sx, sy, sl = square   # sx, sy = bottom-left corner of square; sl = side length
    px, py = point         # px, py = coordinates of the point

    # Check if the point is within the square's boundaries:
    # - The x-coordinate of the point must be between sx and sx + sl
    # - The y-coordinate of the point must be between sy and sy + sl
    # If both conditions are true, the point is inside or on the edge
    if sx <= px <= sx + sl and sy <= py <= sy + sl:
        return True
    else:
        return False

# Test cases
square = (2, 3, 4)
point1 = (4, 5)     # Inside
point2 = (7, 7)     # Outside
point3 = (2, 3)     # On the edge (still inside)

print(is_inside_square(square, point1))  # True
print(is_inside_square(square, point2))  # False
print(is_inside_square(square, point3))  # True
