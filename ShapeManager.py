class Shape:
    _counter = 0
    _shape = 'Shape'

    def __init__(self, description):
        self.description = description
        Shape._counter += 1

    def area(self):
        return 0

    def volume(self):
        return 0

    def __str__(self):
        return f'Object: {self._shape} \nDescription: {self.description} \nArea of object: {self.area()} \nVolume of object: {self.volume()}\n'


class TwoDimensionalShape(Shape):
    _shape = 'Two-dimensional Shape'

    def __init__(self, description):
        super().__init__(description)

    def __str__(self):
        return super().__str__()


class ThreeDimensionalShape(Shape):
    _shape = 'Three-Dimensional Shape'

    def __init__(self, description):
        super().__init__(description)

    def __str__(self):
        return super().__str__()


class Square(TwoDimensionalShape):
    _shape = 'Square'

    def __init__(self, description, length: int):
        self.length = length
        super().__init__(description)

    def area(self):
        return self.length * self.length

    def __str__(self):
        return super().__str__()


class Rectangle(TwoDimensionalShape):
    _shape = 'Rectangle'

    def __init__(self, description, length: int, width: int):
        self.length = length
        self.width = width
        super().__init__(description)

    def area(self):
        return self.length * self.width

    def __str__(self):
        return super().__str__()


class Cube(ThreeDimensionalShape):
    _shape = 'Cube'

    def __init__(self, description, length: int):
        self.length = length
        super().__init__(description)

    def area(self):
        return (self.length * self.length) * 6

    def volume(self):
        return (self.length * self.length) * self.length

    def __str__(self):
        return super().__str__()



class Box(ThreeDimensionalShape):
    _shape = 'Box'

    def __init__(self, description, length: int, width: int, height: int):
        self.length = length
        self.width = width
        self.heigth = height
        super().__init__(description)

    def area(self):
        side_a = (self.length * self.width) * 4
        side_b = (self.width * self.heigth) * 2
        return side_a + side_b

    def volume(self):
        return (self.length * self.width) * self.heigth



square1 = Square('Squares have all equal sides', 7)
rectangle1 = Rectangle('A rectangle has unequal side lenghts', 12, 6)
cube1 = Cube('this object is three-dimensional', 13)
box1 = Box('three-dimensional, but with 3 different sides', 12,9,10)

obj_list = [square1, rectangle1, cube1, box1]

def main():
    for obj in obj_list:
        print(obj)
    print(Shape._counter)

if __name__ == '__main__': main()
