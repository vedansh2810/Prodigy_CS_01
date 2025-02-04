"""
The Ceasar cipher is one of the simplest and one of the earliest known ciphers.
It is a type of substitution cipher that 'shifts' a letter by a fixed amount in the alphabet.

For example with a shift = 3:
a -> d
b -> e
z -> c

"""

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

# letter_to_index creates a dictionary that maps each letter to its corresponding index
letter_to_index = dict(zip(alphabet, range(len(alphabet))))

# index_to_letter is the reverse mapping, converting numbers back into letters
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def encrypt(message, shift):
    cipher = ""

    for letter in message:
        if letter in letter_to_index:
            number = (letter_to_index[letter] + shift) % len(letter_to_index)
            letter = index_to_letter[number]
        cipher += letter

    return cipher

def decrypt(cipher, shift):
    decrypted = ""

    for letter in cipher:
        if letter in letter_to_index:
            number = (letter_to_index[letter] - shift) % len(letter_to_index)
            letter = index_to_letter[number]
        decrypted += letter

    return decrypted

def main():
    message = input("Enter your message: ")
    if not message:
        print("The message cannot be empty.")
        return

    try:
        shift = int(input("Enter the shift: "))
    except ValueError:
        print("The shift value must be an integer.")
        return

    encrypted_message = encrypt(message, shift)
    decrypted_message = decrypt(encrypted_message, shift)

    print("Encrypted message: ", encrypted_message)
    print("Decrypted message: ", decrypted_message)

if __name__ == "__main__":
    main()
