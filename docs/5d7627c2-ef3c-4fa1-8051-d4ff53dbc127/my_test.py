class Triangle:
    
    def __init__(a, b, c):
        self._validate_triangle(a, b, c)
        self.a = a
        self.b = b
        self.c = c
    
    def _validate_triangle(a, b, c):
        if sum(a, b) < c or sum(b, c) < a or sum(c, a) < b:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')
            
        
    def _check_value(value):
        if not ((type(value) is int or type(value) is float) and value > 0):
            raise TypeError('стороны треугольника должны быть положительными числами')
    
    @property
    def a(self, a):
        self._check(a)
        self._a = a
        
    @property
    def b(self, b):
        self._check(b)
        self._b = b
    
    @property
    def c(self, c):
        self._check(c)
        self._c = c


def validate_triangle(value_triangle: tuple):
        try:
            Triangle(*value_triangle)
        except Exception:
            print("Value Error")
        return Triangle(*value_triangle)
        
input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]  # эту строчку не менять (переменную input_data также не менять)

lst_tr = list(map(validate_triangle, input_data))
print(lst_tr)
