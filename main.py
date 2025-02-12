from point import Point

# START #

p1 = Point()
p2 = Point(10, 20)
p3 = Point.empty()
p4 = Point.from_xy(100, 200)
p5 = Point.from_copy(p4)

p1.show()
p2.show()
p3.show()
p4.show()
p5.show()
