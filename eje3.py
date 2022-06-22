# Elaborar un Programa que solicite dos numeros y determine cual es el mayor y cual el menor o si son iguales.
numero_uno = float(input('Escribe un Numero: '))
numero_dos = float(input('Escribe otro Numero: '))

if(numero_uno > numero_dos):
    print(numero_uno, 'Es mayor que', numero_dos)
elif(numero_uno == numero_dos):
    print(numero_uno, ' y ', numero_dos, 'Son Iguales')
else:
    print(numero_dos, 'Es mayor que', numero_uno)