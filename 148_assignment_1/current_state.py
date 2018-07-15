from typing import Any, List


class State:
    """
    A state of a game.
    """
    def __init__(self, is_p1_turn: bool, counter=1) -> None:
        """
        Initialize a state based on whether the game is_p1_turn or not. Setting
        a default parameter counter=1 for later use.

        >>> a = State(True)
        >>> a.turn
        1
        >>> a.p1_turn
        True
        >>> a.current_player
        'p1'
        >>> a.counter
        1
        """
        self.p1_turn = is_p1_turn
        self.counter = counter
        self.new_state = None
        if self.p1_turn == True:
            self.current_player = 'p1'
        else:
            self.current_player = 'p2'
        self.turn = 1

    def __str__(self) -> None:
        """
        Return the details of the current state.

        >>> a = State(True)
        >>> print(a)
        Game starts.
        Trun: 1. Player 1 is making the first move.
        """
        self.current = ''
        if self.turn == 1:
            self.current += 'Game starts.' + '\n' + 'Turn: 1'
            if self.current_player == 'p1':
                self.current += '. Player 1 is making the first move.'
            else:
                self.current += '. Player 2 is making the first move.'
        else:
            self.current += 'Turn: {}'.format(self.turn)
            if self.current_player == 'p1':
                self.current += '. Player 1 has to make a move.'
            else:
                self.current += '. Player 2 has to make a move.'

    def __eq__(self, other: Any) -> bool:
        """
        Return whether two states are equal.

        >>> a = State(True)
        >>> b = State(False)
        >>> a == b
        False
        >>> c = State(False)
        >>> b == c
        True
        """
        return type(self) == type(other) and self.turn == other.turn and \
               self.p1_turn == other.p1_turn

    def get_possible_moves(self) -> List[Any]:
        """
        Return all the possible moves.

        >>> a = State(True)
        >>> a.get_possible_moves()
        builtins.NotImplementedError: must implement a subclass!
        """
        raise NotImplementedError('must implement a subclass!')

    def get_current_player_name(self) -> str:
        """
        Return the name of the current player.

        >>> a = State(True)
        >>> a.get_current_player_name()
        builtins.NotImplementedError: must implement a subclass!
        """
        return self.current_player

    def is_valid_move(self, move_to_make: Any) -> bool:
        """
        Return whether the move_to_make is valid.

        >>> a = State(True)
        >>> a.is_valid_move(2)
        builtins.NotImplementedError: must implement a subclass!
        """
        raise NotImplementedError('must implement a subclass!')

    def make_move(self, move_to_make: Any) -> None:
        """
        Return a new state after making the move_to_make.

        >>> a = State(True)
        >>> a.make_move(1)
        builtins.NotImplementedError: must implement a subclass!
        """
        raise NotImplementedError('must implement a subclass!')


class SubtractSquareState(State):
    """
    A state for subtract square game.
    """
    def __init__(self, is_p1_turn: bool, counter=1) -> None:
        """
        Initialize a state for subtract square game.

        >>> a = SubtractSquareState(True, 2)
        >>> a.counter
        2
        >>> a.num
        None
        >>> a.all_moves
        []
        """
        State.__init__(self, is_p1_turn, counter)
        if self.counter == 1:
            self.num = int(input('Choose a non-negative integer: '))
        else:
            self.num = None
        self.all_moves = []

    def __str__(self):
        """
        Return the details of the current state of subtract square game.

        >>> a = SubtractSquareState(True)
        Choose a non-negative integer: 20
        >>> print(a)
        Game starts.
        Trun: 1. Player 1 is making the first move. Current number: 20
        """
        State.__str__(self)
        self.current += ' Current number: {}'.format(self.num)
        return self.current

    def get_possible_moves(self) -> List[int]:
        """
        Return all the possible moves.

        >>> a = SubtractSquareState(True)
        Choose a non-negative integer: 20
        >>> a.get_possible_moves()
        [1, 4, 9, 16]
        """
        self.all_moves = []
        for num in range(1, int(self.num ** 0.5) + 1):
            self.all_moves.append(num ** 2)
        return self.all_moves

    def is_valid_move(self, move_to_make: int) -> bool:
        """
        Return whether the move_to_make is valid.

        >>> a = SubtractSquareState(True)
        Choose a non-negative integer: 20
        >>> a.get_possible_moves()
        [1, 4, 9, 16]
        >>> a.is_valid_move(3)
        False
        >>> a.is_valid_move(4)
        True
        """
        return move_to_make in self.all_moves

    def make_move(self, move_to_make: int) -> 'SubtractSquareState':
        """
        Return a new state after making the move_to_make.

        >>> a = SubtractSquareState(True)
        Choose a non-negative integer: 20
        >>> a.get_possible_moves()
        [1, 4, 9, 16]
        >>> b = a.make_move(4)
        >>> print(b)
        Trun: 2. Player 2 has to make a move. Current number: 16
        """
        if self.turn % 2 == 1 and self.current_player == 'p1':
            self.new_state = SubtractSquareState(True, 2)
        else:
            self.new_state = SubtractSquareState(False, 2)

        self.new_state.turn = self.turn + 1
        self.new_state.num = self.num - move_to_make
        self.new_state.all_moves = self.new_state.get_possible_moves()

        if self.current_player == 'p1':
            self.new_state.current_player = 'p2'
        else:
            self.new_state.current_player = 'p1'

        return self.new_state


class ChopsticksState(State):
    """
    A state for chopsticks game.
    """
    def __init__(self, is_p1_turn: bool, counter=1) -> None:
        """
        Initialize a state for chopsticks game. The first two indices denote
        the finger pointing up on Player 1's left and right hand respectively.
        The last two indices denote the finger pointing up on Player 2's
        left and right hand respectively.

        ll - your left hand to opponent's left hand
        lr - your left hand to opponent's right hand
        rl - your right hand to opponent's left hand
        rr - your right hand to opponent's right hand


        >>> a = ChopsticksState(True)
        >>> a.players_finger
        [1, 1, 1, 1]
        >>> a.all_moves
        ['ll', 'lr', 'rl', 'rr']
        """
        State.__init__(self, is_p1_turn, counter)
        self.players_finger = [1, 1, 1, 1]
        self.all_moves = self.get_possible_moves()

    def __str__(self):
        """
        Return the details of the current state of chopsticks game.

        >>> a = ChopsticksState(True)
        >>> print(a)
        Game starts.
        Trun: 1. Player 1 is making the first move.
        """
        State.__str__(self)
        self.current += ' Player 1: {} - {}'.format(self.players_finger[0],
                                                    self.players_finger[1])
        self.current += ', Player 2: {} - {}'.format(self.players_finger[2],
                                                     self.players_finger[3])
        return self.current

    def get_possible_moves(self) -> List[str]:
        """
        Return all the possible moves of the current state.

        >>> a = ChopsticksState(True)
        >>> a.players_finger = [1, 1, 4, 1]
        >>> b = a.make_move('ll')
        >>> b.current_player
        'p2'
        >>> b.players_finger
        [1, 1, 0, 1]
        >>> b.get_possible_moves()
        ['rl', 'rr']
        """
        self.all_moves = ['ll', 'lr', 'rl', 'rr']
        if self.current_player == 'p1':
            if self.players_finger[0] == 0:
                if 'll' in self.all_moves:
                    self.all_moves.remove('ll')
                if 'lr' in self.all_moves:
                    self.all_moves.remove('lr')
            if self.players_finger[1] == 0:
                if 'rl' in self.all_moves:
                    self.all_moves.remove('rl')
                if 'rr' in self.all_moves:
                    self.all_moves.remove('rr')
            if self.players_finger[2] == 0:
                if 'll' in self.all_moves:
                    self.all_moves.remove('ll')
                if 'rl' in self.all_moves:
                    self.all_moves.remove('rl')
            if self.players_finger[3] == 0:
                if 'lr' in self.all_moves:
                    self.all_moves.remove('lr')
                if 'rr' in self.all_moves:
                    self.all_moves.remove('rr')
        else:
            if self.players_finger[2] == 0:
                if 'll' in self.all_moves:
                    self.all_moves.remove('ll')
                if 'lr' in self.all_moves:
                    self.all_moves.remove('lr')
            if self.players_finger[3] == 0:
                if 'rl' in self.all_moves:
                    self.all_moves.remove('rl')
                if 'rr' in self.all_moves:
                    self.all_moves.remove('rr')
            if self.players_finger[0] == 0:
                if 'll' in self.all_moves:
                    self.all_moves.remove('ll')
                if 'rl' in self.all_moves:
                    self.all_moves.remove('rl')
            if self.players_finger[1] == 0:
                if 'lr' in self.all_moves:
                    self.all_moves.remove('lr')
                if 'rr' in self.all_moves:
                    self.all_moves.remove('rr')
        return self.all_moves

    def is_valid_move(self, move_to_make: int) -> bool:
        """
        Return whether the move_to_make is valid.

        >>> a = ChopsticksState(True)
        >>> a.players_finger = [1, 1, 4, 1]
        >>> b = a.make_move('ll')
        >>> b.get_possible_moves()
        ['rl', 'rr']
        >>> b.is_valid_move('ll')
        False
        >>> b.is_valid_move('rl')
        True
        """
        self.all_moves = self.get_possible_moves()
        return move_to_make in self.all_moves

    def make_move(self, move_to_make: str) -> 'ChopsticksState':
        """
        Return a new state after making the move_to_make.

        >>> a = ChopsticksState(True)
        >>> a.players_finger = [1, 1, 4, 1]
        >>> b = a.make_move('ll')
        >>> print(b)
        Trun: 2. Player 2 has to make a move. Player 1: 1 - 1, Player 2: 0 - 1
        """
        self.new_state = None
        if self.p1_turn == True:
            self.new_state = ChopsticksState(True)
        else:
            self.new_state = ChopsticksState(False)

        self.new_state.turn = self.turn + 1
        self.new_state.all_moves = self.get_possible_moves()
        self.new_state.players_finger = self.players_finger[:]

        if self.current_player == 'p1':
            if move_to_make == 'll':
                self.new_state.players_finger[2] = (self.players_finger[2] +
                                                    self.players_finger[0]) % 5
            elif move_to_make == 'lr':
                self.new_state.players_finger[3] = (self.players_finger[3] +
                                                    self.players_finger[0]) % 5
            elif move_to_make == 'rl':
                self.new_state.players_finger[2] = (self.players_finger[2] +
                                                    self.players_finger[1]) % 5
            elif move_to_make == 'rr':
                self.new_state.players_finger[3] = (self.players_finger[3] +
                                                    self.players_finger[1]) % 5
        else:
            if move_to_make == 'll':
                self.new_state.players_finger[0] = (self.players_finger[0] +
                                                    self.players_finger[2]) % 5
            elif move_to_make == 'lr':
                self.new_state.players_finger[1] = (self.players_finger[1] +
                                                    self.players_finger[2]) % 5
            elif move_to_make == 'rl':
                self.new_state.players_finger[0] = (self.players_finger[0] +
                                                    self.players_finger[3]) % 5
            elif move_to_make == 'rr':
                self.new_state.players_finger[1] = (self.players_finger[1] +
                                                    self.players_finger[3]) % 5

        if self.current_player == 'p1':
            self.new_state.current_player = 'p2'
        else:
            self.new_state.current_player = 'p1'

        return self.new_state


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
