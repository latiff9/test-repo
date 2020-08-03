# sentence = "This is a common interview question to tackle in a short time"
# char_freq = set(sentence.lower())
# # print(char_freq)

# # Find the number of times char occurs
# char_list = []
# for char in char_freq:
#     char_list.append((char, sentence.count(char)))
# # print(char_list)

# # Sort list based on no of counts
# char_freq_sorted = sorted(char_list, key=lambda item: item[1], reverse=True)
# print(char_freq_sorted)
# print('=' * 40)
# print(char_freq_sorted[1])

# Alternative method using dictionary
from operator import itemgetter

sentence = "This is a common interview question to tackle in a short time"

char_list = set(sentence.lower())
print(char_list)

char_freq = {}
for ch in char_list:
    char_freq[ch] = sentence.count(ch)

print('dictionary')
print(char_freq)
print('-'*45)

char_freq_sorted = sorted(char_freq.items(), key=itemgetter(1), reverse=True)

# char_freq_sorted = sorted(
#     char_freq.items(), key=lambda item: item[1], reverse=True)

print('array of tuples')
print(char_freq_sorted)

print('-'*45)
print(char_freq_sorted[1])
