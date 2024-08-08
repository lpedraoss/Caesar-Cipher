
# Ejemplo de uso
from core.caesar_cipher import CaesarCipher

def load_txt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    # Convertir a ASCII, reemplazando caracteres no ASCII con '?'
    ascii_content = content.encode('latin1', 'replace').decode('latin1')
    return ascii_content
def load_cipher(filename):
    with open(filename, 'r', encoding='latin1') as file:
        content = file.read()
    return content
    
def decrypt_text():
    print('Has elegido la opcion de descifrar mensajes')
    print('<-------------------------------------->')
    print('Por favor, ingrese los siguientes datos:')
    print('desea cargar un archivo con el mensaje a descifrar? (y/n): ')
    option = input('> ').strip().lower()
    if option == 'y':
        encrypted_text = load_cipher('data/cipher_text.txt')
        print('Mensaje a descifrar => {}'.format(encrypted_text))
    else:
        print('Inserte el mensaje a descifrar: ')
        encrypted_text = input('> ').strip().lower()
    shift = int(input('Inserte el desplazamiento utilizado para cifrar: '))
    idioma = input('Inserte el idioma (es/en): ').lower()
    alphanumeric = input('¿Incluir números? (y/n): ').strip().lower() == 'y'
    incluir_especiales = input('¿Incluir caracteres especiales? (y/n): ').strip().lower() == 'y'
    cipher = CaesarCipher(idioma, incluir_especiales,alphanumeric)
    #cipher.set_alphabet(idioma, incluir_especiales)
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
        textPlain = load_txt('data/plain.txt').strip().lower()
        print('Mensaje a cifrar => {}'.format(textPlain))
    else:
        textPlain = input('Inserte el mensaje a encriptar: ').strip().lower()
    shift = int(input('Inserte el desplazamiento: '))
    idioma = input('Inserte el idioma (es/en): ').lower()
    alphanumeric = input('¿Incluir números? (y/n): ').strip().lower() == 'y'
    incluir_especiales = input('¿Incluir alphabet especiales? (y/n): ').strip().lower() == 'y'

    print('<-------------------------------------->')
    cipher = CaesarCipher(idioma, incluir_especiales,alphanumeric)
    #cipher.set_alphabet(idioma, incluir_especiales)
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