""" Point module """
from typing import Self

class Point:

    # Constructor with default values
    def __init__(self, new_x: int = 0, new_y: int = 0):
        self.__x = new_x
        self.__y = new_y

    # Pseudo default constructor
    def empty() -> Self:
        return Point(0, 0)
    
    # Pseudo XY constructor
    def from_xy(new_x: int, new_y: int):
        return Point(new_x, new_y)

    # Pseudo copy constructor
    def from_copy(p: Self) -> Self:
        temp = Point()
        temp.__x = p.__x
        temp.__y = p.__y
        return temp

    # Print point on console
    def show(self) -> None:
        print(f"X = {self.__x}; Y = {self.__y}")

