print(sorted(globals().keys()))
# ['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__' ...]
import methds_class as cs
print(cs.__name__)                  # methds_class
print(cs.__doc__)                   # None
print(dir(cs))                      # ['A', 'Angels', 'Angels2', 'Car', 'Daemons', 'Daemons2', 'ElectricCar', '__builtins__', ... ]
print(sorted(cs.__dict__.keys()))   # ['A', 'Angels', 'Angels2', 'Car', 'Daemons', 'Daemons2', 'ElectricCar', '__builtins__', ... ]
#help(cs)                            # Help on module methds_class:NAME methds_class CLASSES builtins.object A Angels Daemons ...
print(cs)                           # <module 'methds_class' from 'C:\\Users\\alexa\\Desktop\\py\\python_object_prog\\methds_class.py'>
# or
import inspect
print(inspect.getmodule(cs))        # <module 'methds_class' from 'C:\\Users\\alexa\\Desktop\\py\\python_object_prog\\methds_class.py'>
