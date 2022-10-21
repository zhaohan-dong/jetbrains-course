class rectangle:
    def __init__(self, **kwargs):
        self._width = kwargs["width"]
        self._height = kwargs["height"]

    def Width(self):
        return self._width

    def Height(self):
        return self._height

    def SetWidth(self, width):
        self._width = width

    def SetHeight(self, height):
        self._height = height

    def area(self):
        return self._width * self._height

newRectangle = rectangle(width=12, height=10)
newRectangle.SetWidth(14)
print(newRectangle.Width())