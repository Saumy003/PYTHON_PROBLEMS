# Create a function that gives parameter and area of a circle by its radius

def circle(radius):
        area = 3.14 * (radius*radius)
        para = 2 * 3.14 * radius
        return area , para

a ,c = circle(3)

print("Area :" , a)
print("Parameter:" , c)


