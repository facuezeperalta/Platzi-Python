name = 'Facundo'
last_name = 'Peralta'

print (name)
print (last_name)


full_name = print(name + ' ' + last_name)
full_name1 = name + " " + last_name 

template = "Hola me llamo {}".format(full_name)

print (template)
#esta es la mejor forma para poner format en un string.
templateV2 = f"Me nombre es {name} y mi apellido es {last_name} y mi nombre completo es {full_name1}"
print (templateV2)

print (type(name))

