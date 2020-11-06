# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
message = 'GUVF VF ZL FRPERG ZRFFNTR.'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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

decode_table = {}
for key, value in encode_table.items():
    decode_table[value] = key


def load_cipher():
    with open('ciphertext.txt', 'r') as f:
        s = " ".join([l.rstrip() for l in f])
    return s


def encode(old_string):
    new_string = ''

    print(type(old_string))
    for symbol in old_string.upper():
        if symbol.isalpha():

            new_string = new_string + encode_table[symbol]
        else:
            new_string += symbol
    return new_string


def decode(old_string):
    plain_text = ''

    for letter in old_string.upper():
        # print(letter, end='')
        # if letter in [' ', ',' '.']:
        #     plain_text += ' '
        # else:
        if letter.isalpha():

            plain_text = plain_text + decode_table[letter]
        else:
            plain_text = plain_text + letter
    return plain_text


def char_freq(str):
    freq = {}
    for c in str:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq


cipher_text = load_cipher()[0:100]
plain_text = decode(cipher_text)
print(plain_text)

plain_text_character_freqs = char_freq(plain_text)
print(plain_text_character_freqs)

total = sum(plain_text_character_freqs.values())

# 234/1600 * 100

# for i in plaintext:
# if letter[i] not in dict set value to 1:
# if letter in dictionary increase by 1

# loop through every possible key
for key in range(len(LETTERS)):

    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared.
    translated = ''

    # The rest of the program is the same as the original Caesar program:

    # run the encryption/decryption code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)  # get the number of the symbol
            num = num - key

            # handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)

            # add number's symbol at the end of translated
            translated = translated + LETTERS[num]

        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol

    # display the current key being tested, along with its decryption
    print('Key #%s: %s' % (key, translated))