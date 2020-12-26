from ClassFigures import Rectangle, Square, Circle

rectangle1 = Rectangle(3, 8)
rectangle2 = Rectangle(4, 12)

square1 = Square(4)
square2 = Square(20)

circle1 = Circle(6)
circle2 = Circle(17)

figures = [rectangle1, rectangle2, square1, square2, circle1, circle2]

for figure in figures:
    if isinstance(figure, Rectangle):
        print(figure.get_area_rectangle())
    elif isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area_circle())
