import unittest

class Testing(unittest.TestCase):
    pass

tests=Testing()


for atribute in dir(tests):
        if atribute.startswith('_'):
            continue
        print(atribute)