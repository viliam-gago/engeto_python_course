def caesar(message: str, offset: int):
    import string
    alphabet = string.ascii_lowercase
    new = ''

    for char in message:
        if char.lower() not in alphabet:
            new += ' '
        else:
            index = alphabet.index(char.lower())
            index = (index + offset) % len(alphabet)

            if char.islower():
                new += alphabet[index]
            else:
                new += alphabet[index].upper()

    return new


print(caesar('G jmtc Nwrfml Yaybckw',2))