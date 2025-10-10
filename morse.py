MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',  'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',  'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',  'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',  'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',  'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---','3': '...--',
    '4': '....-', '5': '.....', '6': '-....','7': '--...',
    '8': '---..', '9': '----.',
    ' ': '/'
}

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            raise ValueError(f"Character '{char}' cannot be converted to Morse code...")
    return ' '.join(morse_code)

REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def morse_to_text(morse):
    text = []
    for morse_char in filter(None, morse.split(' ')):               #Filter extra spaces to avoid errors
        if morse_char in REVERSE_MORSE_CODE_DICT:
            text.append(REVERSE_MORSE_CODE_DICT[morse_char])
        else:
            raise ValueError(f"Morse code '{morse_char}' cannot be converted to text...")
    return ''.join(text)


