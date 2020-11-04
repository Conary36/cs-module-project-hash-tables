# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

message = 'HRIXAS ZJGKM YDLUB WPCNQ OTEFV'
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(ABC)):

    translated = ''

    for symbol in message:
        if symbol in ABC:
            num = ABC.find(symbol)
            num = num - key

        if num < 0:
            num = num + len(ABC)

        translated = translated + ABC[num]

    else:
        translated = translated + symbol
    print('Key #%s: %s' % (key, translated))






