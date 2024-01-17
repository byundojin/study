import shape

s = shape.Shape(10, 20)

copy_s = shape.Shape.copy(s)

s.print()
copy_s.print()

s.x = 30

s.print()
copy_s.print()