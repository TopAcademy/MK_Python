""" Point module """

class Point:

    # Constructor
    def __init__(self, new_x: int, new_y: int):
        self._x = new_x
        self._y = new_y

    # Print point on console
    def show(self) -> None:
        print(f"X = {self._x}; Y = {self._y}")

