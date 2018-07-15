"""
An implementation of the game and state of stonehenge.
"""
from game import Game
from typing import Any
from game_state import GameState


class StonehengeGame(Game):
    """
    Abstract class for a game to be played with two players.
    """

    def __init__(self, p1_starts):
        """
        Initialize this Game.

        :param p1_starts: A boolean representing whether Player 1 is the first
                          to make a move.
        :type p1_starts: bool
        """
        side_length = int(input("Enter the number of length: "))
        self.current_state = StonehengeState(p1_starts, side_length)

    def get_instructions(self):
        """
        Return the instructions for this Game.

        :return: The instructions for this Game.
        :rtype: str
        """
        return "Players take turns claiming cells. When a player" \
               "captures at least half of the cells in a ley-line," \
               "then the player captures that ley-line. The first " \
               "player to capture at least half of the ley-lines is " \
               "the winner. A ley-line, once claimed, cannot be taken " \
               "by the other player."

    def is_over(self, state):
        """
        Return whether or not this game is over.

        :return: True if the game is over, False otherwise.
        :rtype: bool
        """
        count1 = 0
        count2 = 0
        s = state.ley_lines
        for ch in s:
            count1 += 1 if ch == 1 else 0
            count2 += 1 if ch == 2 else 0
        return count1 >= len(s) * 0.5 or count2 >= len(s) * 0.5

    def is_winner(self, player):
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.

        :param player: The player to check.
        :type player: str
        :return: Whether player has won or not.
        :rtype: bool
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string):
        """
        Return the move that string represents. If string is not a move,
        return an invalid move.

        :param string:
        :type string:
        :return:
        :rtype:
        """
        if not (string.strip().isupper() and len(string.strip()) == 1):
            return -1

        return string.strip()


class StonehengeState(GameState):
    """
    The state of a game at a certain point in time.
    """

    def __init__(self, is_p1_turn: bool, side_length: int, new_grid={}) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.
        """
        super().__init__(is_p1_turn)
        self.length = side_length
        self.grid = new_grid

        if self.grid == {}:
            self.grid = self.get_grid()
        self.ley_lines = self.get_ley_lines()

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        if self.length == 1:
            return '      {}   {}\n     /   /\n{} - {} - {}\n     \ / \ \n' \
                   '  {} - {}   {}\n       \ \n        {}'.format(
                    self.grid['down-left diagonals'][1][0],
                    self.grid['down-left diagonals'][2][0],
                    self.grid['rows'][1][0], self.grid['rows'][1][1],
                    self.grid['rows'][1][2], self.grid['rows'][2][0],
                    self.grid['rows'][2][1],
                    self.grid['down-right diagonals'][2][0],
                    self.grid['down-right diagonals'][1][0])
        elif self.length == 2:
            return '        {}   {}\n       /   /\n  {} - {} - {}   {}\n' \
                   '     / \ / \ /\n{} - {} - {} - {}\n     \ / \ / \ \n' \
                   '  {} - {} - {}   {}\n       \   \ \n        {}   {}'.format(
                    self.grid['down-left diagonals'][1][0],
                    self.grid['down-left diagonals'][2][0],
                    self.grid['rows'][1][0], self.grid['rows'][1][1],
                    self.grid['rows'][1][2],
                    self.grid['down-left diagonals'][3][0],
                    self.grid['rows'][2][0], self.grid['rows'][2][1],
                    self.grid['rows'][2][2], self.grid['rows'][2][3],
                    self.grid['rows'][3][0], self.grid['rows'][3][1],
                    self.grid['rows'][3][2],
                    self.grid['down-right diagonals'][3][0],
                    self.grid['down-right diagonals'][1][0],
                    self.grid['down-right diagonals'][2][0])
        elif self.length == 3:
            return '          {}   {}\n         /   /\n    {} - {} - {}   {}\n'\
                   '       / \ / \ /\n  {} - {} - {} - {}   {}\n' \
                   '     / \ / \ / \ /\n{} - {} - {} - {} - {}\n' \
                   '     \ / \ / \ / \ \n  {} - {} - {} - {}   {}\n' \
                   '       \   \   \ \n        {}   {}   {}'.format(
                    self.grid['down-left diagonals'][1][0],
                    self.grid['down-left diagonals'][2][0],
                    self.grid['rows'][1][0], self.grid['rows'][1][1],
                    self.grid['rows'][1][2],
                    self.grid['down-left diagonals'][3][0],
                    self.grid['rows'][2][0], self.grid['rows'][2][1],
                    self.grid['rows'][2][2], self.grid['rows'][2][3],
                    self.grid['down-left diagonals'][4][0],
                    self.grid['rows'][3][0], self.grid['rows'][3][1],
                    self.grid['rows'][3][2], self.grid['rows'][3][3],
                    self.grid['rows'][3][4], self.grid['rows'][4][0],
                    self.grid['rows'][4][1], self.grid['rows'][4][2],
                    self.grid['rows'][4][3],
                    self.grid['down-right diagonals'][4][0],
                    self.grid['down-right diagonals'][1][0],
                    self.grid['down-right diagonals'][2][0],
                    self.grid['down-right diagonals'][3][0])
        elif self.length == 4:
            return '            {}   {}\n           /   /\n' \
                   '      {} - {} - {}   {}\n         / \ / \ /\n' \
                   '    {} - {} - {} - {}   {}\n       / \ / \ / \ /\n' \
                   '  {} - {} - {} - {} - {}\n     / \ / \ / \ / \ /\n' \
                   '{} - {} - {} - {} - {} - {}   {}\n' \
                   '     \ / \ / \ / \ / \ \n  {} - {} - {} - {} - {}  {}\n' \
                   '       \   \   \   \ \n        {}   {}   {}   {}'.format(
                    self.grid['down-left diagonals'][1][0],
                    self.grid['down-left diagonals'][2][0],
                    self.grid['rows'][1][0], self.grid['rows'][1][1],
                    self.grid['rows'][1][2],
                    self.grid['down-left diagonals'][3][0],
                    self.grid['rows'][2][0], self.grid['rows'][2][1],
                    self.grid['rows'][2][2], self.grid['rows'][2][3],
                    self.grid['down-left diagonals'][4][0],
                    self.grid['rows'][3][0], self.grid['rows'][3][1],
                    self.grid['rows'][3][2], self.grid['rows'][3][3],
                    self.grid['rows'][3][4],
                    self.grid['down-left diagonals'][5][0],
                    self.grid['rows'][4][0], self.grid['rows'][4][1],
                    self.grid['rows'][4][2], self.grid['rows'][4][3],
                    self.grid['rows'][4][4], self.grid['rows'][4][5],
                    self.grid['rows'][3][0], self.grid['rows'][3][1],
                    self.grid['rows'][3][2], self.grid['rows'][3][3],
                    self.grid['rows'][3][4],
                    self.grid['down-right diagonals'][5][0],
                    self.grid['down-right diagonals'][1][0],
                    self.grid['down-right diagonals'][2][0],
                    self.grid['down-right diagonals'][3][0],
                    self.grid['down-right diagonals'][4][0])
        elif self.length == 4:
            return '              {}   {}\n             /   /\n' \
                   '        {} - {} - {}   {}\n           / \ / \ /\n' \
                   '      {} - {} - {} - {}   {}\n         / \ / \ / \ /\n' \
                   '    {} - {} - {} - {} - {}   {}\n' \
                   '       / \ / \ / \ / \ /\n' \
                   '  {} - {} - {} - {} - {} - {}   {}\n' \
                   '     / \ / \ / \ / \ / \ /\n' \
                   '{} - {} - {} - {} - {} - {} - {}\n' \
                   '     \ / \ / \ / \ / \ / \ \n' \
                   '  {} - {} - {} - {} - {} - {}   {}\n' \
                   '       \   \   \   \   \ \n' \
                   '        {}   {}   {}   {}   {}'.format(
                    self.grid['down-left diagonals'][1][0],
                    self.grid['down-left diagonals'][2][0],
                    self.grid['rows'][1][0], self.grid['rows'][1][1],
                    self.grid['rows'][1][2],
                    self.grid['down-left diagonals'][3][0],
                    self.grid['rows'][2][0], self.grid['rows'][2][1],
                    self.grid['rows'][2][2], self.grid['rows'][2][3],
                    self.grid['down-left diagonals'][4][0],
                    self.grid['rows'][3][0], self.grid['rows'][3][1],
                    self.grid['rows'][3][2], self.grid['rows'][3][3],
                    self.grid['rows'][3][4],
                    self.grid['down-left diagonals'][5][0],
                    self.grid['rows'][4][0], self.grid['rows'][4][1],
                    self.grid['rows'][4][2], self.grid['rows'][4][3],
                    self.grid['rows'][4][4], self.grid['rows'][4][5],
                    self.grid['down-left diagonals'][6][0],
                    self.grid['rows'][5][0], self.grid['rows'][5][1],
                    self.grid['rows'][5][2], self.grid['rows'][5][3],
                    self.grid['rows'][5][4], self.grid['rows'][5][5],
                    self.grid['rows'][5][6], self.grid['rows'][6][0],
                    self.grid['rows'][6][1], self.grid['rows'][6][2],
                    self.grid['rows'][6][3], self.grid['rows'][6][4],
                    self.grid['rows'][6][5],
                    self.grid['down-right diagonals'][6][0],
                    self.grid['down-right diagonals'][1][0],
                    self.grid['down-right diagonals'][2][0],
                    self.grid['down-right diagonals'][3][0],
                    self.grid['down-right diagonals'][4][0],
                    self.grid['down-right diagonals'][5][0])

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        """
        moves = []
        count1 = 0
        count2 = 0
        for ch in self.ley_lines:
            count1 += 1 if ch == 1 else 0
            count2 += 1 if ch == 2 else 0
        over = count1 >= len(self.ley_lines) * 0.5 or \
            count2 >= len(self.ley_lines) * 0.5

        rows = self.grid['rows']
        cell = []
        for key in rows:
            for ch in rows[key]:
                cell.append(ch)
        for ch in cell:
            if type(ch) == str:
                if ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and ch not in moves:
                    moves.append(ch)
        if over:
            return []
        return moves

    def make_move(self, move: Any) -> "StonehengeState":
        """
        Return the GameState that results from applying move to this GameState.
        """
        new_grid = {}
        for key1 in self.grid:
            new_grid[key1] = {}
            for key2 in self.grid[key1]:
                lst = self.grid[key1][key2]
                new_grid[key1][key2] = lst[:]
                n = new_grid[key1][key2]
                if move in n:
                    n[n.index(move)] = 1 if self.p1_turn else 2
                count1 = 0
                count2 = 0
                for cell in n:
                    count1 += 1 if cell == 1 else 0
                    count2 += 1 if cell == 2 else 0
                if n[0] == '@' and self.p1_turn:
                    n[0] = 1 if count1 >= (len(n) - 1)/2 else '@'
                elif n[0] == '@' and not self.p1_turn:
                    n[0] = 2 if count2 >= (len(n) - 1)/2 else '@'
            self.ley_lines = self.get_ley_lines()

        if self.p1_turn:
            turn = False
        else:
            turn = True
        return StonehengeState(turn, self.length, new_grid)

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        return 'StonehengeState({}, {}, {})'.format(repr(self.p1_turn),
                                                    repr(self.length),
                                                    repr(self.grid))

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        moves = self.get_possible_moves()
        for move in moves:
            new_state = self.make_move(move)
            new_moves = new_state.get_possible_moves()
            if new_moves == []:
                return 1
        for move in moves:
            new_state = self.make_move(move)
            new_moves = new_state.get_possible_moves()
            lst = [new_state.make_move(x) for x in new_moves]
            for state in lst:
                if state.get_possible_moves() == []:
                    return -1
        if moves == []:
            return -1
        return 1

    def get_rows(self) -> dict:
        """
        Return the current result for key_lines in row.
        """
        rows = {}
        str_list = []
        for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            str_list.append(ch)

        counter = 0
        for num in range(2, self.length + 2):
            line = str_list[counter:counter + num]
            rows[num - 1] = line
            counter += num
        next_ch = str_list.index(rows[self.length][-1]) + 1
        rows[self.length + 1] = str_list[next_ch:next_ch + self.length]

        for key in rows:
            rows[key].insert(0, '@')

        return rows

    def get_down_left_diagonals(self) -> dict:
        """
        Return the current result for key_lines for down-left diagonals.
        """
        down_left_diagonals = {}
        rows = self.get_rows()
        for key in rows:
            rows[key].remove('@')

        for num in range(self.length + 1):
            line = []
            for i in range(1, self.length + 1):
                try:
                    line.append(rows[i][num])
                except IndexError:
                    pass
            if num - 1 >= 0:
                line.append(rows[self.length + 1][num - 1])
            down_left_diagonals[num + 1] = line

        for key in down_left_diagonals:
            down_left_diagonals[key].insert(0, '@')

        return down_left_diagonals

    def get_down_right_diagonals(self) -> dict:
        """
        Return the current result for key_lines for down-right diagonals.
        """
        down_right_diagonals = {}
        rows = self.get_rows()
        for key in rows:
            rows[key].remove('@')

        for num in range(self.length + 1):
            line = []
            for i in range(2):
                try:
                    line.append(rows[self.length + 1 - i][num])
                except IndexError:
                    pass
            for i in range(2, self.length + 1):
                try:
                    line.append(rows[self.length + 1 - i]
                                    [num - self.length - 1])
                except IndexError:
                    pass
            down_right_diagonals[num + 1] = line

        for key in down_right_diagonals:
            down_right_diagonals[key].insert(0, '@')

        return down_right_diagonals

    def get_grid(self) -> dict:
        """
        Return the current result for key_lines.
        """
        return {'rows': self.get_rows(),
                'down-right diagonals': self.get_down_right_diagonals(),
                'down-left diagonals': self.get_down_left_diagonals()}

    def get_ley_lines(self) -> list:
        """
        Return the current ley
        """
        ley_lines = []
        for key1 in self.grid:
            for key2 in self.grid[key1]:
                ley_lines.append(self.grid[key1][key2][0])
        return ley_lines


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
