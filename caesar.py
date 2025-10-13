def caesar_cipher(text, shift, mode='encrypt'):
    if not isinstance(text, str):
        raise ValueError("Text must be a string.")
    if not isinstance(shift, int):
        raise ValueError("Shift must be an integer.")
    if mode not in ['encrypt', 'decrypt']:
        raise ValueError("Mode must be 'encrypt' or 'decrypt'.")
    
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')                 # ORD Determines ASCII base for uppercase/lowercase
            if mode == 'encrypt':
                shifted = (ord(char) - base + shift) % 26 + base
            elif mode == 'decrypt':
                shifted = (ord(char) - base - shift) % 26 + base
            else:
                raise ValueError("Mode must be 'encrypt' or 'decrypt'.")
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)
