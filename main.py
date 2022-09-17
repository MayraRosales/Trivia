import time
import random  

# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.
puntaje = random.randint(0, 15)

#Bienvenidos a la trivia
print ('Bienvenido a la trivia de Cultura General')
print ('Prodremos a prueba tus conocimientos')

#Agregaremos personalización consultando nombre
nombre = input('\nIngresa tu nombre: ')

print('\nHola',nombre, 'responde las siguientes preguntas escribiendo la letra de la alternativa y presionando "Enter" para enviar tu respuesta.\n')

#Preguntas y respuestas
print('1) ¿Quién escribio la obra La Metamorfosis?')
print('a) Franz Kafka')
print('b) Luffy')
print('c) Pedro Castillo')
print('d) Jorgito')

# Respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input('\nTu respuesta: ')

#Condicional While
while respuesta_1 not in ('a', 'b', 'c', 'd','x'):
  respuesta_1 = input('Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ')

#condicional if/elif/else para verificar respuesta
if respuesta_1 == 'b':
  print('Incorrecto!', nombre, ',Luffy')
elif respuesta_1 == 'c':
  print('Incorrecto!', nombre, ', Pedro Castillo es el presidente del Perú')
elif respuesta_1 == 'd':
  print('Incorrecto!', nombre, ',Jorgito es un comediante de youtube')
elif respuesta_1 == 'x':
  print(nombre,'Este es un mensaje secreto')
else:
  puntaje = puntaje + 10
  print('Perfecto', nombre, '!')
  
time.sleep(2) # Espera 2 segundos antes de continuar.
# Pregunta 2
print ('\n1) ¿En que país se encuentra la Isla de Pascua?')
print ('a) Perú')
print ('b) Bolivia')
print ('c) Ecuador')
print ('d) Chile')

# Almacenamos la rspuesta del usuario en la variable "respuesta_2"
respuesta_2 = input('\nTu respuesta: ')

while respuesta_2 not in ('a', 'b', 'c', 'd'):
  respuesta_2 = input ('Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ')

# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_2 == 'a':
  print ('Incorrecto!', nombre, 'Perú')
elif respuesta_2 == 'b':
  print ('Incorrecto!', nombre, 'Bolivia')
elif respuesta_2 == 'c':
  print ('Incorrecto!', nombre, 'Ecuador')
else:
  puntaje += 10
  print ('Genial', nombre, '!')

# Pregunta 3
print ('\n1) ¿Quien canto por primera vez el Himno Nacional del Perú?')
print ('a) Suneo')
print ('b) Rosa Merino')
print ('c) Doraemon')
print ('d) Novita')

# Almacenamos la respuesta del usuario en la variable "respuesta_3"
respuesta_3 = input('\nTu respuesta: ')

while respuesta_3 not in ('a', 'b', 'c', 'd'):
  respuesta_3 = input ('Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ')

if respuesta_3 == 'a':
  print ('Totalmente incorrecto! ...')
  puntaje = puntaje / 2
elif respuesta_3 == 'd':
  print ("...")
  puntaje = puntaje + 5
elif respuesta_3 == 'c':
  print ('Incorrecto! ...')
  puntaje = puntaje - 5
else:
  print ('Impresionante! ...')
  puntaje = puntaje * 2

#Pregunta 4
pregunta_4 = print('4) ¿Cúal no fue un prócer de la independencia?')
print('a) María Parado de Bellido')
print('b) Micaela BAstidas Puyucahua')
print('c) José Gabriel Condorcanqui')
print('d) Ricardo Mendoza')

respuesta_4 = 'd'

time.sleep(1)
#Puntaje obtenido
print('Gracias', nombre,'por juegar la trivia de Cultura General, alcanzaste', puntaje,'puntos')