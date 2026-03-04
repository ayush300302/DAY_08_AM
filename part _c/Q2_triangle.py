def classify_triangle(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid input"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"

    if a == b == c:
        return "Equilateral"

    if a == b or b == c or a == c:
        return "Isosceles"

    return "Scalene"


print(classify_triangle(3,3,3))
print(classify_triangle(3,4,5))
print(classify_triangle(5,5,8))
print(classify_triangle(1,2,3))