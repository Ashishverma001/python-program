from helper import read
data = read('pride_n_prejudice.txt')
from string import ascii_lowercase

for letter in ascii_lowercase:
    Counter = data.count(letter)
    print(f'{letter} found {Counter}times')

# wap to find the most occuring alphabets and its frequency

freq = 0
freq_letter = ''
for letter  in ascii_lowercase:
    print(f'{letter} found {Counter} time')
    if freq < Counter:
        freq = Counter #70510
        freq_letter=letter#e
print(f'most frequent letter is {freq_letter}occure {freq} times')