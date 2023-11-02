import sys


NESTED_MORSE = {
        " ": "/ ",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        '?':'..--..',
        '/':'-..-.',
        '-':'-....-',
        '(':'-.--.',
        ')':'-.--.-'
}

def morse(s) -> dict:
    encoded_string = '';
    for c in s:
        if c.upper() in NESTED_MORSE.keys():
            encoded_string += NESTED_MORSE[c.upper()] + ' '
        else:
            raise AssertionError("the arguments are bad")
    encoded_string = encoded_string.strip()
    print(encoded_string);


if  __name__ == "__main__":
    try:
        if (len(sys.argv) > 2):
            raise AssertionError("the arguments are bad")
        morse(sys.argv[1])
    except AssertionError as e:
        print("AssertionError: " + str(e));