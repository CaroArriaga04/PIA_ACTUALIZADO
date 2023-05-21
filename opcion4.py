def eliminar_frase():
    id_frase=input("Ingrese el ID de la frase que desea eliminar: ")
    for i in range (len(frases)):
        if frases[i]['idfrase']==id_frase:
            frase_eliminada=frases.pop(i)
            print(f"La frase {frase_eliminada['idfrase']} ha sido eliminada")

            guardar_frases(frases)
            return
        print(f"La frase {id_frase} no existe")