# object.__init__(self[, ...])
# Called after the instance has been created (by __new__()), but before it is returned to the caller.
# The arguments are those passed to the class constructor expression.
# If a base class has an __init__() method, the derived class’s __init__() method, if any,
# must explicitly call it to ensure proper initialization of the base class part of the instance;
# for example: super().__init__([args...]).
# Because __new__() and __init__() work together
# in constructing objects (__new__() to create it, and __init__() to customize it),
# no non-None value may be returned by __init__(); doing so will cause a TypeError to be raised at runtime.

# object.__repr__(self)
# Called by the repr() built-in function to compute the “official” string representation of an object.
# If at all possible, this should look like a valid Python expression that could be used to recreate
# an object with the same value (given an appropriate environment).
# If this is not possible, a string of the form <...some useful description...> should be returned.
# The return value must be a string object.
# If a class defines __repr__() but not __str__(), then __repr__() is also used when
# an “informal” string representation of instances of that class is required.
# This is typically used for debugging,
# so it is important that the representation is information-rich and unambiguous.

# object.__str__(self)
# Called by str(object) and the built-in functions format() and print() to compute the “informal”
# or nicely printable string representation of an object. The return value must be a string object.
# This method differs from object.__repr__() in that there is no expectation that __str__() return
# a valid Python expression: a more convenient or concise representation can be used.
# The default implementation defined by the built-in type object calls object.__repr__().
class Hui:
    lenght = 0
    colour = ""

    def __init__(self, lenght=0, colour=""):
        self.lenght = lenght
        self.colour = colour

    def __del__(self):
        print("Destructor called")

    def pokazhi_huy_speredi(self):
        return self.lenght, self.colour

    def pokazhi_huy_sboku(self):
        return f"Vot huec: {self.lenght} {self.colour}"

    def pokazhi_huy_eshe_raz(self):
        return f"{self.lenght} {self.colour}"

    def __repr__(self):
        return f"{self.lenght} {self.colour}"

    def __str__(self):
        return f"Vot huec: {self.lenght} {self.colour}"


if __name__ == "__main__":
    import methds_class_init_str_repr
    huy1 = Hui(20, "black")
    print(huy1)
    # Vot huec: 20 black
    print(Hui.lenght)
    # 0
    Hui.lenght = 10
    print(Hui.lenght)
    # 10
    print(huy1.pokazhi_huy_speredi())
    # return representation of object as tuple
    # (20, 'black')
    print(huy1.pokazhi_huy_speredi()[0], huy1.pokazhi_huy_speredi()[1])
    # return representation of object as [formal]string with author's method - from tuple
    # 20 black
    print(huy1.pokazhi_huy_eshe_raz())
    # return representation of object as [formal]string with author's method
    # 20 black
    print(repr(huy1))
    # return representation of object as [formal]string with __repr__ method
    # 20 black
    print(huy1.pokazhi_huy_sboku())
    # return representation of object as [informal]string with author's method
    # Vot huec: 20 black
    print(huy1)
    # return representation of object as [informal]string with __str__ method
    # Vot huec: 20 black
