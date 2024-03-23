import random
random.seed(42)
alphabet = "abcdefghijklmnopqrstuvwxyz"
all_combinations_alphabet = list(alphabet + alphabet.upper())
rdm_combination = all_combinations_alphabet.copy()
random.shuffle(rdm_combination)
