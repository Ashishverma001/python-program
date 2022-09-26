from string import punctuation
import helper as h 

data = h.read('pride_n_prejudice.txt')
print(len(data))

# remove punctuation 
for p in punctuation:
    data = data.replace(p,'')

# string into words and remove spaces and empty string 
words =[words.strip()for word in data.lower().split()]

print("TOTAL WORDS FOUND: ",len(words))
print("UNIQUE WORDS FOUND: ",len(set(words)))

# creat a dicitionary
wc = {}
for word in set(words):
    wc[word] = words.count(word)

# sorting the dictionary -> wc,items() return a list of tuple 
wc = sorted(wc.items(), key=lambda x: x[1], reverse=True)

# print the top 10 words 
for i in range(10):
    print(wc[i]) 