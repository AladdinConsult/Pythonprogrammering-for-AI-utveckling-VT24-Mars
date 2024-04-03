# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

# point1 = Point(10,20)
# point2 = Point(15,25)
# # print(point1.x, point1.y)
# # print(point2.x, point2.y)

# # point1.x = 110
# # print(point1.x, point1.y)

# print(point1)



# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
    
#     def __repr__(self):
#         return f'Point(x={self.x}, y={self.y})'
    
#     def __str__(self):
#         return f'Point object with(x={self.x}, y={self.y})'


# point1 = Point(10,20)

# print(point1)
# print(repr(point1))


# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
    
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
    
    
        

# point1 = Point(10,20)
# point2 = Point(10,20)

# print(point1==point2)


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def swap_xy(self):
        self.x, self.y = self.y, self.x
    

point1 = Point(10,20)

point1.swap_xy()
print(point1.x, point1.y)