class Pencil:                                               # Class created
    type = "hi-tech"                                        # Class attribute
    model = "Parker"                                        # Class attribute

    def __init__(self, color="grey", price="free"):      # constructor
        self.color = color                                  # Class attribute
        self.__price = price                                # encapsulation - private attribute

    def draw_picture(self):                                 # method
        return f"Нарисован рисунок цветом '{self.color}'."

    def __str__(self):                                      # polymorphism_1.1
        return f"The pencil, {self.color}, {self.model}; {self.__price}, {self.type}"


class Pen(Pencil):                                          # inheritance(inheritance)
    def sign_document(self):                                # method
        if self.color not in ("blue", "black", "violet"):
            return f"Ручкой цвета '{self.color}' нельзя подписать документ."
        return f"Подписан документ."

    def __str__(self):                                  # polymorphism_1.2
        return f"The pen, {self.color}, {Pencil.model}; {self._Pencil__price}"


if __name__ == "__main__":
    blue_pen = Pen(color="blue")
    print(blue_pen.draw_picture())
    print(blue_pen.sign_document())
    red_pen = Pen(color="red")
    print(red_pen.draw_picture())
    print(red_pen.sign_document())
    print(red_pen)                                          # The pen, Parker; free
    #print(Pencil.color)                                     # AttributeError
    print(Pencil.type)                                      # hi-tech
    # MODIFICATION
    print(blue_pen.color)                                   # blue
    blue_pen.color = "green"
    print(blue_pen.color)                                   # green
    # ENCAPSULATION
    pencil = Pencil("black", "$100")
    print(pencil)                                           # The pencil, black, Parker; $100, hi-tech
    pencil.color = "white"
    pencil.price = "$900"
    print(pencil)                                           # The pencil, white, Parker; $100, hi-tech
    pencil._Pencil__price = "$900"
    print(pencil)                                           # The pencil, white, Parker; $900, hi-tech


class Pencil:
    __slots__ = ["color", "__model", "price"]               #

    def __init__(self, price="free", color="grey", model="Parker"): # constructor
        self.color = color
        self.__model = model                                # encapsulation - private attribute
        self.price = price

    def draw_picture(self):                                 # method
        return f"Нарисован рисунок цветом '{self.color}'."

    def __str__(self):
        return f"{self.color}, {self.__model}"


class Pen(Pencil):                                          # inheritance(inheritance)
    #__slots__ = ["color"]                                  #
    def __init__(self, price, pen_type, color="black", model="Parker"): # new constructor
        super().__init__(price=price, color=color)          # old methods added
        self.pen_type = pen_type                            # extension, new method added
        self.__model = model                                # __ couldn't be inherited

    def sign_document(self):                                # method
        if self.color not in ("blue", "black", "violet"):
            return f"Ручкой цвета '{self.color}' нельзя подписать документ."
        elif self.pen_type == "гелевая":
            return f"Ручкой типа '{self.pen_type}' нельзя подписать документ."
        return f"Подписан документ."

    def __str__(self):
        return f"{self.color}, {self.__model}, {self.pen_type}, {self.price}"


if __name__ == "__main__":
    blue_ball_pen = Pen(color="blue", pen_type="шариковая", price="free")
    print(blue_ball_pen.draw_picture())
    print(blue_ball_pen.sign_document())
    blue_gel_pen = Pen("free", color="blue", pen_type="гелевая")
    print(blue_gel_pen.draw_picture())
    print(blue_gel_pen.sign_document())
    #print(blue_ball_pen)                                    # AttributeError _Pen__model
    print(blue_gel_pen)                                     # blue, Parker, гелевая, free
#    pen = Pen("ball")                                       # TypeError: missing 'pen_type'
    pen = Pen("free", "ball")
    print(pen)                                              # black, Parker, ball, free


class Polygon:

    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
# or
#    def __init__(self, no_of_sides=3):
#        super().__init__(no_of_sides=no_of_sides)

    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


x3 = Triangle()
x3.inputSides()
x3.findArea()


class Plants:
    name = None

    def flowing(self):
        print("Regular/irregular flowing with rain/tap water", end="")


class HousePlants(Plants):
    def flowing(self):
        print("")
        super().flowing()
        print(", adding fertilizer as well")


flower = Plants()
flower.flowing()                # Regular/irregular flowing with rain/tap water

cactus = HousePlants()
cactus.flowing()                # Regular/irregular flowing with rain/tap water, adding fertilizer as well
