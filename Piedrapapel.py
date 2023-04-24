#Proyecto de piedra papel o tijera.
import random
elementos = ('piedra','papel','tijera')

userOption = input('piedra, papel o tijera => ')

userOption = userOption.lower()

while userOption not in elementos:
    print ('La opcion ingresada no es válida, intente nuevamente')
    userOption = input('Ingresa una de estas => piedra, papel o tijera => ')


computerOption = random.choice(elementos)

print('User option =>',userOption)
print('Computer option =>',computerOption)

""" print (computerOption) """

if userOption == computerOption:
    print ('Es un empate')

elif userOption == 'piedra':
    if computerOption == 'tijera':
        print ('Piedra gana a tijera')
        print ('Tu ganas')
        
    else:
        print ('Papel gana a piedra')
        print ('gana la maquina')
elif userOption == 'papel':
    if computerOption == 'piedra':
        print ('Papel gana a la piedra')	
        print ('Tu ganas!')

    else:
        print ('Tijera corta al papel')
        print ('Gana la maquina')
elif userOption == 'tijera':
    if computerOption == 'papel':
        print('tijera corta al papel')
        print('Tu ganas')
    
    else:
        print ('Piedra gana a tijera')
        print ('Gana la Maquina')

else:
    print ('La opción ingresada no es correcta')
    


print ('*'*10)
print ('la computadora elijio: ', computerOption)