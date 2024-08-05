
# Ejemplo de uso
from core.caesar_cipher import CaesarCipher
def load_cipher_text(path=None):
    with open(path, 'r') as file:
        return file.read()
    
def decrypt_text():
    print('Has elegido la opcion de descifrar mensajes')
    print('<-------------------------------------->')
    print('Por favor, ingrese los siguientes datos:')
    print('desea cargar un archivo con el mensaje a descifrar? (y/n): ')
    option = input('> ').strip().lower()
    if option == 'y':
        encrypted_text = load_cipher_text('data/cipher_text.txt')
        print('Mensaje a descifrar => {}'.format(encrypted_text))
    else:
        print('Inserte el mensaje a descifrar: ')
        encrypted_text = input('> ').strip().lower()
    shift = int(input('Inserte el desplazamiento utilizado para cifrar: '))
    idioma = input('Inserte el idioma (es/en): ').lower()
    incluir_especiales = input('¿Incluir caracteres especiales? (y/n): ').strip().lower() == 'y'
    cipher = CaesarCipher(idioma, incluir_especiales)
    cipher.set_alphabet(idioma, incluir_especiales)
    mssg = cipher.decrypt(encrypted_text, shift)
    print('<-------------------------------------->')
    print(f'Texto descifrado:')
    print('{}'.format(mssg))

def cipher_text():
    print('Has elegido la opcion de cifrar mensajes')
    print('<-------------------------------------->')
    print('Por favor, ingrese los siguientes datos:')
    print('desea cargar un archivo con el mensaje a cifrar? (y/n): ')
    option = input('> ').strip().lower()
    if option == 'y':
        textPlain = load_cipher_text('data/plain.txt').strip().lower()
        print('Mensaje a cifrar => {}'.format(textPlain))
    else:
        textPlain = input('Inserte el mensaje a encriptar: ').strip().lower()
    shift = int(input('Inserte el desplazamiento: '))
    idioma = input('Inserte el idioma (es/en): ').lower()
    incluir_especiales = input('¿Incluir alphabet especiales? (y/n): ').strip().lower() == 'y'

    print('<-------------------------------------->')
    cipher = CaesarCipher(idioma, incluir_especiales)
    cipher.set_alphabet(idioma, incluir_especiales)
    c = cipher.encrypt(textPlain, shift)
    print('Texto cifrado:')
    print('{}'.format(c))
    
def caesar_CLI():
    print('1. Cifrar texto')
    print('2. Descifrar texto')
    print('Seleccione una opción: ')
    option = input('> ')
    if option == '1':
        cipher_text()
    elif option == '2':
        decrypt_text()
    else:
        print('Opción no válida')