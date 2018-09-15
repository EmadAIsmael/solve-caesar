'''

1. read frequency table
2. count letter occurences in text and total count of all letters
2. calculate frequencies in text ans sort accordingly
3. compare frequency table with text frequencies
4. compute calculated shift.
5. return decrypted text

url for English language letter frequency table:
http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html

'''

alphabet = lambda shift: [chr((c + shift) % 26 + ord('a')) for c in range(26)]


# plain = alphabet(0)
# cipher = alphabet(5)
# print(list(plain))
# print(cipher)

def encrypt(text, key):
    plain = alphabet(0)
    cipher = alphabet(key)
    cipher_text = ''
    for c in text:
        if 'a' <= c <= 'z':
            cipher_text += cipher[plain.index(c)]
        else:
            cipher_text += c
    return cipher_text


def decrypt(text, key):
    plain = alphabet(0)
    cipher = alphabet(key)
    plain_text = ''
    for c in text:
        if 'a' <= c <= 'z':
            plain_text += plain[cipher.index(c)]
        else:
            plain_text += c
    return plain_text


# plain_text = 'hello'
# cipher_text = encrypt(plain_text, 7)

# print(encrypt(plain_text, 7))
#
# print(decrypt(cipher_text, 7))


ftable = []
with open("English_language_letter_frequency_ratios.txt", "r") as f:
    for r in f:
        x = r.strip().split(",")
        ftable.append([x[0], float(x[1])])

txt_freq = {chr(c + ord('A')): 0 for c in range(26)}
letter_cnt = 0

with open("caesar_cipher_encrypted_text.txt", "r") as f:
    cipher_text = f.read().upper()

for c in cipher_text:
    if 'A' <= c <= 'Z':
        txt_freq[c] += 1
        letter_cnt += 1

ftext = []
for k, v in txt_freq.items():
    ftext.append([k, round(v / letter_cnt * 100)])
ftext.sort(key=lambda r: r[1], reverse=True)

print(decrypt(cipher_text.lower(), ord(ftext[0][0]) - ord(ftable[0][0])))

