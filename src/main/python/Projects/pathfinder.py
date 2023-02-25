# def create_grid(rows, columns):
#     return [[" " for column in range(columns)] for row in range(rows)]

class Grid:
    __slots__ = ["__rows" , "__columns"]

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns

    def __repr__(self):
        my_grid = self.create()
        output = ""

        for row in my_grid:
            output += str(row) + "\n"

        return output

    def get_rows(self): 
        return self.__rows

    def get_columns(self): 
        return self.__columns
    
    def create(self):
        return [[(row, column) for column in range(self.__columns)] for row in range(self.__rows)]

class findClosest:
    __slots__ = ["__grid", "__start_coord", "__final_coord", "__position"]

    def __init__(self, grid, start_coord, final_coord):
        self.__grid = grid
        self.__start_coord = start_coord
        self.__final_coord = final_coord
        self.__position = start_coord

    def pathfind(self):
        if self.__final_coord[0] > self.__grid.get_rows() or self.__final_coord[1] > self.__grid.get_columns():
            raise ValueError("ERROR: Final position out of grid bounds.")

        for _ in range(self.__start_coord[0]):
            self.__position[0] += 1
            print(self.__position)
            print(self.__position[0] == self.__final_coord[0])
            print(self.__position[1] == self.__final_coord[1])

        if self.__position[0] == self.__final_coord[0] and self.__position[1] == self.__final_coord[1]:
            new_position = (self.__position[0], self.__position[1])
            return "Done! New position:", new_position

def main():
    my_grid = Grid(10, 10)
    print(my_grid)
    pathfinder = findClosest(my_grid, (0, 0), (8, 0)).pathfind()



if __name__ == "__main__":
    main()