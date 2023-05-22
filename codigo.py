from clase import Frase
import clase
print("¡Bienvenido a la aplicacion de frases motivadoras!")

Frase.leer_frase()
while True:
    print("MENU")
    print("1.- Agregar frase")
    print("2.- Ver frase")
    print("3.- Ver frases")
    print("4.- Eliminar frase")
    print("5.- Modificar frase")
    print("6.- Salir")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        clase.agregar_frase()
        Frase.escribir_frase()
    elif opcion == 2:
        clase.mostrar_info()
        Frase.escribir_frase()
    elif opcion == 3:
        clase.mostrar_frases()
        Frase.escribir_frase()
    elif opcion == 4:
        clase.eliminar_frase()
        Frase.escribir_frase()
    elif opcion == 5:
        clase.modificar_frase()
        Frase.escribir_frase()
    elif opcion == 6:
        break