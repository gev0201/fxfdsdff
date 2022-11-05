from rectangle import rectangle


class square(rectangle):

    def __init__(self, a):
        self.a = a
        print(a * a)


# creating object of the class
obj = square(10)
