from objAttributes import Position

class Object:
    def __init__(self):
        self.position = Position()

    def __init__(self, x, y, z):
        self.position = Position(x, y, z)

    def move(self, x, y, z):
        self.position.setX(x)
        self.position.setY(y)
        self.position.setZ(z)

    def moveX(self, x):
        self.position.setX(x)

    def moveY(self, y):
        self.position.setY(y)

    def moveX(self, z):
        self.position.setZ(z)
