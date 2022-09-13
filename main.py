
import random
import time

puntaje = random.randint(0, 10)

iniciar_trivia = True 
intentos = 0
puntaje = 0

print("\033[34m Bienvenido a trivia sobre ciberseguridad \033[39m")
print(" \033[34m Pondremos a prueba tus conocimientos \033[39m")
print('Inicias con', puntaje, 'puntos')

BLACK = '\033[30m'
RED = '\033[310m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[38m'

nombre = input(GREEN+'\nIngresa tu nombre: '+RESET)

print(BLUE+'\n Hola', nombre, "Responder las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+RESET)
print ('Hola', nombre, 'iniciamos en 3 segundos...')
time.sleep(3)
print('Lindo nombre', nombre)



print("1) ¿Que es es un ataque DDoS?")
print(YELLOW+"a) un ataque de denegación")
print("b) ataque distribuido de denegación de servicio")
print("c) una versión distribuida")
print("d) un grupo de personas o automatismos atacan a un servidor"+RESET)


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

  
  

print("\n¿Que es Kali Linux?")
print("a) Un sistema Operativo basado en Debian")
print("b) Un sistema Operativo usado por Pentesting")
print("c) Un Browser de linux")
print("d) Una distribucion basada en debian GNU/Linux")
print("e) Un Kernel")

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

print('Iniciamos a jugar con los numeros')
print('\nHola', nombre, "Puedes ralizar tus operaciones aqui:\n"
)

num1 = int(input('Ingrese el 1 numero: '))
num2 = int(input('Ingrese el 2 numero: '))
op = input('Ingrese la operacion: ')
if op == '+':
  print('Resultado: ', num1+num2)
elif op == '-':
  print('Resultado', num1-num2)
elif op == '*':
  print('Rsultado: ', num1*num2)
elif op == '/':
  print('Resultado: ', num1/num2)

def ejercicio1():
  x = int(input("\nIngrese el primer numero: "))
  y = int(input("Ingrese el segundo numero: "))
  print((x+y)/2)
 
def ejercicio2():
  x = int(input("Ingrese el primer numero: "))
  y = int(input("Ingrese el segundo numero: "))
  print(x**y)

def ejercicio3():
  x = int(input("Ingrese el numero: "))
  print(x**(1/2))

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

x = int(input('Ingrese el numero: '))
x = x * x
if x >= 0:
  print('El numero es positvo')
else:
  print('El numero es negativo')

x = int(input('Primer numero: '))
y = int(input('Segundo numero: '))
if x > y:
  print('El numero', x, 'es mayor')
else:
  print('El numero', y, 'es mayor')

print(GEEN+'\nJuega un momento con los numeros', nombre+RESET)
z = input('\nIngresa la palabra: ')
x = int(input('Numero de veces: '))
y = 0
while y < x:
  print(z)
  y = y + 15

print('Jugemnos un momento con las filas de sginos, formados figuras ')
x = int(input('numero de filas: '))
y = 0
while y <= x:
  z = 0
  while z < y:
    print('+', end = '')
    z = z + 1
  print('')  
  y = y + 1
  


print('\n¿Deseas intentar nuevamente mi Trivia?')
repetir_trivia = input('Ingresa <si> para repetir, o cualquier tecla para finalizar: ').lower()

if repetir_trivia != 'si':
  print('\nEspero {nombre} que lo hayas pasdo bien, hsta pronto!')

print('Gracias!', nombre, 'por jugar mi trivia, alcanzaste', puntaje, 'puntos')