
class MazeGame():
    def __init__(self, name = 'Chris "topher" Waldon', description = "Im a Rock!"):
        self.__name = name
        self.__description = description
        self.__map = map{}

    def map_builder(self):
        entrance = room()


class Room():
    def __init__(self):
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.description = ""
        self.items = []

name = input("Enter your name: ")
description = input("describe yourself: ")
