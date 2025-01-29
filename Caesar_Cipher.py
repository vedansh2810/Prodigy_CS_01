"""
The Ceasar cipher is one of the simplest and one of the earliest known ciphers.
It is a type of substitution cipher that 'shifts' a letter by a fixed amount in the alphabet.

For example with a shift = 3:
a -> d
b -> e
z -> c

"""

alphabet = "abcdefghijklmnopqrstuvwxyz "

#letter_to_index creates a dictionary that maps each letter to its corresponding index (e.g., 'a': 0, 'b': 1, ..., 'z': 25, ' ': 26)
letter_to_index = dict(zip(alphabet, range(len(alphabet))))

#index_to_letter is the reverse mapping, converting numbers back into letters
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, shift):
    cipher = ""

    for letter in message:
        number = (letter_to_index[letter] + shift) % len(letter_to_index)
        letter = index_to_letter[number]
        cipher += letter

    return cipher


def decrypt(cipher, shift):
    decrypted = ""

    for letter in cipher:
        number = (letter_to_index[letter] - shift) % len(letter_to_index)
        letter = index_to_letter[number]
        decrypted += letter

    return decrypted


def main():
    message = input("Enter your message :")
    shift = int(input("Enter the shift :"))
    print("Encrypted message : ", encrypt(message, shift))
    print("Decrypted message : ", decrypt(encrypt(message, shift), shift))

main()
