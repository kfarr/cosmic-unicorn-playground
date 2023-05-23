

# FONT DATA
# x,y are unused - could be used for drawing above below line
# w, h are width and height
# s is spacing
# data is binary bit representation of pixels, starting at top left

font2x5 = {
    " ": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b0000000000},
    "!": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b0101010001},
    "'": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b0100000000},
    ",": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b0000010110},
    "-": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b0000110000},
    ".": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b0000000010},
    "0": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b1111111111},
    "1": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b0101010101},
    "2": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b1101111011},
    "3": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b1101110111},
    "4": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b1010110101},
    "5": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b1110110111},
    "6": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b1010111111},
    "7": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b1101010101},
    "8": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b1111001111},
    "9": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b1111110101},
    ":": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b0001000100},
    ";": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b0001000110},
    "<": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b0001100100},
    "=": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b0011001100},
    ">": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b0010011000},
    "?": {"x": 0, "y": 0, "w": 2, "h": 5, "s": 1, "data": 0b1101111000},
    }

font3x5 = {
            " ": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b000000000000000},
            "🚶": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b010110111010101},
            "✋": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b000010110111110},
            "!": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b010010010000010},
            "0": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111101101101111},
            "1": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b110010010010111},
            "2": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111001111100111},
            "3": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111001011001111},
            "4": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b101101111001001},
            "5": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111100111001111},
            "6": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111100111101111},
            "7": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111001010010010},
            "8": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111101111101111},
            "9": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111101111001111},
            "A": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b010101111101101},
            "B": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b110101110101110},
            "C": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b011100100100011},
            "D": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b110101101101110},
            "E": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111100110100111},
            "F": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111100110100100},
            "G": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b011100101101011},
            "H": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b101101111101101},
            "I": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111010010010111},
            "J": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111010010010110},
            "K": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b101101110101101},
            "L": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b100100100100111},
            "M": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b101111111101101},
            "N": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111101101101101},
            "O": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111101101101111},
            "P": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b110101110100100},
            "Q": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b010101101110011},
            "R": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b110101110101101},
            "S": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b011100010001110},
            "T": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111010010010010},
            "U": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b101101101101111},
            "V": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b101101101101010},
            "W": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b101101111111101},
            "X": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b101101010101101},
            "Y": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b101101111001111},
            "Z": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111001010100111},
            "-": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b000000111000000},
            ":": {"x":0,"y":0,"w":1,"h":5,"s":1,"data":0b01010},
            ".": {"x":0,"y":0,"w":1,"h":5,"s":1,"data":0b00001}
        }


font4x5 = {
            "0": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01101001100110010110},
            "1": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b110010010010111},
            "2": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11100001011110001111},
            "3": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11100001011000011110},
            "4": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b10011001011100010001},
            "5": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11111000111000011110},
            "6": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01111000111010010110},
            "7": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11110001001001000100},
            "8": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01101001011010010110},
            "9": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01101001011100011110},
            "A": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01101001100111111001},
            "B": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11101001111010011110},
            "C": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01111000100010000111},
            "D": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11101001100110011110},
            "E": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11111000111010001111},
            "F": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11111000111010001000},
            "G": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01111000101110010111},
            "H": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b10011001111110011001},
            "I": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111010010010111},
            "J": {"x":0,"y":0,"w":3,"h":5,"s":1,"data":0b111001001001110},
            "K": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b10011010110010101001},
            "L": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b10001000100010001111},
            "M": {"x":0,"y":0,"w":5,"h":5,"s":1,"data":0b1000111011101011000110001},
            "N": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b10011101101110011001},
            "O": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01101001100110010110},
            "P": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11101001100111101000},
            "Q": {"x":0,"y":0,"w":5,"h":5,"s":1,"data":0b0110010010100101011001111},
            "R": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11101001100111101001},
            "S": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b01111000011000011110},
            "T": {"x":0,"y":0,"w":5,"h":5,"s":1,"data":0b1111100100001000010000100},
            "U": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b10011001100110010110},
            "V": {"x":0,"y":0,"w":5,"h":5,"s":1,"data":0b1000110001100010101000100},
            "X": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b10011001011010011001},
            "Y": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b10011001011100011110},
            "Z": {"x":0,"y":0,"w":4,"h":5,"s":1,"data":0b11110001011010001111},
    }


font5x9 = {
    " ": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000000000000000000000000000000},
    "!": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00100001000010000100001000000000100},
    '"': {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01010010100000000000000000000000000},
    "#": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01010010101101100000110110101001010},
    "$": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00100011111000001110000011111000100},
    "%": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b11001110010001000100010001001110011},
    "&": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01000101001010001000101011001001101},
    "'": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b10000100001000000000000000000000000},
    "(": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00100010001000010000100000100000100},
    ")": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00100000100000100001000010001000100},
    "*": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000001001010101110101010010000000},
    "+": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000001000010011111001000010000000},
    ",": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000000000000000110000100010000},
    "-": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000000000011111000000000000000},
    ".": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000000000000000000001100011000},
    "/": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00001000010001000100010001000010000},
    "0": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01110100011000110001100011000101110},
    "1": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00100011000010000100001000010001110},
    "2": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01110100010000101110100001000011111},
    "3": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01110100010000101110000011000101110},
    "4": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00010001100101011111000100001000010},
    "5": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b11111100001111000001000011000101110},
    "6": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01110100001000011110100011000101110},
    "7": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b11111000010001000100010001000010000},
    "8": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01110100011000101110100011000101110},
    "9": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01110100011000101111000010000101110},
    ":": {"x":0,"y":0,"w":2,"h":9,"s":1,"data":0b00111100111100},
    ";": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01100011000000001100011000010001000},
    "<": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00010001000100010000010000010000010},
    "=": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000001111100000111110000000000},
    ">": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01000001000001000001000100010001000},
    "?": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01100100100001000100001000000000100},
    "@": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01110100010000101101101011010101110},
    "A": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00100010101000110001111111000110001},
    "B": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b11110010010100111110010010100111110},
    "C": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01110100011000010000100001000101110},
    "D": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b11110010010100101001010010100111110},
    "E": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b11111100001000011100100001000011111},
    "F": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b11111100001000011100100001000010000},
    "G": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01110100011000010111100011000101110},
    "H": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b10001100011000111111100011000110001},
    "I": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01110001000010000100001000010001110},
    "J": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00111000100001000010000101001001100},
    "K": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b10001100101010011000101001001010001},
    "L": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b10000100001000010000100001000011111},
    "M": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b10001110111010110101100011000110001},
    "N": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b10001110011010110011100011000110001},
    "O": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01110100011000110001100011000101110},
    "P": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b11110100011000111110100001000010000},
    "Q": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01110100011000110001101011001001101},
    "R": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b11110100011000111110101001001010001},
    "S": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01110100011000001110000011000101110},
    "T": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b11111001000010000100001000010000100},
    "U": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b10001100011000110001100011000101110},
    "V": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b10001100011000101010010100010000100},
    "W": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b10001100011000110101101011101110001},
    "X": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b10001100010101000100010101000110001},
    "Y": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b10001100010101000100001000010000100},
    "Z": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b11111000010001000100010001000011111},
    "[": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01110010000100001000010000100001110},
    "\"": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b10000100000100000100000100000100001},
    "]": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00111000010000100001000010000100111},
    "^": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00100010101000100000000000000000000},
    "_": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000000000000000000000000011111},
    "`": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b11000110001000001000000000000000000},
    "a": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000000111000001011111000101110},
    "b": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b10000100001011011001100011100110110},
    "c": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000000011101000010000100000111},
    "d": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00001000010110110011100011001101101},
    "e": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000000111010001111111000001110},
    "f": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00110010010100011110010000100001000},
    "g": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0001110100011000110001011110000101110},
    "h": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b10000100001011011001100011000110001},
    "i": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00100000000110000100001000010001110},
    "j": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000001100001000010000101001001100},
    "k": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b10000100001001010100110001010010010},
    "l": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01100001000010000100001000010001110},
    "m": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000001101010101101011010110101},
    "n": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000001011011001100011000110001},
    "o": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000000111010001100011000101110},
    "p": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01110100011000110001111101000010000},
    "q": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01110100011000110001011110000100001},
    "r": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000001011011001100001000010000},
    "s": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000000111110000011100000111110},
    "t": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00100001000111100100001000010000111},
    "u": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000001000110001100011001101101},
    "v": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000001000110001100010101000100},
    "w": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000001000110001101011010101010},
    "x": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000001000101010001000101010001},
    "y": {"x":0,"y":0,"w":5,"h":10,"s":1,"data":0b0000000000100011000110001011110000101110},
    "z": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00000000001111100010001000100011111},
    "{": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00010001000010001000001000010000010},
    "|": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b00100001000010000000001000010000100},
    "}": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01000001000010000010001000010001000},
    "~": {"x":0,"y":0,"w":5,"h":9,"s":1,"data":0b01000101010001000000000000000000000},
}
