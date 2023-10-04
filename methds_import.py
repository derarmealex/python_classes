# import <library>
# import <library> as <alias>
# from <library> import *
# from <library> import <object>
# from <library> import <object> as <alias>

# print(library.__name__)
# print(library.__doc__)
# print(sorted(library.__dict__.keys()))
# print(dir(library))
# help(library)

import getpass
print(getpass.getuser())                        #

import math
#print(pi)                                       # NameError
print(math.pi)                                  # 3.141592653589793
print(math.modf(math.pi))                       # (0.14159265358979312, 3.0)
print(int(math.modf(math.pi)[-1]))              # 3
print(int(math.modf(math.pi)[0]))               # 0
print(round(math.modf(math.pi)[0], 2))          # 0.14

print('%.2f, %i' % math.modf(math.pi))          # 0.14, 3
print(math.floor(4.5))                          # 4
print(math.ceil(4.5))                           # 5
x = 2, 2
print(math.prod(x))                             # 4
print(math.sqrt(25))                            # 5.0

from math import *
print(pi)                                       # 3.141592653589793
print(math.pi)                                  # 3.141592653589793

import inspect
print(inspect.getmodule(math.modf))             # <module 'math' (built-in)>
print(inspect.getmodule(math))                  # <module 'math' (built-in)>
print(inspect.getmodule(math.pi))               # None

import os
os.system('cls')                                                           # clear console
print(os.name)                                                             # nt
print(os.cpu_count())                                                      # 4
print(os.path.isabs('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))    # True/False
print(os.path.isfile('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))   # True/False
print(os.path.isdir('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))    # True/False
print(os.path.islink('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))   # True/False
print(os.path.exists('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))   # True/False
print(os.path.lexists('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))  # True/False
print(os.path.basename('E:\music\Various Artists\Bob Kerrey-The Band Played Waltzing Matilda.mp3'))
                                                # Bob Kerrey-The Band Played Waltzing Matilda.mp3
print(os.path.getsize('E:\music\Various Artists\Bob Kerrey-The Band Played Waltzing Matilda.mp3'))
                                                # 4657964 [bytes]
print(os.listdir('E:\music\playlist'))          # ['AaRON - Birds in the Storm.flac', ...
for data in os.environ: print(os.environ[data]) # ...

import os.path, time
print("This file    : %s" % __file__)
print("Last modified: %s" % time.ctime(os.path.getmtime("../python_tools/.gitignore")))
print("Created      : %s" % time.ctime(os.path.getctime("../python_tools/.gitignore")))
print("Access time  : %s" % time.ctime(os.path.getatime("../python_tools/.gitignore")))
# This file    : C:\Users\alexa\Desktop\py\python_syntax\draft1_syntax.py
# Last modified: Fri Sep 15 13:46:48 2023
# Created      : Wed Sep 13 14:38:01 2023
# Access time  : Sun Sep 17 17:43:23 2023

import platform
print(platform.python_version())                # 3.11.5
print(platform.system())                        # Windows
print(platform.release())                       # 10
print(platform.machine())                       # AMD64
print(platform.architecture())                  # ('64bit', 'WindowsPE')
print(platform.architecture()[0])               # 64bit

import struct
print(struct.calcsize("P") * 8)                 # 64

import site
print(site.getsitepackages())                   # ['C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.11 ...

import socket
print(socket.gethostname())                     # DESKTOP-TD4SVJM
print(socket.gethostbyname('DESKTOP-TD4SVJM'))  # 10.0.0.1

addr = '127.0.0.2561'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")

import sys
print(sys.version)                              # 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)]
print(sys.platform)                             # win32
print(sys.copyright)                            # Python Copyright Information...
print(copyright)                                # -//-
print(sys.byteorder)                            # little/big
print(sys.builtin_module_names)                 # ('_abc', '_ast', '_bisect', '_blake2', '_codecs' ...
print(sys.getsizeof())                          # ... bytes
print(sys.getrecursionlimit())                  # 1000
#sys.setrecursionlimit(1001)                     # 1001
