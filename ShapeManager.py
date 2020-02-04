class Shape:
    _counter = 0

    def __init__(self, name: str, description: str, axis_x: int):
        self.name = name
        self.description = description
        self.axis_x = axis_x
        Shape._counter += 1

    def area(self):
        return 0
    

    def volume(self):
        return 0

    def __str__(self):
        return f'Shape: {self.name} \nDescription: {self.description} \nArea of shape: {self.area()} \nVolume of shape: {self.volume()}'


class TwoDimensionalShape(Shape):
    def __init__(self, name: str, description: str, axis_x: int, axis_y: int):
        super().__init__(name, description, axis_x)
        self.axis_y = axis_y

    def __str__(self):
        return f'Two-Dimensional Shape: {self.name} \nDescription: {self.description} \nArea of shape: {super().area()} \nVolume of shape: {super().volume()}'


class ThreeDimensionalShape(TwoDimensionalShape):
    def __init__(self, name: str, description: str, axis_x: int, axis_y: int, axis_z: int):
        super().__init__(name, description, axis_x, axis_y)
        self.axis_z = axis_z

    def __str__(self):
        return f'Thee-Dimensional Shape: {self.name} \nDescription: {self.description} \nArea of shape: {super().area()} \nVolume of shape: {super().volume()}'




stickman = Shape('line', 'a fucking line', 40)
cube = ThreeDimensionalShape('cube', 'a cube with three axis', 32,20,11)

