class Pencil:                                           # Class created
    type = "hi-tech"                                    # Class attribute
    model = "Parker"                                    # Class attribute
    def __init__(self, color="серый", price = "free"):  # constructor
        self.color = color                              # Class attribute
        self.__price = price                            # encapsulation - private attribute

    def draw_picture(self):                             # method
        return f"Нарисован рисунок цветом '{self.color}'."

    def __str__(self):                                  # polymorphism_1.1
        return f"The pencil, {self.color}, {self.model}; {self.__price}, {self.type}"


class Pen(Pencil):                                      # inheritance(inheritance)

    def sign_document(self):                            # method
        if self.color not in ("blue", "чёрный", "фиолетовый"):
            return f"Ручкой цвета '{self.color}' нельзя подписать документ."
        return f"Подписан документ."

    def __str__(self):                                  # polymorphism_1.2
        return f"The pen, {Pencil.model}; {self._Pencil__price}"


blue_pen = Pen(color="blue")
print(blue_pen.draw_picture())
print(blue_pen.sign_document())
red_pen = Pen(color="красный")
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
    __slots__ = ["color"]                               #

    def __init__(self, color="серый", model="Parker"):                  # constructor
        self.color = color
        self.__model = model

    def draw_picture(self):                             # method
        return f"Нарисован рисунок цветом '{self.color}'."


class Pen(Pencil):                                      # inheritance(inheritance)

    #__slots__ = ["color"]                              #

    def __init__(self, color, pen_type):                # constructor
        super().__init__(color=color)                   # method extension
        self.pen_type = pen_type                        # encapsulation - private attribute

    def sign_document(self):                            # method
        if self.color not in ("синий", "чёрный", "фиолетовый"):
            return f"Ручкой цвета '{self.color}' нельзя подписать документ."
        elif self.pen_type == "гелевая":
            return f"Ручкой типа '{self.pen_type}' нельзя подписать документ."
        return f"Подписан документ."


blue_ball_pen = Pen(color="синий", pen_type="шариковая")
print(blue_ball_pen.draw_picture())
print(blue_ball_pen.sign_document())
blue_gel_pen = Pen(color="синий", pen_type="гелевая")
print(blue_gel_pen.draw_picture())
print(blue_gel_pen.sign_document())
