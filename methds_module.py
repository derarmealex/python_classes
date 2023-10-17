import methds_class
# SIMPLE
angel_mikhail = methds_class.Angels()
angel_mikhail.name = "Mikhail"
angel_mikhail.age = 999
# or
#angel_mikhail = methds_class.Angels("Mikhail", 999) # TypeError
angel_mikhail.brother = "Gavriil"
print(angel_mikhail.name)               # Mikhail
print(angel_mikhail.age)                # 999
print(angel_mikhail.brother)            # Gavriil

demon_azatoth = methds_class.Daemons()
demon_azatoth.name = "Azatoth"
#demon_azatoth.age = 9999
print(demon_azatoth.name)               # Azatoth
print(demon_azatoth.age)                # 500

#print(angel_gavriil.name)               # NameError
angel_ariel = methds_class.Angels()
print(angel_ariel.name)                 # Spirith
print(angel_ariel.age)                  # 500

print(angel_mikhail)                    # Wish I had an angel Mikhail
print(demon_azatoth)                    # Wish I had a daemon Azatoth
# CONSTRUCTOR
angel_mikhail = methds_class.Angels2()
angel_mikhail.name = "Mikhail"
angel_mikhail.age = 999
# or
angel_mikhail = methds_class.Angels2("Mikhail", 999)

#angel_mikhail.brother = "Gavriil"
print(angel_mikhail)                    # <methds_class.Angels2 object at 0x000001FCBB53CB90>
print(angel_mikhail.name)               # Mikhail
print(angel_mikhail.age)                # 999

demon_azatoth = methds_class.Daemons2()
demon_azatoth.name = "Azatoth"
#demon_azatoth.age = 9999
# or
demon_azatoth = methds_class.Daemons2("Azatoth")
print(demon_azatoth.name)               # Azatoth
print(demon_azatoth.age)                # 500

#print(angel_gavriil.name)               # NameError
angel_ariel = methds_class.Angels2()
print(angel_ariel.name)                 # Spirith
print(angel_ariel.age)                  # 500


print(sorted(globals().keys()))
# ['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__' ...]
import methds_class as cs
print(cs.__name__)                  # methds_class
print(cs.__doc__)                   # None
print(dir(cs))                      # ['A', 'Angels', 'Car', 'Daemons', 'ElectricCar', 'Movies', '__builtins__', '__cached__' ...
print(sorted(cs.__dict__.keys()))   # ['A', 'Angels', 'Car', 'Daemons', 'ElectricCar', 'Movies', '__builtins__', '__cached__' ...
#help(cs)                            # Help on module clss: NAME clss CLASSES builtins.object Movies ...
print(cs)                           # <module 'methds_class' from 'C:\\Users\\alexa\\Desktop\\py\\python_object_prog\\methds_class.py'>
# or
import inspect
print(inspect.getmodule(cs))        # <module 'methds_class' from 'C:\\Users\\alexa\\Desktop\\py\\python_object_prog\\methds_class.py'>
