###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

# name = input("Hola, como te llamas?\n")
# print(f"Hola {name}")

# city, country = input("En que ciudad y pais vives?\n").split(", ")
# print(f"genial {name}, que lindo es vivir en {city}, {country}.")

# age = int(input("Cuantos años tienes?\n"))
# print(f"Entonces {name}, tienes {age} y vives en {city}, {country}. ¡Qué interesante!")


### Completa aquí

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

cadena = "12345"
print(type(cadena))
print(int(cadena))
print(type(int(cadena)))

### Completa aquí

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

name = "Nico"
age = 31
height = 1.80
city = "Buenos Aires"

print(f"hola {name}, tienes {age} años, mides {height} metros y vives en {city}. Lo se todo")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

PI = 3.14
print(f"el numero redondeado es: {round(PI)}")
print(f"el redondeo de {PI} dividido entre 2 es: {round(PI) // 2}")