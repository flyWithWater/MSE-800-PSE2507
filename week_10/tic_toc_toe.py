"""
1. Design (Top-Down)
Plan the project structure with classes and functions
Each class should have clear methods

2. Implementation
Create a 3×3 board and display it.
Let two players take turns entering moves.
Detect winner or draw.
Use good OOP practices (encapsulation, methods, and attributes).

3. Testing
Run and debug the game using - manual testing
Handle invalid inputs.

4. Code Quality
Run Pylint:
Improve your score by fixing Pylint warnings and following Python style guidelines.
"""


"""
Tic Tac Toe Game
Classes:

1. Player class
    - Attributes: name, symbol
    - Methods: make_move()

2. Board class
    - Attributes: grid (3x3 list)
    - methods: is_game_finish(), get_result()

3. Game class:
    -attributes: player 1 , player 2, board, points
    -methods: start(); stop(); print_result(); print_points()


4. Main function to run the game
"""


from more_itertools import first


class Player:
    
    def __init__(self,name:str,mark_number:int):
        self._name = name
        self.mark_number = mark_number
    
    def make_move(self)->int:
        #ask the user to move
        next_move_str = input(f"{self._name},please enter your next step:")
        try:

            next_move = int(next_move_str)
            return next_move
        except Exception as e:
            self.make_move()
        
class Result:

    def __init__(self,winned_player:int,winned_result):
        self.winned_player = winned_player
        self.winned_result = winned_result


class Board:

    def __init__(self):
        self.board_array = int[3][3]

    def is_game_finish(self):
        """two conditions the game will be finish:
            1. a player winned the game;
            2. all the position was placed a piece.
        """
        sum(1 for )
    
    def is_someone_win(self)->Result:
        for index in range(0,len(self.board_array)):
            row = self.board_array[index]
            if len(set(row))==1:
                return Result(row[0],f"{index} row")
        
        for 




    def get_result(self):
        pass




        
