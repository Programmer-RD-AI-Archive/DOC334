from inital import *
import sys

args = list(sys.argv)
args = list(filter(lambda arg: arg.split('.')[-1] == "txt",args))
encrypted_file, decrypted_file = args

with open(encrypted_file, 'r') as e_file:
    txt = e_file.read().split(' ')
    
new_txt = ""
for t in txt:
    new_t = ""
    for letter in t:
        new_t += all_combinations_alphabet[rdm_combination.index(letter)] if letter in all_combinations_alphabet else ""
    new_txt += new_t + " "

with open(decrypted_file, 'w') as d_file:
    d_file.write(new_txt)
