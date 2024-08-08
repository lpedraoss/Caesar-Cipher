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
    def __init__(self, idioma='es', especial=False,numbers=False):
        """
        Initializes the CaesarCipher object.

        Parameters:
        - idioma (str): The language to use for the cipher. Default is 'es' (Spanish).
        - especial (bool): Whether to include special characters in the cipher. Default is False.

        Returns:
        None
        """
        
        self.alphabet = None
        self.alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
        self.alphabet_es = 'abcdefghijklmnñopqrstuvwxyz'
        self.especial_en = "!@#$%^&*()-_+={}[]:;'\"<>,./\\|?~` "
        self.especial_es = "¡¿!?@#$%&*()-_+={}[]:;'\"<>,./\\|^~` "
        self.alphanumeric = '0123456789'
        self.set_alphabet(idioma, especial,numbers)

    def set_alphabet(self, idioma, especial,numbers=False):
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
                self.alphabet += self.especial_en
            if numbers:
                self.alphabet += self.alphanumeric
        elif idioma == 'es':
            self.alphabet = self.alphabet_es
            if especial:
                self.alphabet += self.especial_es
            if numbers:
                self.alphabet += self.alphanumeric
        else:
            self.alphabet = self.alphabet_es
            
        self.alphabet = {char: i for i, char in enumerate(self.alphabet)}


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