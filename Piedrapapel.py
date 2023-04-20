#Proyecto de piedra papel o tijera.
import random
elementos = ['piedra','papel','tijera']

userOption = input('piedra, papel o tijera =>')

computerOption = random.choice(elementos)

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
    


print ('*'*10)
print ('la computadora elijio: ', computerOption)