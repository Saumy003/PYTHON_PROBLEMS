# Write OOPS classes to handle the following scenarios:-

# 1. A user can create and view 2D coordinates
class Point:

    def __init__(self , x ,y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return "{},{}" .format(self.x_cod , self.y_cod)
    
# 2. A user can find distance between two points    

    def euclidean_distance(self , other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
# 3. A user can find the distance of a coordinate from origin

    def distance_from_origin(self):
        return ((self.x_cod)**2 + (self.y_cod)**2)**0.5
        # return self.euclidean_distance(Point(0,0)


p1 = Point(0,0)
p2 = Point(2 ,2)
distance = p1.euclidean_distance(p2)
print(distance)

origin_distance = p2.distance_from_origin()
print(origin_distance)

# 4. A user can check if a point lies on a line

class Line:
    def __init__(self , A , B, C):
        self.A = A
        self.B = B
        self.C = C
    def __str__(self):
        return "{}x + {}y + {} = 0".format(self.A , self.B , self.C)
    
    def point_on_line(line , point):
        if line.A * point.x_cod + line.B * point.y_cod + line.C == 0:
            print("Point lies on the line")
        else:
            print("Point does not lies on the line")

    # 5. A user can find the distance between a given 2D point and a given line

    def shortest_distance(line , point):
        return (line.A*point.x_cod + line.B*point.y_cod + line.C) / (line.A**2 + line.B**2)**0.5
    
# 4 -> code      
l1 = Line(3,4,5)
p1 = Point(2,1)

check = l1.point_on_line(p1)
print(check)

# 5 -> code
l2 = Line(4 ,5, 6)
p2 = Point(1 ,1)

shortdistance = l2.shortest_distance(p2)
print(shortdistance)