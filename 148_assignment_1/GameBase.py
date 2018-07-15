from typing import Any
from current_state import SubtractSquareState, ChopsticksState


class Game:
    """
    A game superclass containing several foundimental game attributes.
    """
    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize the Game, store the boolean value is_p1_turn.

        >>> a = Game(True)
        >>> a.p1_turn
        True
        """
        self.p1_turn = is_p1_turn

    def __str__(self) -> str:
        """
        Return the name of the game.

        >>> a = Game(True)
        >>> print(a)
        Game
        player 1 moves first: True
        """
        return type(self).__name__ + '\n' + \
               'player 1 moves first: {}'.format(self.p1_turn)

    def __eq__(self, other: Any) -> bool:
        """
        Return whethre the two states are equal

        >>> a = Game(True)
        >>> b = Game(False)
        >>> a == b
        False
        """
        return str(self) == str(other)

    def get_instructions(self) -> str:
        """
        Return the instruction of the game.

        >>> a = Game(True)
        >>> a.get_instructions()
        builtins.NotImplementedError: must implement a subclass!
        """
        raise NotImplementedError('must implement a subclass!')

    def is_over(self, current_state: Any) -> bool:
        """
        Return whether the current_state of the game is over.

        >>> a = Game(True)
        >>> a.is_over('I dont know')
        builtins.NotImplementedError: must implement a subclass!
        """
        raise NotImplementedError('must implement a subclass!')

    def is_winner(self, player: str) -> bool:
        """
        Return if the player is the winner.

        >>> a = Game(True)
        >>> a.is_winner('p1')
        builtins.NotImplementedError: must implement a subclass!
        """
        raise NotImplementedError('must implement a subclass!')

    def str_to_move(self, move: str) -> Any:
        """
        Return a move based on the string inputed.

        >>> a = Game(True)
        >>> a.str_to_move('1')
        builtins.NotImplementedError: must implement a subclass!
        """
        raise NotImplementedError('must implement a subclass!')


class SubtractSquareGame(Game):
    """
    A game of subtracting squares.
    """
    def __init__(self, is_p1_turn: bool) -> None:
        """"
        Initialize the subtract square game.

        >>> a = SubtractSquareGame(True)
        Choose a non-negative integer: 20
        >>> type(a.current_state)
        <class '__main__.SubtractSquareState'>
        >>> a.current_player
        'p1'
        """
        Game.__init__(self, is_p1_turn)
        self.current_state = SubtractSquareState(is_p1_turn)
        self.current_player = self.current_state.current_player

    def get_instructions(self) -> str:
        """
        Return the instruction of the subtract square game.

        >>> a = SubtractSquareGame(True)
        Choose a non-negative integer: 20
        >>> print(a.get_instructions())
        1. A non-negative integer is chosen as the starting value.
        2. When the game starts, the player whose turn it is chooses
        some square of a positive integer (such as 1, 4, 9, 16, ...) to subtract
         from the value. The square provided must be less than the starting
         value. The next player choose another square to subtract from the new
         value.
         3. Play continues to alternate between the two players until no moves
         are possible. Whoever is about to play at that point loses!'
        """
        return '1. A non-negative integer is chosen as the starting value.\n' \
               '2. When the game starts, the player whose turn it is chooses' \
               'some square of a positive integer (such as 1, 4, 9, 16, ...) ' \
               'to subtract from the value. The square provided must be less ' \
               'than the starting value. The next player choose another ' \
               'square to subtract from the new value.\n3. Play continues to ' \
               'alternate between the two players until no moves are ' \
               'possible. Whoever is about to play at that point loses!'

    def is_over(self, current_state: SubtractSquareState) -> bool:
        """
        Return whether the current_state of the subtract square game is over.

        >>> a = SubtractSquareGame(True)
        Choose a non-negative integer: 20
        >>> a.is_over(a.current_state)
        False
        """
        return current_state.num == 0

    def is_winner(self, player: str) -> bool:
        """
        Return if the player is the winner.

        >>> a = SubtractSquareGame(True)
        Choose a non-negative integer: 20
        >>> a.is_winner('p1')
        False
        >>> a.is_winner('p2')
        False
        """
        return player != self.current_state.current_player and \
               self.is_over(self.current_state)

    def str_to_move(self, move: str) -> int:
        """
        Return a move based on the string inputed.

        >>> a = SubtractSquareGame(True)
        Choose a non-negative integer: 20
        >>> a.str_to_move('1')
        1
        """
        return int(move)


class ChopsticksGame(Game):
    """
    Chopsticks game.
    """
    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize the chopsticks game.

        >>> a = ChopsticksGame(True)
        >>> type(a.current_state)
        <class '__main__.SubtractSquareState'>
        >>> a.current_player
        'p1'
        """
        Game.__init__(self, is_p1_turn)
        self.current_state = ChopsticksState(is_p1_turn)
        self.current_player = self.current_state.current_player

    def get_instructions(self) -> str:
        """
        Return the instruction of the chopsticks game.

        >>> a = ChopsticksGame(True)
        >>> print(a.get_instructions())
        1. Each of two plaers begins with one finger pointed up on each of
        their hands.
        2. Player A touches one hand to one of Player Bs hands, increasing the
        number of fingers pointing up on Player Bs hand by the number on Player
        As hand. The number pointing up on Player As hand remains the same.
        3. If Player B now has five fingers up, that hand becomes "dead" or
        unplayable. If the number of fingers should exceed five, subtract five
        from the sum.
        4. Now Player B touches one hand to one of Player As hands, and the
        distribution of fingers proceeds as above, including the possibility of
        a "dead" hand.
        5. Play repeats steps 2-4 until some player has two "dead" hands, thus
        losing.'
        """
        return '1. Each of two plaers begins with one finger pointed up on ' \
               'each of their hands.\n2. Player A touches one hand to one of ' \
               'Player Bs hands, increasing the number of fingers pointing up '\
               'on Player Bs hand by the number on Player As hand. The number '\
               'pointing up on Player As hand remains the same.\n3. If ' \
               'Player B now has five fingers up, that hand becomes "dead" or '\
               'unplayable. If the number of fingers should exceed five, ' \
               'subtract five from the sum.\n4. Now Player B touches one ' \
               'hand to one of Player As hands, and the distribution of ' \
               'fingers proceeds as above, including the possibility of a ' \
               '"dead" hand.\n5. Play repeats steps 2-4 until some player ' \
               'has two "dead" hands, thus losing.'

    def is_over(self, current_state: ChopsticksState) -> bool:
        """
        Return whether the current_state of the chopsticks game is over.

        >>> a = ChopsticksGame(True)
        >>> a.is_over(a.current_state)
        False
        """
        return current_state.players_finger[:2] == [0, 0] or \
               current_state.players_finger[2:] == [0, 0]

    def is_winner(self, player: str) -> bool:
        """
        Return if the player is the winner.

        >>> a = ChopsticksGame(True)
        >>> a.is_winner('p1')
        False
        """
        if self.current_state.players_finger[:2] == [0, 0]:
            if player == 'p1':
                return False
            else:
                return True
        elif self.current_state.players_finger[2:] == [0, 0]:
            if player == 'p2':
                return False
            else:
                return True
        else:
            return False

    def str_to_move(self, move: str) -> str:
        """
        Return a move based on the string inputed.

        >>> a = ChopsticksGame(True)
        >>> a.str_to_move('ll')
        'll'
        """
        return move


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
