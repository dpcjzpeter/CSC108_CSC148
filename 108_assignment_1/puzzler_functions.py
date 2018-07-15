"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles_small.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """Return True if and only if the puzzle is the same as the view.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    """
    # put the function body here
    
    return puzzle == view


def game_over(puzzle: str, view: str, current_selection: str) -> bool:
    """Return True if and only if the puzzle is the same as the view or the
    current_selection is QUIT.
    
    >>> game_over('better', 'better', 'S')
    True
    >>> game_over('axed', 'aced', 'C')
    False
    >>> game_over('electricity', 'e^ec^^^c^^^', 'Q')
    True
    """
    
    if current_selection == 'Q':
        return True
    else:
        return puzzle == view


def bonus_letter(puzzle: str, view: str, letter: str) -> bool:
    """Return True if and only if the letter appears in the puzzle but not in
    the view.
    
    >>> bonus_letter('cat', 'c^t', 'a')
    True
    >>> bonus_letter('water', 'w^t^^','h')
    False
    >>> bonus_letter('what', '^^^t', 't')
    False
    """
    
    return letter in puzzle and letter not in view


def update_letter_view(puzzle: str, view: str, index: int, letter: str) -> str:
    """Return a single character string representing the next view of the
    character at the given index. If the character at that index of the puzzle
    matches the letter guessed, then return that character. Otherwise, return 
    the character at that index of the view.
    
    >>> update_letter_view('lesson', 'l^^^^n', 1, 'e')
    'e'
    >>> update_letter_view('ground', '^r^^^^', 4, 'u')
    '^'
    """
    
    if puzzle[index] == letter:
        return letter
    else:
        return view[index]


def calculate_score(current_score: int, num_occurence: int, letter_type: str) -> int:
    """Return the new score by adding CONSONANT_POINTS per num_occurrence of the
    letter to the current_score if the letter_type is CONSONANT, or by deducting
    the VOWEL_PRICE from the current_score if the letter_type is VOWEL.
    
    >>> calculate_score(5, 2, 'C')
    7
    >>> calculate_score(2, 4, 'V')
    1
    """
    
    if letter_type == 'C':
        return current_score + CONSONANT_POINTS * num_occurence
    else:
        return current_score - VOWEL_PRICE


def next_player(current_player: str, num_occurence: int) -> str:
    """Return the next player (one of PLAYER_ONE or PLAYER_TWO). Return the
    current_player if the num_occurence in the puzzle of the letter last chosen
    is greater than 0. Otherwise, return the other player.
    
    >>> next_player('Player One', 3)
    'Player One'
    >>> next_player('Player Two', 0)
    'Player One'
    """
    
    players = ['Player One', 'Player Two']
    if num_occurence > 0:
        return current_player
    else:
        players.remove(current_player)
        return players[0]
