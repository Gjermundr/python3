class Shape:
    _counter = 0

    def __init__(self, name: str, description: str,):
        self.name = name
        self.description = description
        Shape._counter += 1

    def display_description(self):
        return f'Shape: {self.name} \nDescription: {self.description} \nArea of shape: {self.area()} \nVolume of shape: {self.volume()}'

    def area(self):
        return 0
    

    def volume(self):
        return 0

    def __str__(self):
        return 'One-Dimensional Shape'


class TwoDimensionalShape(Shape):
    def __init__(self, name, description):
       super().__init__(name, description)

    def __str__(self):
        return 'Two-Dimensional Shape' + super().description




thing = Shape('a line', 'a fucking line')

print(thing.display_description())