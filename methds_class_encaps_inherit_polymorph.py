class Pencil:                                           # Class created
    type = "hi-tech"                                    # attribute

    def __init__(self, color="серый", model="Parker"):  # constructor
        self.color = color                              # attribute
        self.__model = model                            # encapsulation - private attribute
        self.price = "free"                             # attribute

    def draw_picture(self):                             # method
        return f"Нарисован рисунок цветом '{self.color}'."

    def __str__(self):                                  # polymorphism_1.1
        return f"The pencil, {self.__model}; {self.price}, {Pencil.type}"


class Pen(Pencil):                                      # inheritance(inheritance)

    def sign_document(self):                            # method
        if self.color not in ("синий", "чёрный", "фиолетовый"):
            return f"Ручкой цвета '{self.color}' нельзя подписать документ."
        return f"Подписан документ."

    def __str__(self):                                  # polymorphism_1.2
        return f"The pen, {self._Pencil__model}; {self.price}"


# new_pen = pencil("green", "Parker")                    # TypeError
blue_pen = Pen(color="синий")
print(blue_pen.draw_picture())
print(blue_pen.sign_document())
red_pen = Pen(color="красный")
print(red_pen.draw_picture())
print(red_pen.sign_document())
print(red_pen)                                          # The pen, Parker; free
pencil = Pencil("black")
print(pencil)                                           # The pencil, Parker; free, hi-tech


class Pencil:
    __slots__ = ["color"]                               #

    def __init__(self, color="серый"):                  # constructor
        self.color = color

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
