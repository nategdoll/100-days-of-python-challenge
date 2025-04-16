alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(phrase, shift):
    encoded_phrase = ""
    
    for letter in phrase:
        index = alphabet.index(letter)
        new_index = (index + shift) % len(alphabet)
        encoded_phrase += alphabet[new_index]

    return encoded_phrase

def decode(phrase, shift):
    return encode(phrase, len(alphabet)-shift)