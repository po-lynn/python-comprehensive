class MyClass:
    def __init__(self, value):
        self._x = value

    def get_x(self):
        return self._x

    def set_x(self, value):
        if value < 0:
            raise ValueError("Value must be positive.")
        self._x = value

obj = MyClass(-2)
print(obj.get_x())    # Output: 2
obj.set_x(10)
print(obj.get_x())    # Output: 10
