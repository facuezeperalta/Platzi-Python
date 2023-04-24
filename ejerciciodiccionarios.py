person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}
person['twitter'] = '@nicobytes'
person['name'] = 'Felipe'
person.pop('age')

print(list(person.keys())) #list se usa para convertir tuplas en listas NO Olvidar

print(list(person.values()))
