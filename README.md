Cifrado César
El cifrado César es una técnica de cifrado simple en la que cada letra del texto plano se desplaza un número fijo de posiciones en el alfabeto. Por ejemplo, con un desplazamiento de 3, la letra A se convierte en D, la B en E, y así sucesivamente. Este método es uno de los tipos más antiguos y básicos de cifrado, utilizado por Julio César en sus comunicaciones privadas.

Características del Cifrado César
Simplicidad: Es fácil de entender e implementar.
Desplazamiento fijo: Utiliza un desplazamiento fijo para todas las letras del texto.
Vulnerabilidad: Es vulnerable a ataques de fuerza bruta y análisis de frecuencia debido a su simplicidad.
Fórmula Matemática
Para cifrar una letra en el cifrado César, se utiliza la siguiente fórmula:

[ C = (P + K) \mod 26 ]

Donde:

( C ) es la letra cifrada.
( P ) es la letra del texto plano.
( K ) es el número de posiciones de desplazamiento.
( \mod 26 ) asegura que el resultado se mantenga dentro del rango del alfabeto.
Para descifrar, se utiliza la fórmula inversa:

[ P = (C - K) \mod 26 ]

Ejemplo
Si queremos cifrar el texto "HELLO" con un desplazamiento de 3:

H se convierte en K
E se convierte en H
L se convierte en O
L se convierte en O
O se convierte en R
El texto cifrado sería "KHOOR".

Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar. ```