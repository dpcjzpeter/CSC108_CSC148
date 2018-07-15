"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
from stack import Stack
from tree import Tree

# TODO: Adjust the type annotation as needed.


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


# TODO: Implement a recursive version of the minimax strategy.
def minimax_recursive_strategy(game: Any) -> Any:
    """
    Return a move for game through applying recursive minimax strategy.
    """
    state = game.current_state
    moves = game.current_state.get_possible_moves()
    player = game.current_state.get_current_player_name()
    lst = [recursion_helper(game, state, move, player) for move in moves]
    if max(lst) == 1 or max(lst) == 0:
        return moves[lst.index(max(lst))]
    return moves[0]


# TODO: Implement an iterative version of the minimax strategy.
def minimax_iterative_strategy(game: Any) -> Any:
    """
    Return a move for game through applying interactive minimax strategy.
    """
    state = game.current_state
    moves = state.get_possible_moves()
    stack = Stack()
    stack.add([Tree(state), []])
    box = []
    while not stack.is_empty():
        re = stack.remove()
        if re[0].value.get_possible_moves() != [] and re[0].children == []:
            lst = []
            for move in re[0].value.get_possible_moves():
                lst.append([Tree(re[0].value.make_move(move)), []])
            stack.add([Tree(re[0].value, lst), []])
            for l in lst:
                stack.add(l)
        elif game.is_over(re[0].value):
            game.current_state = re[0].value
            player = re[0].value.get_current_player_name()
            if game.is_winner(player):
                re[1] = 1
            else:
                re[1] = -1 if game.is_winner('p1') or \
                    game.is_winner('p2') else 0
            box.append(re)

        else:
            count = []
            for i in re[0].children:
                count += [a[1] * -1 for a in box if a[0].value is i[0].value]
            re[1] = max(count)
            box.append(re)

    score = []
    for i in box[-1][0].children:
        for itm in box:
            if i[0].value == itm[0].value:
                score.append(itm[1] * -1)
    if 1 in score:
        return moves[score.index(1)]
    elif 0 in score:
        return moves[score.index(0)]
    return moves[0]


def recursion_helper(game: Any, state: Any, move: Any, player: Any) -> Any:
    """
    Return a number on the interval [-1, 0, 1] based on game, state, move
    to make and current player.
    """
    new_state = state.make_move(move)
    moves = new_state.get_possible_moves()
    if game.is_over(new_state):
        game.current_state = new_state
        if game.is_winner(player):
            return 1
        elif game.is_winner('p1') or game.is_winner('p2'):
            return -1
        return 0
    elif new_state.get_current_player_name() == player:
        return max(recursion_helper(game, new_state, x, player) for x in moves)
    else:
        return min(recursion_helper(game, new_state, x, player) for x in moves)


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
