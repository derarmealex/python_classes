# Метод __repr__ вызывается стандартной функцией repr и возвращает строку,
# которая является представлением объекта в формате инициализации.
# Этот метод может быть также полезен, если необходимо вывести информацию об объектах,
# когда они являются элементами коллекции.

#Методы для операций сравнения:
#    __lt__(self, other) — <;
#    __le__(self, other) — <=;
#    __eq__(self, other) — ==;
#    __ne__(self, other) — !=;
#    __gt__(self, other) — >;
#    __ge__(self, other) — >=.

#Метод __call__(arg1, arg2, ...) вызывается, когда сам объект вызывается как функция с аргументами.

#Методы для работы с объектом как с коллекцией:
#    __getitem__(self, key) используется для получения элемента коллекции по ключу self[key];
#    __setitem__(self, key, value) используется для записи значения по ключу self[key] = value;
#    __delitem__(self, key) используется для удаления ключа и соответствующего ему значения;
#    __len__(self) вызывается стандартной функцией len;
#    __contains__(self, item) вызывается при проверке принадлежности значения item объекту-коллекции self с помощью оператора in.

#Математические операции:
#    __add__(self, other) — self + other;
#    __sub__(self, other) — self - other;
#    __mul__(self, other) — self * other;
#    __matmul__(self, other) — self @ other;
#    __truediv__(self, other) — self / other;
#    __floordiv__(self, other) — self // other;
#    __mod__(self, other) — self % other;
#    __divmod__(self, other) — divmod(self, other);
#    __pow__(self, other) — self ** other;
#    __lshift__(self, other) — self << other;
#    __rshift__(self, other) — self >> other;
#    __and__(self, other) — self & other;
#    __xor__(self, other) — self ^ other;
#    __or__(self, other) — self | other;
#    __radd__(self, other) — other + self;
#    __rsub__(self, other) — other - self;
#    __rmul__(self, other) — other * self;
#    __rmatmul__(self, other) — other @ self;
#    __rtruediv__(self, other) — other / self;
#    __rfloordiv__(self, other) — other // self;
#    __rmod__(self, other) — other % self;
#    __rdivmod__(self, other) — divmod(other, self);
#    __rpow__(self, other) — other ** self;
#    __rlshift__(self, other) — other << self;
#    __rrshift__(self, other) — other >> self;
#    __rand__(self, other) — other & self;
#    __rxor__(self, other) — other ^ self;
#    __ror__(self, other) — other | self;
#    __iadd__(self, other) — self += other;
#    __isub__(self, other) — self -= other;
#    __imul__(self, other) — self *= other;
#    __imatmul__(self, other) — self @= other;
#    __itruediv__(self, other) — self /= other;
#    __ifloordiv__(self, other) — self //= other;
#    __imod__(self, other) — self %= other;
#    __ipow__(self, other) — self **= other;
#    __ilshift__(self, other) — self <<= other;
#    __irshift__(self, other) — self >>= other;
#    __iand__(self, other) — self &= other;
#    __ixor__(self, other) — self ^= other;
#    __ior__(self, other) — self |= other.


class Movies:
    """
    film library
    ...
    Attributes
    ----------
    name: str
        title of the movie
    year: int
        release year
    colour: str
        colour or black and white
    director: str
        director's name
    main_actor: str
        main actor's name
    main_actor2: str
        main actor's name
    main_actor3: str
        main actor's name
    ...
    Methods
    -------
    func():
        output referential info about the movie
    """
#    name = None
#    year = 0
#    colour = None
#    director = None
#    main_actor = None
#    main_actor2 = None
#    main_actor3 = None

#    __slots__ = ["name", "year", "colour", "director", "main_actor", "main_actor2", "main_actor3"]

    def __init__(self, name="-", year="-", colour="-", director="-", main_actor="-", main_actor2="-", main_actor3="-"):
        """
        set attributes for Movies
        ...
        Attributes
        ----------
        name: str
            title of the movie
        year: int
            release year
        colour: str
            colour or black and white
        director: str
            director's name
        main_actor: str
            main actor's name
        main_actor2: str
            main actor's name
        main_actor3: str
            main actor's name
        """
        self.colour = colour
        self.name = name
        self.__year = year
        self.director = director
        self.main_actor = main_actor
        self.main_actor2 = main_actor2
        self.main_actor3 = main_actor3

    def func(self):
        """
        flick
        ...
        output referential info about the movie
        if there's no more than one main actor, print '-' instead of the names
        """
        return f'{self.__year}, {self.name}, {self.colour}, director: {self.director}, actors: {self.main_actor}, {self.main_actor2}, {self.main_actor3}'

    def __repr__(self):
        return f'{self.__year}, {self.name}, {self.colour}, director: {self.director}, actors: {self.main_actor}, {self.main_actor2}, {self.main_actor3}'

f1 = Movies('Baisers volés', 1968, 'colour', 'François Truffaut', 'Jean-Pierre Léaud')
f2 = Movies('Het verloren paradijs', 1978, 'colour', 'Harry Kümel', 'Hugo Van Den Berghe', 'Willeke van Ammelrooy')
f3 = Movies('La Haine', 1995, 'black&white', 'Mathieu Kassovitz', 'Vincent Cassel', 'Saïd Taghmaoui', 'Hubert Kounde')

if __name__ == "__main__":

    Movies.main_actor4 = "-"                                        #
    print(Movies.main_actor4)                                       # -
#    f4 = Movies('La Haine', 1995, 'black&white', 'Mathieu Kassovitz', 'Vincent Cassel', 'Saïd Taghmaoui', 'Hubert Kounde', 'bibi')
# TypeError
    f3.main_actor3 = 'H. Koundé'
    f3.__year = 2000
# 1995, La Haine, black&white, director: Mathieu Kassovitz, actors: Vincent Cassel, Saïd Taghmaoui, H. Koundé
    f3._Movies__year = 2000
# 2000, La Haine, black&white, director: Mathieu Kassovitz, actors: Vincent Cassel, Saïd Taghmaoui, H. Koundé
    movie_copy = repr(f3)
    print(movie_copy)
# 2000, La Haine, black&white, director: Mathieu Kassovitz, actors: Vincent Cassel, Saïd Taghmaoui, H. Koundé
    print(f3.func())


class Pencil:

    def __init__(self, color="серый"):
        self.color = color

    def draw_picture(self):
        return f"Нарисован рисунок цветом '{self.color}'."


class Pen(Pencil):

    def sign_document(self):
        if self.color not in ("синий", "чёрный", "фиолетовый"):
            return f"Ручкой цвета '{self.color}' нельзя подписать документ."
        return f"Подписан документ."


blue_pen = Pen(color="синий")
print(blue_pen.draw_picture())
print(blue_pen.sign_document())
red_pen = Pen(color="красный")
print(red_pen.draw_picture())
print(red_pen.sign_document())


class Pencil:

    def __init__(self, color="серый"):
        self.color = color

    def draw_picture(self):
        return f"Нарисован рисунок цветом '{self.color}'."


class Pen(Pencil):

    def __init__(self, color, pen_type):
        super().__init__(color=color)
        self.pen_type = pen_type

    def sign_document(self):
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


class Car:

    def __init__(self, color, consumption, tank_volume, mileage=0):
        self.color = color
        self.consumption = consumption
        self.tank_volume = tank_volume
        self.reserve = tank_volume
        self.mileage = mileage
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return "Двигатель запущен."
        return "Двигатель уже был запущен."

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return "Двигатель остановлен."
        return "Двигатель уже был остановлен."

    def drive(self, distance):
        if not self.engine_on:
            return "Двигатель не запущен."
        if self.reserve / self.consumption * 100 < distance:
            return "Малый запас топлива."
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехали {distance} км. Остаток топлива: {self.reserve} л."

    def refuel(self):
        self.reserve = self.tank_volume

    def get_mileage(self):
        return self.mileage

    def get_reserve(self):
        return self.reserve

    def get_consumption(self):
        return self.consumption

    def __str__(self):
        return f"Электромобиль. " \
               f"Цвет: {self.color}. " \
               f"Пробег: {self.mileage} км. " \
               f"Остаток заряда: {self.reserve} кВт*ч."


class ElectricCar(Car):

    def __init__(self, color, consumption, bat_capacity, mileage=0):
        super().__init__(color, consumption, bat_capacity, mileage)
        self.bat_capacity = bat_capacity

    def drive(self, distance):
        if not self.engine_on:
            return "Двигатель не запущен."
        if self.reserve / self.consumption * 100 < distance:
            return "Малый запас заряда."
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехали {distance} км. Остаток заряда: {self.reserve} кВт*ч."

    def recharge(self):
        self.reserve = self.bat_capacity

    def __repr__(self):
        return f"ElectricCar('{self.color}', " \
               f"{self.consumption}, " \
               f"{self.bat_capacity}, " \
               f"{self.mileage})"
    def __add__(self, other):
        new_car = ElectricCar(self.color,
                              self.consumption + other.consumption,
                              self.bat_capacity + other.bat_capacity,
                              self.mileage + other.mileage)
        new_car.reserve = self.reserve + other.reserve
        return new_car


electric_car = ElectricCar(color="white", consumption=15, bat_capacity=90)
print(electric_car.start_engine())
print(electric_car.drive(100))
print(electric_car)
electric_car = ElectricCar(color="белый", consumption=15, bat_capacity=90)
print(electric_car)
print(repr(electric_car))
electric_car_1 = ElectricCar(color="чёрный", consumption=17, bat_capacity=80)
print([electric_car, electric_car_1])
electric_car.start_engine()
electric_car_1.start_engine()
electric_car.drive(300)
electric_car_1.drive(100)
new_electric_car = electric_car + electric_car_1
print(new_electric_car)


class A:

    def __init__(self):
        self.value = 10

    def __add__(self, other):
        return "Выполняется метод __add__."

    def __radd__(self, other):
        return "Выполняется метод __radd__."

    def __iadd__(self, other):
        self.value += other
        return self

    def __str__(self):
        return f"value: {self.value}."


a = A()
print(a + 1)
print(1 + a)
a += 1
print(a)
