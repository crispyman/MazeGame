import random

class MazeGame():
    def __init__(self, name = 'Chris "topher" Waldon', description = "Im a Rock!"):
        self.__name = name
        self.__description = description
        #self.__map = map{}
        random.SystemRandom()

    def mapbuilder(self, number_of_rooms = 10):
        map_grid = [[0 for x in range(number_of_rooms)] for y in range(number_of_rooms)]
        location = [number_of_rooms - 1, number_of_rooms // 2]
        map_grid[location[0]][location[1]] = Room()
        for i in range(number_of_rooms):
            direction = random.randrange(3)
            if direction == 0:
                location[0] += 1
            elif direction == 1:
                location[0] -= 1
            elif direction == 2:
                location[1] += 1
            else:
                location[1] -= 1
            map_grid[location[0] % number_of_rooms][location[1] % number_of_rooms] = Room()
        # x = 0
        # y = 0
        # while x < len(map_grid):
        #     y = 0
        #     while y < len(map_grid[x]):
        #         if map_grid[x][y] != 1:
        #             y += 1
        #             continue
        #         map_grid[x][y] = Room()
        #         print(str(y) + " " + str(x))
        #         y += 1
        #     x += 1
        #
        x = 0
        y = 0
        while x < len(map_grid):
            y = 0
            while y < len(map_grid[x]):
                if map_grid[x][y] == 0:
                    y += 1
                    continue
                if type(map_grid[x][(y+1) % number_of_rooms]) == type(Room):
                    map_grid[x][y].north = map_grid[x][(y+1) % number_of_rooms]

                if type(map_grid[x][(y-1) % number_of_rooms]) == type(Room):
                    map_grid[x][y].south = map_grid[x][(y-1) % number_of_rooms]

                if type(map_grid[(x+1) % number_of_rooms][y]) == type(Room):
                    map_grid[x][y].east = map_grid[(x+1) % number_of_rooms][y]

                if type(map_grid[(x-1) % number_of_rooms][y]) == type(Room):
                    map_grid[x][y].west = map_grid[(x-1) % number_of_rooms][y]

                y += 1
            x += 1
        for x in map_grid:
            for y in x:
                print(type(y) == type(Room()), end=" ")
            print()
        print(map_grid)
        return map_grid[location[0] % number_of_rooms][location[1] % number_of_rooms]

class Room():
    def __init__(self):
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.description = ""
        self.items = []
    def set_north(self, connected_room):
        if self.north != connected_room:
            self.north = connected_room
            connected_room.set_south(self)

    def set_south(self, connected_room):
        if self.south != connected_room:
            self.south = connected_room
            connected_room.set_north(self)

    def set_east(self, connected_room):
        if self.east != connected_room:
            self.east = connected_room
            connected_room.set_west(self)

    def set_west(self, connected_room):
        if self.west != connected_room:
            self.west = connected_room
            connected_room.set_east(self)
    def set_random(self):
        direction = random.randrange(4)


name = input("Enter your name: ")
description = input("describe yourself: ")
x = MazeGame()
map = x.mapbuilder(40)
