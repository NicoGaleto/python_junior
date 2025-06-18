# print("Hola Mundo")
a = 10 
b = 25
c = a + b
print("El resultado de la suma es:", c)

print ("""hola rey, que esta pasando 
       esto me parece que esta copado. 
       muy copado""")

print ("int:")
print (type(10))
print (type(10.55))

print ("hola" + str(   50))

my_name = "Nico"
age = 30

print(f"hola  mi nombre es {my_name}, tengo {age} y soy de buenos aires")

name, age, city = "Nico", 31, "Buenos Aires" 

print(type(name))
print(type(age))
print(type(city))

print(f"hola, soy {name}, tengo {age} años, me gusta el futbol y soy de {city}!")

name = input("hola, como te llamas?\n")
print(f"hola {name}, encantado de conocerte!")

age = int(input("cuantos años tenes?\n"))
print(f"hola, tengo {age} años y en unos dias cumplo {age + 1} años!")

country, city = input("en que pais y ciudad vives?\n").split()
print(f"vivo en {city}, {country} hace 8 años")