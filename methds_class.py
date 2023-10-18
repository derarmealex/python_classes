# Методы для операций сравнения:
#    __lt__(self, other) — <;
#    __le__(self, other) — <=;
#    __eq__(self, other) — ==;
#    __ne__(self, other) — !=;
#    __gt__(self, other) — >;
#    __ge__(self, other) — >=.

# Метод __call__(arg1, arg2, ...) вызывается, когда сам объект вызывается как функция с аргументами.

# Методы для работы с объектом как с коллекцией:
#    __getitem__(self, key) используется для получения элемента коллекции по ключу self[key];
#    __setitem__(self, key, value) используется для записи значения по ключу self[key] = value;
#    __delitem__(self, key) используется для удаления ключа и соответствующего ему значения;
#    __len__(self) вызывается стандартной функцией len;
#    __contains__(self, item) вызывается при проверке принадлежности значения item объекту-коллекции self с помощью оператора in.

# Математические операции:
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
class Angels:
    name = "Spirith"
    age = 500

    def __str__(self):
        return f"Wish I had an angel {self.name}"

    def __del__(self):
        print("Destructor called")


class Daemons(Angels):
    def __str__(self):
        return f"Wish I had a daemon {self.name}"


class Angels2:
    def __init__(self, name="Spirith", age=500):
        self.name = name
        self.age = age

    def __del__(self):
        print("Destructor called")


class Daemons2(Angels2):
    pass


if __name__ == "__main__":
    import methds_class
# SIMPLE
    angel_mikhail = methds_class.Angels()
    angel_mikhail.name = "Mikhail"
    angel_mikhail.age = 999
# or
    #angel_mikhail = methds_class.Angels("Mikhail", 999) # TypeError (no __init__)
    angel_mikhail.brother = "Gavriil"
    print(angel_mikhail.name)                       # Mikhail
    print(angel_mikhail.age)                        # 999
    print(angel_mikhail.brother)                    # Gavriil

    demon_azatoth = methds_class.Daemons()
    demon_azatoth.name = "Azatoth"
    #demon_azatoth.age = 9999
    print(demon_azatoth.name)                       # Azatoth
    print(demon_azatoth.age)                        # 500

    #print(angel_gavriil.name)                       # NameError
    angel_ariel = methds_class.Angels()
    print(angel_ariel.name)                         # Spirith
    print(angel_ariel.age)                          # 500

    print(angel_mikhail)                            # Wish I had an angel Mikhail
    print(demon_azatoth)                            # Wish I had a daemon Azatoth
# CONSTRUCTOR
    angel_mikhail = methds_class.Angels2()
    angel_mikhail.name = "Mikhail"
    angel_mikhail.age = 999
# or
    angel_mikhail = methds_class.Angels2("Mikhail", 999)

    angel_mikhail.brother = "Gavriil"
    print(angel_mikhail)                            # <methds_class.Angels2 object at 0x000001FCBB53CB90>
    print(angel_mikhail.name)                       # Mikhail
    print(angel_mikhail.age)                        # 999

    demon_azatoth = methds_class.Daemons2()
    demon_azatoth.name = "Azatoth"
    #demon_azatoth.age = 9999
# or
    demon_azatoth = methds_class.Daemons2("Azatoth")
    print(demon_azatoth.name)                       # Azatoth
    print(demon_azatoth.age)                        # 500

    #print(angel_gavriil.name)                       # NameError
    angel_ariel = methds_class.Angels2()
    print(angel_ariel.name)                         # Spirith
    print(angel_ariel.age)                          # 500
    print(angel_ariel)                              # <methds_class.Angels2 object at 0x000002E5543325A0>
    #del angel_ariel
    #print(angel_ariel)                              # NameError
    #del angel_ariel
    #print(angel_ariel)                              # NameError
    print(Angels2)                                  # <class '__main__.Angels2'>
    #del Angels2
    #print(Angels2)                                  # NameError


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


if __name__ == "__main__":
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


if __name__ == "__main__":
    a = A()
    print(a + 1)
    print(1 + a)
    a += 1
    print(a)
