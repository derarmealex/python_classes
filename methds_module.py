print(sorted(globals().keys()))
# ['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

import class_
print(class_.f3.func())            # 1995, La Haine, black&white, director: Mathieu Kassovitz, actors: ...

import class_ as cs
print(cs)                          # <module 'clss' from 'C:\\Users\\alexa\\Desktop\\.py\\python_tools\\clss.py'>
print(cs.f3.func())                # 1995, La Haine, black&white, director: Mathieu Kassovitz, actors: ...
# or
import inspect
print(inspect.getmodule(cs))       # <module 'class_' from 'C:\\Users\\alexa\\Desktop\\py\\python_tools\\class2.py'>

from class_ import f1
print(f1.func())                   # 1968, Baisers volés, colour, director: François Truffaut, actors: ...
#print(class_.f1.func())            # NameError
#print(f3.func())                   # NameError

print(cs.__name__)                  # class_
print(cs.__doc__)                   # None
print(dir(cs))                      # ['Movies', '__builtins__', '__cached__', '_ ...
print(sorted(cs.__dict__.keys()))   # ['Movies', '__builtins__', '__cached__', '_ ...
help(cs)                            # Help on module clss: NAME clss CLASSES builtins.object Movies ...
