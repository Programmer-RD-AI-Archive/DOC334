from inital import *
import sys

args = list(sys.argv)
args = list(filter(lambda arg: arg.split('.')[-1] == "txt",args))
init_file, final_file = args

with open(init_file, 'r') as init_f:
    txt = init_f.read().split(' ')

new_txt = ""
for t in txt:
    new_t = ""
    for letter in t:
        new_t += rdm_combination[all_combinations_alphabet.index(letter)] if letter in all_combinations_alphabet else ""
    new_txt += new_t + " "

with open(final_file, 'w') as final_f:
    final_f.write(new_txt)
