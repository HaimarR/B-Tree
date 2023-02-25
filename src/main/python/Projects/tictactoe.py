import random

class TicTacToe(object):

#BOARD UPDATERS START
    def clear_board(self):
        """
        WHAT DOES IT DO:
        - Resets board
        - Board values are deleted/reset
        - Turns go back to 0
        - Available cells are reset so every board cell is available/empty

        WHEN IS IT CALLED:
        - Called in the beginning of every game
        """
        board_values = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        turn_sum = 0
        available_cells = list(range(9))

        return board_values, turn_sum, available_cells

    def update_board(self, gamemode, board_values, position, turn="user", turn_sum=0, available_cells=list(range(9))):
        """
        WHAT DOES IT DO:
        - Updates board
        - Given a new position choosen by either the player or the AI,
          it adds the new position to board_values<list>(User:X, AI:O), turns go up by 1
          and removes that position from available_cells<list>
        - If the position given is not in available_cells<list>, the user is prompted to enter a new position
        - Board values are updated to return the new board information
        WHEN IS IT CALLED:
        - Called after the user or the AI choose a position
        """
        position_int = int(position)

        if board_values[position_int] == " ":
            if turn == "user":
                board_values[position_int] = "X"
                turn_sum += 1
            elif turn == "ai":
                board_values[position_int] = "O"   
            available_cells.remove(position_int)
        else:
            print("ERROR: That position has already been taken, please choose another position")
            self.game(gamemode, board_values)

        return board_values, available_cells, turn_sum

    def print_board(self, board_values : list, turn_sum):
        """
        WHAT DOES IT DO:
        - Prints updated board
        - Given board_values<list> and turn_sum<int>, the function prints the game info
          and the board values
        - Each board_value will be printed in its cell
        - Board values are updated to return the new board information
        WHEN IS IT CALLED:
        - Called after each time update_board is called
        """
        print()

        print("_________________")
        print("GAME INFO:")
        print("  - Turn: ", turn_sum)
        #more future game info goes here
        print("_________________")

        print()

        print("/////////////////")
        print()
        print("Current board:")
        print()
        x = 0
        while x < 9:

            print("     |     |     ") #Row 1
            print("", board_values[x], "|", board_values[x+1], "|", board_values[x+2], sep="  ") #Row 2

            if x < 6:
                print("_____|_____|_____") #Row 3
            else:
                print("     |     |     ")

            x += 3

        print()
        print("/////////////////")
        print()

    def choose_position(self, board_values : list, available_cells : list, gamemode : str):
        gamemode = gamemode.lower()
        if gamemode == "easy":
            new_position = available_cells[random.randint(0, len(available_cells) - 1)]
        elif gamemode == "medium":
            if 4 in available_cells:
                new_position = 4
            else:
                o_indexes = self.get_indexes(board_values, "O")
                taken_rows = self.row_count(o_indexes)

                for row in taken_rows:
                    if row!=0:
                        return ''
        
            return new_position
#BOARD UPDATERS END

#GAME CHECKERS START
    def game_in_progress(self, available_cells):
        """
        WHAT DOES IT DO:
        - Checks if game is in progress
        - Given available_cells<list>, the function returns False if there's no available cells,
          returns True otherwise
        WHEN IS IT CALLED:
        - Called before every turn
        """
        if available_cells == []:
            return False

        return True

    def get_indexes(self, board_values : list, letter : str="X"):
        value_indexes = []
        
        for index in range(len(board_values)):
            if board_values[index] == letter:
                value_indexes.append(index)

        return value_indexes

    def row_count(self, value_indexes : list):
        """
        WHAT DOES IT DO:
        - Returns how many same-team-values(User:X, AI:O) are in a row
        - 
        WHEN IS IT CALLED:
        - 
        """
        row0_count = 0
        row1_count = 0
        row2_count = 0

        for index in range(len(value_indexes)):
            row = value_indexes[index] // 3
            
            if row == 0:
                row0_count += 1
            elif row == 1:
                row1_count += 1
            elif row == 2:
                row2_count += 1

        return row0_count, row1_count, row2_count

    def column_count(self, value_indexes : list):
        col0_count = 0
        col1_count = 0
        col2_count = 0

        for index in range(len(value_indexes)):
            col = value_indexes[index] % 3
            
            if col == 0:
                col0_count += 1
            elif col == 1:
                col1_count += 1
            elif col == 2:
                col2_count += 1

        return col0_count, col1_count, col2_count

    def diagonal_count(self, value_indexes : list):
        diagonal_right_count = 0  #Diagonal that goes from left to right (0,4,8)
        diagonal_left_count = 0   #Diagonal that goes from right to left (2,4,6)
        if 4 not in value_indexes:
            return diagonal_right_count, diagonal_left_count
        else:
            value_indexes.remove(4)
            diagonal_right_count += 1
            diagonal_left_count += 1
            for index in range(len(value_indexes)):
                
                diagonal = value_indexes[index] % 4
                
                if diagonal == 0:
                    diagonal_right_count += 1
                elif diagonal == 2:
                    diagonal_left_count += 1

            return diagonal_right_count, diagonal_left_count

    def check_horizontal_win(self, board_values : list):
        x_indexes = self.get_indexes(board_values, "X")

        row1, row2, row3 = self.row_count(x_indexes)
        if row1 == 3 or row2 == 3 or row3 == 3:
            return True

        return False

    def check_vertical_win(self, board_values : list):
        x_indexes = self.get_indexes(board_values, "X")

        col1, col2, col3 = self.column_count(x_indexes)
        if col1 == 3 or col2 == 3 or col3 == 3:
            return True

        return False

    def check_diagonal_win(self, board_values : list):
        x_indexes = self.get_indexes(board_values, "X")

        diag1, diag2 = self.diagonal_count(x_indexes)
        if diag1 == 3 or diag2 == 3:
            return True
        return False

    def check_horizontal_loss(self, board_values : list):
        o_indexes = self.get_indexes(board_values, "O")

        row1, row2, row3 = self.row_count(o_indexes)
        if row1 == 3 or row2 == 3 or row3 == 3:
            return True

        return False

    def check_vertical_loss(self, board_values : list):
        o_indexes = self.get_indexes(board_values, "O")

        col1, col2, col3 = self.row_count(o_indexes)
        if col1 == 3 or col2 == 3 or col3 == 3:
            return True

        return False

    def check_diagonal_loss(self, board_values : list):
        o_indexes = self.get_indexes(board_values, "O")

        diag1, diag2 = self.diagonal_count(o_indexes)
        if diag1 == 3 or diag2 == 3:
            return True
        return False
#GAME CHECKERS END

#MAIN GAME FUNCTIONS START
    def game(self, gamemode, board_values, turn_sum=0, available_cells=list(range(9))):

        while True:
            if self.game_in_progress(available_cells):
                #user's turn
                new_position = input("Choose new position (0-8): ")
                
                
                output_tuple = self.update_board(gamemode, board_values, new_position, "user", turn_sum, available_cells)
                new_board = output_tuple[0]
                available_cells = output_tuple[1]
                turn_sum = output_tuple[2]
                self.print_board(new_board, turn_sum)

                if self.check_horizontal_win(new_board) or self.check_vertical_win(new_board) or self.check_diagonal_win(new_board):
                    print("Congratultions! You have won!")
                    return "Win"
            else:
                self.print_board(new_board, turn_sum)
                print("Tie!")
                return "Tie"

            if self.game_in_progress(available_cells):
                new_position = self.choose_position(board_values, available_cells, gamemode)

                output_tuple = self.update_board(gamemode, board_values, new_position, "ai", turn_sum, available_cells)
                new_board = output_tuple[0]
                available_cells = output_tuple[1]
                turn_sum = output_tuple[2]

                if self.check_horizontal_loss(new_board) or self.check_vertical_loss(new_board) or self.check_diagonal_loss(new_board):
                    self.print_board(new_board, turn_sum)
                    print("Sorry, you lost.")
                    return "Loss"
                
                
            else:
                self.print_board(new_board, turn_sum)
                print("Tie!")
                return "Tie"
            
            self.print_board(new_board, turn_sum)

            o_indexes = self.get_indexes(board_values, "O")
            taken_rows = list(self.row_count(o_indexes))
            print(taken_rows)
    def runner(self, wins=0, losses=0, ties=0):
        gamemode = input("Choose your gamemode (easy/medium/hard/impossible): ")
        gamemode = gamemode.lower()
        print(wins, losses)
        clear_board_tuple = self.clear_board()
        board_values = clear_board_tuple[0]
        turn_sum = clear_board_tuple[1]
        available_cells = clear_board_tuple[2]

        self.print_board(board_values, turn_sum)

        game_result = self.game(gamemode, board_values, turn_sum, available_cells)
        if game_result == "Win":
            wins += 1
        elif game_result == "Loss":
            losses += 1
        elif game_result == "Tie":
            ties += 1
            
        print("Score:", wins, "-", losses)

        play_again = input("Play again? (Y/N): ")
        if play_again.upper() != "Y":
            return wins, losses, ties #if player doesn't waant to play again, it returns the wins and losses
        self.clear_board()
        return self.runner(wins, losses)
#MAIN GAME FUNCTIONS END     

#MAIN CALLER FUNCTION
    def main(self):
        
        game_stats = self.runner()
        print("_________________")
        print("Session stats: ")
        print("Games played:", game_stats[0] + game_stats[1])
        print("Wins:", game_stats[0])
        print("Losses:", game_stats[1])
        print("Ties:", game_stats[2])
        #add more session stats here
        print("_________________")

if __name__ == "__main__":
    TicTacToe().main()