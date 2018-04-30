import random
import descriptions

class MazeGame():
    def __init__(self, name = 'Chris "topher" Waldon', description = "Im a Rock!"):
        self.__name = name
        self.__description = description
        self.__inventory = {"items": [], "weapons": []}
        self.__player_location = None
        self.__start = None
        self.__exit = None
        # self.__descriptions = ""
        #self.__map = map{}
        #random.SystemRandom()

    def game(self, number_of_rooms = 10):
        cheat = False
        self.initalizemap(number_of_rooms)
        while not self.__player_location.exit:
            print(self.__player_location.description)
            if self.__player_location.attributes[0] == "action":
                print("you can do action: " + self.__player_location.attributes[1])

            elif self.__player_location.attributes[0] == "event":
                if self.__player_location.attributes[1] == "enemy":
                    enemy = self.__player_location.attributes[2][random.randrange[len(self.__player_location.attributes[2])]]
                    print("you see a {} rapidly approaching you.".format(enemy))
                    if len(self.__inventory["weapons"]) != 0:
                        print ("you attack it with {} and destroy it".format(self.__inventory["weapons"][random.randrange[len(self.__inventory["weapons"])]]))
                    elif "Holy Bible" in self.__inventory["items"]:
                        print("The {} attempts to approach you but when it gets close it appears to start smoking before retreating out of sight.".format(enemy))
                    elif "necronomicon" in self.__inventory["items"]:
                        print("The {} walks right past you without slowing down.".format(self.__player_location.attributes[2]))
                    else:
                        print("you have no weapon handy, you wish you had picked something up as the {} slowly tears you apart.".format(enemy))
                        exit(0)
            print("You can go:", end=" ")
            for x in self.__player_location.get_directions():
                print(x, end=" ")
            print()
            if not cheat:
                action: str = input("what do you want to do?")
            else:
                print("You go: " + action)

            if action == "HELP!" or cheat:
                print("fine!")
                cheat = True
                print(self.__player_location.get_directions())
                action = self.__player_location.get_directions()[
                         random.randrange(len(self.__player_location.get_directions()))][:1]

            if self.__player_location.attributes[0] == "action" and action.lower() == self.__player_location.attributes[1]:
                if self.__player_location.attributes[2] == "event":
                    if self.__player_location.attributes[3] == "death":
                        print("you slowly start to open the...")
                        exit(0)
                    else:
                        print(self.__player_location.attributes[3])
                elif self.__player_location.attributes[2] == "weapon":
                    w = self.__player_location.attributes[3][random.randrange(len(self.__player_location.attributes[3]))]
                    print("you find a {}".format(w))
                    self.__inventory["weapons"].append(w)
                elif self.__player_location.attributes[2] == "item":
                    i = self.__player_location.attributes[3][random.randrange(len(self.__player_location.attributes[3]))]
                    if i == "Holy Water":
                        print("you drink the {} and feel energized".format(i))
                    else:
                        print("you find a {}".format(i))
                    self.__inventory["items"].append(i)

            elif action.lower() == "move north" or action.lower() == "n":
                if self.__player_location.north is not None:
                    self.__player_location = self.__player_location.north
                else:
                    print("you walk into a wall, it hurts")

            elif action.lower() == "move south" or action.lower() == "s":
                if self.__player_location.south is not None:
                    self.__player_location = self.__player_location.south
                else:
                    print("you walk into a wall, it hurts")

            elif action.lower() == "move east" or action.lower() == "e":
                if self.__player_location.east is not None:
                    self.__player_location = self.__player_location.east
                else:
                    print("you walk into a wall, it hurts")

            elif action.lower() == "move west" or action.lower() == "w":
                if self.__player_location.west is not None:
                    self.__player_location = self.__player_location.west
                else:
                    print("you walk into a wall, it hurts")

            elif action.lower() == "restart":
                print("Hope you have better luck this time!")
                number_of_rooms *= 2
                self.initalizemap(number_of_rooms)

            elif action.lower() == "inventory":
                print(self.__inventory)

            else:
                print("while trying to figure out what to do, you keel over and die.")
                #exit(0)


        print(
            "You squint at the bright light as you enter the next room," +
            " then suddenly you realise your outdoors," +
            "you turn around only to see that your standing on a flat open plain next to a small town.")
        print("You are carying: " + str(self.__inventory["items"]) + " " + str(self.__inventory["weapons"]))
        exit(0)

    def initalizemap(self, number_of_rooms = 10):
        map_width = number_of_rooms // 2
        if number_of_rooms > len(descriptions.list):
            for m in range(number_of_rooms - len(descriptions.list)):
                descriptions.list.append(["You enter a large empty room with smooth stone walls", ["nothing"]])

        # https://codereview.stackexchange.com/questions/134647/creating-a-grid-to-the-specified-size-using-lists
        map_grid = [[0 for x in range(map_width)] for y in range(map_width)]
        location = [map_width - 1, map_width // 2]
        map_grid[location[0]][location[1]]: Room() = Room()

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
            map_grid[location[0] % map_width][location[1] % map_width] = Room()
            if i == number_of_rooms - 1:
                map_grid[location[0] % map_width][location[1] % map_width].exit = True
                map_grid[location[0] % map_width][location[1] % map_width].description = "The exit"
                map_grid[location[0] % map_width][location[1] % map_width].attributes = ["nothing"]

                # print(map_grid[location[0] % map_width][location[1] % map_width].exit)
            else:
                map_grid[location[0] % map_width][location[1] % map_width].description, map_grid[location[0] % map_width][location[1] % map_width].attributes = descriptions.list.pop(random.randrange(len(descriptions.list)))

        map_grid[map_width - 1][map_width // 2].description = "You wake up with a headache in a large room with stone walls, there is no apparent source of light"
        map_grid[map_width - 1][map_width // 2].attributes = ["action", "search", "item", ["Pen"]]
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
                if type(map_grid[x][(y+1) % map_width]) == type(Room()):
                    map_grid[x][y].north = map_grid[x][(y+1) % map_width]

                if type(map_grid[x][(y-1) % map_width]) == type(Room()):
                    map_grid[x][y].south = map_grid[x][(y-1) % map_width]

                if type(map_grid[(x+1) % map_width][y]) == type(Room()):
                    map_grid[x][y].east = map_grid[(x+1) % map_width][y]

                if type(map_grid[(x-1) % map_width][y]) == type(Room()):
                    map_grid[x][y].west = map_grid[(x-1) % map_width][y]

                y += 1
            x += 1
        # for x in map_grid:
            # for y in x:
                # print(type(y) == type(Room()), end=" ")
            # print()
        # print(map_grid)
        # print(map_grid[location[0] % map_width][location[1] % map_width])
        self.__start = map_grid[map_width - 1][ map_width // 2]
        self.__player_location = map_grid[map_width - 1][ map_width // 2]

class Room():
    def __init__(self):
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.description = ""
        self.attributes = []
        self.exit = False

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

    def get_directions(self):
        valid_directions = []
        if self.north is not None:
            valid_directions.append("North")
        if self.south is not None:
            valid_directions.append("South")
        if self.east is not None:
            valid_directions.append("East")
        if self.west is not None:
            valid_directions.append("West")
        return valid_directions


name = input("Enter your name: ")
description = input("describe yourself: ")
x = MazeGame()
x.game()
