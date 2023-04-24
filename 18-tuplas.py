#las tuplas son inmutables
numbers = (1,2,3,4,5,6,7)
strings = ['Facundo','Ezequiel','Perala']

print ('0=> ',numbers[0])
print ('-1=> ',numbers[-1])

#En las tuplas se puede solamente declarar y leer nada mas. NO SE PUEDEN ACTUALIZAR LOS DATOS.
print(strings.index('Facundo'))
print(type(strings))
my_List = list(strings)
print(type(my_List))