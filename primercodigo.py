
MiEdad = 22
EdadDeMiMama = 48
print("La diferencia entre las edades es: ",EdadDeMiMama - MiEdad, "años")

resultado = "La diferencia entre las edades es: " + str(EdadDeMiMama-MiEdad) + " años"
resultado2 = f"La diferencia entre las edades es: {EdadDeMiMama-MiEdad} años"
print (resultado)
print (resultado2)

#paso 1: pedir la edad de la persona numero 1
edadPersona1 = input("Por favor ingrese la edad de la primera persona: ")
#paso 2: pedir la edad de la persona numero 2
edadPersona2 = input("Por favor ingrese la edad de la segunda persona: ")
#paso 3: calcular la diferencia en las edades
diferenciaDeEdad = int(edadPersona1) - int(edadPersona2)
#paso 4: imprimir la diferencia en las edades
print (f'la diferencia en las edades es de {diferenciaDeEdad} años')

inputNumerico = int(input("Por favor ingerese un número: "))
print(inputNumerico)
