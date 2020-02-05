class Shape:
    '''base class for all child-classses/objects'''
    _counter = 0                         # A counter for each object created
    _shape = 'Shape'                     # Class variable declaring type of object/shape

    def __init__(self, description):
        self.description = description
        Shape._counter += 1             # <- Statement that increments the class variable each time constructor is called

    def area(self):
        '''The areal calculation of object'''
        return 0

    def volume(self):
        '''the volume calculation of object'''
        return 0

    def __str__(self):
        '''layout for all sub-classes and objects with shape, description, area, volume'''
        return f'Object: {self._shape} \nDescription: {self.description}' \
               f' \nArea of object: {self.area()} \nVolume of object: {self.volume()}\n'


class TwoDimensionalShape(Shape):
    _shape = 'Two-dimensional Shape'            # Updating class variable with correct name

    def __init__(self, description):
        super().__init__(description)

    def __str__(self):
        return super().__str__()                # inherit __str__ of base class: Shape


class ThreeDimensionalShape(Shape):
    _shape = 'Three-Dimensional Shape'          # Updating class variable with correct name

    def __init__(self, description):
        super().__init__(description)

    def __str__(self):
        return super().__str__()                # inherit __str__ of base class: Shape


class Square(TwoDimensionalShape):
    _shape = 'Square'

    def __init__(self, description, length: int):
        '''The square's sides are all equal lengths'''
        self.length = length
        super().__init__(description)

    def area(self):
        return self.length * self.length

    def __str__(self):
        return super().__str__()


class Rectangle(TwoDimensionalShape):
    _shape = 'Rectangle'

    def __init__(self, description, length: int, width: int):
        '''A rectangle has two unique side values'''
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
        '''The cube is three-dimensional with all sides being the same length'''
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
        '''The box is three-dimensional and has three values to consider when calculation surface area and volume'''
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


# Creating shape objects:
square1 = Square('Squares have all equal sides', 7)
rectangle1 = Rectangle('A rectangle has unequal side lenghts', 12, 6)
cube1 = Cube('this object is three-dimensional', 13)
box1 = Box('three-dimensional, but with 3 different sides', 12,9,10)

# Adding objects to a list
obj_list = [square1, rectangle1, cube1, box1]

def main():
    '''main function, contains all function calls and statements of the program'''
    for obj in obj_list:
        print(obj)
    print(Shape._counter)


# A statement that makes the processor load all lines of code into memory before calling main() function
if __name__ == '__main__': main()

