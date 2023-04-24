my_dict = {}

print(type(my_dict))

my_dict = {
    'name' : 'Facundo',
    'lastName': 'Peralta',
    'Age': 27
}

print(my_dict)

print(len(my_dict))

#Operaciones con los diccionarios.

print(my_dict['name'])
print(my_dict['lastName'])
print(my_dict['Age'])
print(my_dict.get('asdaf')) #con get evitamos que el programa tire error.

print('avion' in my_dict)
print('name' in my_dict)


# inserccion y actualizacion

persona = {
    'name' : 'Facundo',
    'lastName' : 'Peralta',
    'lang': ['python', 'JavaScript'],
    'age' : 27
}
print(persona)

persona['name'] = 'Ezequiel'
persona['age'] -= 2
persona['lang'].append('Voy a aprender Go') #puedo usar métodos de listas cuando es una lista lo que está dentro del diccionario
print(persona)

del persona['lastName']

print(persona)

persona.pop('age')

print(persona)

#metodos utiles de los diccionarios:
#obtener los items del diccionario 
print('Aca imprime los items=> ')
print(persona.items())
#o también puedo obtener las keys
print('Aca imprime los keys => ')
print(persona.keys())






