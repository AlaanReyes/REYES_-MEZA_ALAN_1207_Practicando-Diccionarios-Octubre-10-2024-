print("Welcome to Practicando Diccionarios Octubre 10 2024!") # Bienvenida al programador 
print(" ")
print("REYES MEZA ALAN EDUARDO_1207 : 3W #NOMBRE PRACTICA Y DATOS DE PROGRAMADOR")
print(" ")
#Diccionario 
#Los diccionarios se utilizan para almacenar valores de datos en pares clave:valor.
#Un diccionario es una colección ordenada*, modificable y que no permite duplicados.
#Creando y desplegando diccionario

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(" ")

#Imprima el valor de "brand" o "marca"  del diccionario:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
print(" ")

#Los valores duplicados sobrescribirán los valores existentes:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(" ")

#Imprima la cantidad de elementos en el diccionario:

#Print the number of items in the dictionary:
print(len(thisdict))


#Tipos de datos de cadena, int, booleanos y de lista:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(" ")
# Imprima el tipo de datos de un diccionario:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
print(" ")

# Usando el método dict() para hacer un diccionario:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

print(" ")

print("MI FAMILIA:")
myfamily = {
  "child1" : {
    "name" : "Alex",
    "year" : 2004
  },
  "child2" : {
    "name" : "Alexandra",
    "year" : 2007
  },
  "child3" : {
    "name" : "Marcos",
    "year" : 2011
  }
}

child1 = {
  "name" : "Alex",
  "year" : 2004
}
child2 = {
  "name" : "Alejandro",
  "year" : 2007
}
child3 = {
  "name" : "Marcos",
  "year" : 2011
}
myfamily = {
"child1" : child1,
"child2" : child2,
"child3" : child3
}
print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

print(" ")

mydict = dict(thisdict)
print(mydict)
d1 = {
  "Nombre": "ALAN",
  "Edad": 16,
  "Numero_E": 1207
}
print(d1)
#{'Nombre': 'Sara', 'Edad': 27, 'numero E.': 1207}

d2 = dict([
     ('Nombre', 'REYES'),
      ('Edad', 16),
      ('Numero_E', 1207),
])
print(d2)
#{'Nombre': 'Sara', 'Edad': '27', 'numero E.': '1207'}

d3 = dict(Nombre='REYES',
          Edad=16,
           Numero_E=1207)
print(d3)
#{'Nombre': 'Sara', 'Edad': 27, 'numero E.': 1207}

print(d1['Nombre'])     #ALAN
print(d2.get('Nombre')) #EDUARDO

print(" ")

monedas = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))
print(" ")

nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])
print(" ")

frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")

print(" ")

curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0
for asignatura, creditos in curso.items():
    print(asignatura, 'tiene', creditos, 'créditos')
    total_creditos += creditos
print('Número total de créditos del curso: ', total_creditos)
print(" ")

cesta = {}
continuar = True
while continuar:
    item = input('Introduce un artículo: ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    cesta[item] = precio
    continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"
coste = 0
print('Lista de la compra')
for item, precio in cesta.items():
    print(item, '\t', precio)
    coste += precio
print('Coste total: ', coste)
print(" ")

clientes = {}
opcion = ''
while opcion != '6':
    if opcion == '1':
        nif = input('Introduce NIF del cliente: ')
        nombre = input('Introduce el nombre del cliente: ')
        direccion = input('Introduce la dirección del cliente: ')
        telefono = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        cliente = {'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':vip=='S'}
        clientes[nif] = cliente
    if opcion == '2':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            del clientes[nif]
        else:
            print('No existe el cliente con el nif', nif)
    if opcion == '3':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            print('NIF:', nif)
            for clave, valor in clientes[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el cliente con el nif', nif)
    if opcion == '4':
        print('Lista de clientes')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'])
    if opcion == '5':
        print('Lista de clientes preferentes')
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'])
    opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')