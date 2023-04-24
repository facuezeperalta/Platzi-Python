#Estructura de datos super usada en python.
numbers = [1,2,3,4,5,6,7,8,9,10]
task = ['make a dishes', 'play video games']
print (numbers)
print (type(numbers))
print (task)
print(type(task[0]))

text = 'hola'

task[0] = 'do the dishes'

print (task)

print (numbers[:3])
print (numbers[1:3])

print(True in task)

#métodos de listas

#CRUD

#crear
numeros = [1,2,3,4,5]

#leer
print (numeros[0])

#update
numeros.append(10) #agrega al final.
print (numeros)

numeros.insert(0,500) #primer argumento posicion y segundo el valor que quiero insertar

print (numeros)

#fusionar listas

tareas = ['t1','t2','t3']

new_list = numeros + tareas

print(new_list)

print(new_list.index('t2'))

index = new_list.index('t2')

new_list[index] = 'to do chaged'

print(new_list)


#eliminar
new_list.remove('t1')

print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

#ordenar las listas
#ponerla en reversa
new_list.reverse()
print(new_list)

#sort

numbers2 = [1,4,5,6,8]

numbers2.sort()
print(numbers2)

#ordenar strings

listadeStrings = ['Facundo','Perlata','Abel']

listadeStrings.sort()

print(listadeStrings)










