text = 'Ella sabe python'
#indexing es que los textos tiene un indicador a nivel de posicioes.
print(text[0])
print(text[1])
print(text[5])
print(text[-1])

size = len(text)

print('Tamaño => ',size)

print(text[size-1]) #Se pone menos uno para re acomodar el index con el tamaño.

#pero poniendo -1 se soluciona
print(text[-1])


#slicing
print(text[::-1]) #Imprime al revés el texto.
print(text[0:10]) #desde el cominezo hasta el carracter indicado, sino tiene nada arranca en el comienzo del texto hasta donde le coloquemos el segundo argumento.

print(text[5:]) 

print(text[10:16:2])

