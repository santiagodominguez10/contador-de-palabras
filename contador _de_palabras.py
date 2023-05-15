import csv
import string

translator = str.maketrans('', '', string.punctuation)

# Pedimos los datos personales al usuario
nombre = input("Ingrese su nombre 🖊 : ")
apellido = input("Ingrese su apellido 🖊 : ")
dni = input("Ingrese su DNI 🖊 : ")

# Pedimos el texto al usuario
texto = input("Ingrese el texto 🗒 : ")

# Contamos las palabras del texto
word_count = {}
words = texto.split()
for word in words:
    word = word.translate(translator).lower()
    count = word_count.get(word, 0)
    count += 1
    word_count[word] = count

num_palabras = len(words)

# Guardamos los datos en un archivo CSV
with open('datos_personales.csv', mode='w') as output_file:
    writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Nombre', 'Apellido', 'DNI'])
    writer.writerow([nombre, apellido, dni])

# Mostramos el resultado al usuario
print(f"Muchas gracias❗❗, {nombre} {apellido}, por insertar tu texto 🗒. Tu texto tiene... {num_palabras} palabras.")
