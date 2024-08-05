class CaesarCipher:
    """
    Class representing a Caesar Cipher encryption and decryption algorithm.
    Args:
        idioma (str, optional): The language to use for the cipher. Defaults to 'es'.
        especial (bool, optional): Whether to include special characters and numbers in the cipher. Defaults to False.
    Attributes:
        alphabet (dict): The alphabet used for the cipher.
        alphabet_en (dict): The English alphabet.
        alphabet_es (dict): The Spanish alphabet.
        especial_en (dict): Special characters and numbers in English.
        especial_es (dict): Special characters and numbers in Spanish.
        numbers_en (dict): Numbers in English.
        numbers_es (dict): Numbers in Spanish.
        modulus (int): The modulus used for the cipher.
        indices (dict): A dictionary mapping indices to characters in the alphabet.
    Methods:
        set_alphabet(idioma, especial): Sets the alphabet based on the language and special character options.
        encrypt(text, shift): Encrypts the given text using the specified shift value.
        decrypt(encrypted_text, shift): Decrypts the given encrypted text using the specified shift value.
    """
    def __init__(self, idioma='es', especial=False):
        """
        Initializes the CaesarCipher object.

        Parameters:
        - idioma (str): The language to use for the cipher. Default is 'es' (Spanish).
        - especial (bool): Whether to include special characters in the cipher. Default is False.

        Returns:
        None
        """
        self.alphabet = None
        self.alphabet_en = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        self.alphabet_es = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'ñ': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        self.especial_en = {
            "!": 26, "@": 27, "#": 28, "$": 29, "%": 30, "^": 31, "&": 32, "*": 33,
            "(": 34, ")": 35, "-": 36, "_": 37, "+": 38, "=": 39, "{": 40, "}": 41,
            "[": 42, "]": 43, ":": 44, ";": 45, "'": 46, "\"": 47, "<": 48, ">": 49,
            ",": 50, ".": 51, "/": 52, "\\": 53, "|": 54, "?": 55, "~": 56, "`": 57, " ": 58
        }
        self.especial_es = {
            "¡": 27, "¿": 28, "!": 29, "?": 30, "@": 31, "#": 32, "$": 33, "%": 34, "&": 35,
            "*": 36, "(": 37, ")": 38, "-": 39, "_": 40, "+": 41, "=": 42, "{": 43,
            "}": 44, "[": 45, "]": 46, ":": 47, ";": 48, "'": 49, "\"": 50, "<": 51,
            ">": 52, ",": 53, ".": 54, "/": 55, "\\": 56, "|": 57, "^": 58, "~": 59,
            "`": 60, " ": 61
        }
        self.numbers_en = {
            '0': 59, '1': 60, '2': 61, '3': 62, '4': 63, '5': 64, '6': 65, '7': 66, '8': 67, '9': 68
        }
        self.numbers_es = {
            '0': 62, '1': 63, '2': 64, '3': 65, '4': 66, '5': 67, '6': 68, '7': 69, '8': 70, '9': 71
        }
        self.set_alphabet(idioma, especial)

    def set_alphabet(self, idioma, especial):
        """
        Sets the alphabet based on the specified language and special character flag.

        Parameters:
            idioma (str): The language to set the alphabet for. Valid values are 'en' for English and 'es' for Spanish.
            especial (bool): Flag indicating whether to include special characters in the alphabet.

        Returns:
            None
        """
        if idioma == 'en':
            self.alphabet = self.alphabet_en
            if especial:
                self.alphabet.update(self.especial_en)
                self.alphabet.update(self.numbers_en)
        elif idioma == 'es':
            self.alphabet = self.alphabet_es
            if especial:
                self.alphabet.update(self.especial_es)
                self.alphabet.update(self.numbers_es)
        else:
            self.alphabet = self.alphabet_es
            if especial:
                self.alphabet.update(self.especial_es)
                self.alphabet.update(self.numbers_es)
        self.modulus = len(self.alphabet)
        self.indices = {v: k for k, v in self.alphabet.items()}

    def encrypt(self, text, shift):
        """
        Encrypts the given text using the Caesar cipher algorithm.
        Parameters:
        - text (str): The text to be encrypted.
        - shift (int): The number of positions to shift each character.
        Returns:
        - encrypted_text (str): The encrypted text.
        Example:
        cipher = CaesarCipher()
        encrypted_text = cipher.encrypt("Hello, World!", 3)
        print(encrypted_text)
        # Output: "Khoor, Zruog!"
        """
        encrypted_text = ''
        for char in text:
            if char in self.alphabet:
                new_index = (self.alphabet[char] + shift) % self.modulus
                encrypted_text += self.indices[new_index]
            else:
                encrypted_text += char
        with open('data/cipher_text.txt', 'w') as file:
            file.write(encrypted_text)
            
        return encrypted_text

    def decrypt(self, encrypted_text, shift):
        """
        Decrypts the given encrypted text using the Caesar cipher algorithm.

        Parameters:
        - encrypted_text (str): The text to be decrypted.
        - shift (int): The number of positions to shift each character.

        Returns:
        - decrypted_text (str): The decrypted text.

        """
        decrypted_text = ''
        for char in encrypted_text:
            if char in self.alphabet:
                new_index = (self.alphabet[char] - shift) % self.modulus
                decrypted_text += self.indices[new_index]
            else:
                decrypted_text += char
        with open('data/decipher_text.txt', 'w') as file:
            file.write(decrypted_text)
        return decrypted_text