# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
# def load_names(path):
#     with open(path) as text_file:
#         return text_file.read().splitlines()
#
# names = load_names('names.txt')
def load_cipher(path):
    with open('ciphertext.txt', 'r') as reader:
        print(reader.read())
        return reader.read().splitlines()


encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

first_string = 'hello'
words = load_cipher('ciphertext.txt')

def encode(old_string):
    new_string = ''

    for symbol in old_string.upper():
        new_string = new_string + encode_table[symbol]

        return new_string


raggle = encode(words)
print(raggle)

decode_table = {}
for key, value in encode_table.items():
    decode_table[value] = key


def decode(old_string):
    new_string = ''

    for letter in old_string.upper():
        new_string = new_string + decode_table[letter]

    return new_string


decoded = decode(raggle)
print(decoded)

# message = 'HRIXAS ZJGKM YDLUB WPCNQ OTEFV'
# ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# for key in range(len(ABC)):
#
#     translated = ''
#
#     for symbol in message:
#         if symbol in ABC:
#             num = ABC.find(symbol)
#             num = num - key
#
#         if num < 0:
#             num = num + len(ABC)
#
#         translated = translated + ABC[num]
#
#     else:
#         translated = translated + symbol
#     print('Key #%s: %s' % (key, translated))
