#Importamos la libreria ramdom
import random
#Para implementar puntajes, crearemos una nueva vaiable llamada 'puntaje', la que inicializamos en 0.
puntaje = random.randint(0, 10)

#Para implementar puntajes, crearemos una nueva vaiable llamada 'puntaje', la que inicializamos en 0.

puntaje = 0
#Agregamos perzonalizacion para nuestros jugadores, pregutando y almacenado sus nombres en una bariable
nombre = input('Ingresa tu nombre: ')


# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia

print("Bienvenido a trivia sobre ciberseguridad")
print("Pondremos a prueba tus conocimientos")
print('Tienes', puntaje, 'puntos')

#Agregamos perzonalizacion para nuestros jugadores, pregutando y almacenado sus nombres en una variable
nombre = input('Ingresa tu nombre: ')

# Es importante dar instrucciones sobre cómo jugar
# Ahora, lo personalizaremos con el nombre del jugador, diciendole a print() que muestre el contenido de la variable 'nombre'.  Cada cosa distinta que queremos que nos muestre en la pantlla, la separamos con comas
print('\n Hola', nombre, "Responder las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"
)

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

# Pregunta 1
print("1) ¿Que es es un ataque DDoS?")
print("a) un ataque de denegación")
print("b) ataque distribuido de denegación de servicio")
print("c) una versión distribuida")
print("d) un grupo de personas o automatismos atacan a un servidor")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\nTu respuesta: ")
if respuesta_1 == 'x':
  print('Nunca te rindas!')

while respuesta_1 not in ('a', 'b', 'c', 'd'):
  respuesta_1 = input('debes responder a, b, c, o d. Ingresa nuevamente tu respuesta: ')
if respuesta_1 == 'a':
  puntaje -= 4
  puntaje = random.randint(0, 10)
  print('Incorrecto', nombre, 'No es un ataque de denegación')
elif respuesta_1 == 'c':
  puntaje -= 4
  puntaje = random.randint(0, 10)
  print('Incorrecto', nombre, 'No es una versión distribuida')
elif respuesta_1 == 'd':
  puntaje -= 4 
  puntaje = random.randint(0, 10)
  print('Incorrecto', nombre, 'No es un grupo de personas o automatismos atacan a un servidor')
else:
  puntaje += 10
  puntaje = random.randint(0, 10)
  print('Muy bien!', nombre, 'Tienes', puntaje, 'Puntos!')

  
  
#Pregunta 2
print("\n¿Que es Kali Linux?")
print("a) Un sistema Operativo basado en Debian")
print("b) Un sistema Operativo usado por Pentesting")
print("c) Un Browser de linux")
print("d) Una distribucion basada en debian GNU/Linux")
print("e) Un Kernel")
#Almacenamos la respuesta usuario en la variable respuesta_2
respuesta_2 = input("\nTu Respuesta: ")
if respuesta_2 == 'x':
  print('Nunca te rindas!')
while respuesta_2 not in('a', 'b', 'c', 'd'):
  respuesta_2 = input('Debes responder a, b ,c ,d. Ingresa nuevamente la respuesta: ')
  
if respuesta_2 == 'a':
  puntaje -= 4
  puntaje = random.randint(0, 10)
  print('Incorrecto!', nombre, 'Un sistema Operativo basado en Debian')
  puntuje = puntaje /4
elif respuesta_2 == 'b':
  puntaje -= 4
  puntaje = random.randint(0, 10)
  print('Incorrecto', nombre, 'n sistema Operativo usado por Pentesting')
elif respuesta_2 == 'c':
  puntaje -= 4
  puntaje = random.randint(0, 10)
  print('Incorrecto', nombre, 'Un Browser de linux')
else:
  puntaje += 10
  puntaje = random.randint(0, 10)
  print('Muy bien!', nombre, 'tienes', puntaje,  'puntos!')
#Pregunta 3
print('\nHola', nombre, "Puedes ralizar tus operaciones aqui:\n"
)

num1 = int(input('Ingrese el numero'))
num2 = int(input('Ingrese el numero: '))
op = input('Ingrese la operacion: ')
if op == '+':
  print('Resultado: ', num1+num2)
elif op == '-':
  print('Resultado', num1-num2)
elif op == '*':
  print('Rsultado: ', num1*num2)
elif op == '/':
  print('Resultado: ', num1/num2)
#Pregunta 4
def ejercicio1():
  x = int(input("Ingrese el primer numero: "))
  y = int(input("Ingrese el segundo numero: "))
  print((x+y)/2)
  #Pregunta 5
def ejercicio2():
  x = int(input("Ingrese el primer numero: "))
  y = int(input("Ingrese el segundo numero: "))
  print(x**y)
#Pregunta 6
def ejercicio3():
  x = int(input("Ingrese el numero: "))
  print(x**(1/2))
#Ejercicio 7
def ejercicio4():
  x = int(input("Ingrese el primer numero: "))
  y = int(input("Ingrese el segundo numero: "))
  print((x**2+ y**2)**(1/2))
print("Ingrese numero de ejercicio: ")
num = int(input())
if num == 1:
  ejercicio1()
elif num == 2:
  ejercicio2()
elif num == 3:
  ejercicio3()
elif num == 4:
  ejercicio4()
  

  print('Gracias!', nombre, 'por jugar mi trivia, alcanzaste', puntaje, 'puntos')