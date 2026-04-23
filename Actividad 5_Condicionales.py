"""a = 3
if a > 0:
    print('A is a positive number')# A is a positive number
else:
    print('A is a negative number')


a = int(input("Inserta un numero: "))
if a > 0:
    print("El numero es positivo")
elif a < 0:
    print("El numero es negativo")
if a % 2 == 0:
    print("El numero es par")
elif a % 2 != 0:
    print("El numero es impar")
else:
    print("No es par ni impar")


a = 0
if a > 0:
   if a % 2 == 0:
       print('A is a positive and even integer')
   elif:
       print('A is a positive number')
elif a == 0:
   print('A is zero')
else:
   print('A is a negative number')


numero = int(input("Numero: "))
if numero != 0:
    if numero > 0:
        print("El numero es positivo")
        if numero % 2 == 0:
            print("El numero es par")
        else:
            print("El numero es impar")
    else:
        print("El numero es negativo")
        if numero % 2 != 0:
            print("El numero es impar")
        else :
            print("El numero es par")
else:
    print("El numero es cero")"""


#DEBER 
#Ejercicios: Nivel 1
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Tienes la edad suficiente para aprender a conducir.")
else:
    faltan = 18 - edad
    print(f"Necesitas {faltan} años más para aprender a conducir.")

my_age = 18
your_age = int(input("Ingrese su edad: "))

diferencia = abs(my_age - your_age)

if your_age > my_age:
    if diferencia == 1:
        print("Eres 1 año mayor que yo.")
    else:
        print(f"Eres {diferencia} años mayor que yo.")
elif your_age < my_age:
    if diferencia == 1:
        print("Soy 1 año mayor que tú.")
    else:
        print(f"Soy {diferencia} años mayor que tú.")
else:
    print("Tenemos la misma edad.")

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")


#Ejercicios: Nivel 2
puntaje = int(input("Ingrese su puntaje: "))

if 90 <= puntaje <= 100:
    print("A")
elif 80 <= puntaje <= 89:
    print("B")
elif 70 <= puntaje <= 79:
    print("C")
elif 60 <= puntaje <= 69:
    print("D")
else:
    print("F")

mes = input("Ingrese el mes: ").lower()

if mes in ["septiembre", "octubre", "noviembre"]:
    print("Otoño")
elif mes in ["diciembre", "enero", "febrero"]:
    print("Invierno")
elif mes in ["marzo", "abril", "mayo"]:
    print("Primavera")
elif mes in ["junio", "julio", "agosto"]:
    print("Verano")
else:
    print("Mes no válido")

fruits = ['banana', 'orange', 'mango', 'lemon']

fruta = input("Ingrese una fruta: ").lower()

if fruta in fruits:
    print("Esa fruta ya existe en la lista")
else:
    fruits.append(fruta)
    print("Fruta agregada:", fruits)
