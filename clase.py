frases = []
idfrases = set()
calificaciones = []

class VFrase:
    def __init__(self, idfrase, texto_frase, autor):
        self.idfrase = idfrase
        self.texto_frase = texto_frase
        self.autor = autor

class Frase:
    def calificaciones_prom(self):
        print(self.sacar_promedio())

    def mostrar_info_frase(self):
        (promedio, count, p1, p2, p3, p4, p5) = self.sacar_promedio()
        print(f"ID de la frase: {self.idfrase}")
        print(f"Texto: {self.texto_frase}")
        print(f"Autor: {self.autor}")
        print(f"Calificacion: {promedio}")
        print(f"{count} Calificaciones globales")
        print(f"5 estrellas: {p5}%")
        print(f"4 estrellas: {p4}%")
        print(f"3 estrellas: {p3}%")
        print(f"2 estrellas: {p2}%")
        print(f"1 estrellas: {p1}%")

    def ReadFrase():
        with open("Frases.txt", "r", encoding="utf8") as xd:
            for linea in xd:
                idfrase, texto_frase, autor = linea.strip().split(",")
                frase = VFrase(idfrase, texto_frase, autor)
                frases.append(frase)

    def WriteFrase():
        with open("Frases.txt", "w", encoding="utf8") as amlo:
            for frase in frases:
                amlo.write(f"{frase.idfrase},{frase.texto_frase}, {frase.autor}\n")

    def sacar_promedio(self):
        total = 0
        count = len(self.calificaciones)
        promedio = 0
        v1 = 0
        v2 = 0
        v3 = 0
        v4 = 0
        v5 = 0
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        p5 = 0
        for stars_calif in self.calificaciones:
            if stars_calif == 1:
                v1 += 1
            if stars_calif == 2:
                v2 += 1
            if stars_calif == 3:
                v3 += 1
            if stars_calif == 4:
                v4 += 1
            if stars_calif == 5:
                v5 += 1
            total += stars_calif
        if total > 0:
            p1 = round((100 / count) * v1, 2)
            p2 = round((100 / count) * v2, 2)
            p3 = round((100 / count) * v3, 2)
            p4 = round((100 / count) * v4, 2)
            p5 = round((100 / count) * v5, 2)
            promedio = round(total / count, 2)
        return promedio, count, p1, p2, p3, p4, p5

def agregar_frase():
    idfrase=input("Ingrese el ID de la frase: ")
    if idfrase in idfrases:
        print("Lo sentimos, ese ID ya existe, intente con otro por favor.\n")
        return
    
    texto_frase=input("Ingrese la frase: ")
    autor=input("Ingrese el nombre del autor de la frase: ")
    frase=VFrase(idfrase,texto_frase,autor)
    frases.append(frase)
    idfrases.add(idfrase)
    print("¡Frase agregada exitosamente!")

    Frase.WriteFrase() #escribir las frases nuevas en el archivo

def mostrar_info():
    idfrase = input("Ingrese el id de la frase: ")
    frase_encontrada = False
    
    for frase in frases:
        if frase.idfrase == idfrase:
            op = input("Desea calificar esta frase S/N: ")
            if op.upper() == "S":
                stars_calif = int(input(f"Ingresa la calificacion que le das a la frase (1 a 5): "))
                calificaciones.append(stars_calif)
                print("Calificacion agregada con exito!")
            frase_encontrada = True
            break
    if not frase_encontrada:
        print("No existe una frase con el id ingresado")

def mostrar_frases():
    if len(frases) == 0:
        print("No hay frases registradas.")
    else:
        print("Información de todas las frases:")
        for frase in frases:
            frase.mostrar_info_frase()

def eliminar_frase():
    id_frase=input("Ingrese el ID de la frase que desea eliminar: ")
    frase_encontrada=False
    for i in range (len(frases)):
        if frases[i].idfrase==id_frase:
            frase_eliminada=frases.pop(i)
            print(f"La frase {frase_eliminada.idfrase} ha sido eliminada")

            Frase.WriteFrase()
            return
    
    print(f"La frase {id_frase} no existe")

def modificar_frase():
    idfrase = input("Ingrese el id de la frase a modificar: ")
    for frase in frases:
        if frase.idfrase == idfrase:
            print("Deseas modificar:\n1.Texto de frase\n2.Autor\n3.Texto y autor")
            opcion = int(input("Elige una opcion: "))
            if opcion == 1:
                modificacion_texto = input("Ingresa la modificacion que deseas a la frase: ")
                frase.texto_frase = modificacion_texto
            elif opcion == 2:
                modificacion_autor = input("Ingresa la modificacion del autor: ")
                frase.autor = modificacion_autor
            elif opcion == 3:
                modificacion_texto = input("Ingresa la modificacion que deseas a la frase: ")
                frase.texto_frase = modificacion_texto
                modificacion_autor = input("Ingresa la modificacion del autor: ")
                frase.autor = modificacion_autor
            with open("Frases.txt", "w", encoding="utf8") as amlo:
                for frase in frases:
                    amlo.write(f"{frase.idfrase},{frase.texto_frase}, {frase.autor}\n")
            print("¡Frase modificada exitosamente!")
            
            return
    print("No existe una frase con el id ingresado")