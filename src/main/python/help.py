def retuple():
    return [[0 for rows in range(3)] for columns in range(3)]

def idk():
    d2 = board_values = [[" " for rows in range(3)] for columns in range(3)]
    available_cells = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
    available_cells[board_values[0]].pop(board_values[1])
    print(available_cells)

# print(idk())

# print(ord("a"))
my_str = "abcd"
print(my_str[len(my_str) - 2])