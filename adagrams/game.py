import random
import copy

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():

    letter_pool_copy = copy.deepcopy(LETTER_POOL)
    player_hand = []
    letter_weights = list(LETTER_POOL.values())
    letter_pool_list = list(LETTER_POOL.keys())

    while len(player_hand) < 10:
        letter = (random.choices(letter_pool_list, weights= (letter_weights)))

        if letter_pool_copy[letter[0]] == 0:
            continue
        else:
            letter_pool_copy[letter[0]] -= 1

        player_hand.append(letter[0])

    return player_hand


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass