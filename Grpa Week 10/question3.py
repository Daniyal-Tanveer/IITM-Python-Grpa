class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side
        self.compute_area()  # call it here

    def compute_area(self):
        self.area = self.side * self.side
