import string


def encrypt(plaintext, shift):
    alphabet = list(string.ascii_lowercase)
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    encrypted_message = ""

    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            index = alphabet.index(char)
            shifted_char = shifted_alphabet[index]
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_message += shifted_char
        else:
            encrypted_message += char
    return encrypted_message


def decrypt(plaintext, shift):
    return encrypt(plaintext, -shift)


def crack(plaintext):
    for shift in range(26):
        cracked = encrypt(plaintext, -shift)
        if "the" in cracked.lower() and "of" in cracked.lower():
            return cracked
    return ""


