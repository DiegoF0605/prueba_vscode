print('Hola terrícolas')

x = 0
y = 13
if x < y:
    print('x es menor que y')

if x > y:
    print('x es mayor que y')

if x == y:
    print('x es igual que y')
    j = 90

if x < y:
    print('x es menor que y')

else:
    print('x no es menor que y')


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años.')
