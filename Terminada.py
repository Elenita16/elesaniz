import json
import random
from Poblacion import Poblacion
from Raton import Raton
from Familia import Familia

fechasNacimiento=["10/10/2019", "01/11/2019", "04/11/2019", "03/10/2019", "15/10/2019", "14/10/2019", "28/10/2019", "30/11/2019", "01/09/2019", "07/11/2019"]
pesos=[200.23, 198.17, 178.98, 205.1, 231.24, 198.32, 187.14, 169.33, 265.19, 177.67]
temperaturas=[40.0, 39.5, 41.1, 38.2]
descripciones1=["Es gris", "Es blanco", "Es azul"]
descripciones2=["Tiene los ojos rojos", "Es inquiet@", "Tiene los ojos negros"]
cromosomasSinMutacionMacho=["X", "Y"]
cromosomasSinMutacionHembra=["X", "X"]
cromosomasMutacionHembra=["XM", "XM"]
cromosomasMachoEsteril=["XM", "Y"]
cromosomasMachoPoligamia=["XM", "YM"]
tiposMutaciones=["Esteril", "Poligamo"]
nombresClavesJSON = ["Ratones", "codigoRaton","FechaNac", "Peso", "Sexo", "Temperatura", "Descripcion", "Cromosomas"]

def menuPrincipal():
    print("1º Abrir un archivo que contenga una población de ratones pidiendo el nombre al usuario")
    print("2º Crear una población virtual de ratones a partir del tamaño de la población, el porcentaje de machos, hembras y mutaciones")
    print("3º Crear una nueva población de ratones")
    opcionIncorrecta = True
    while opcionIncorrecta:
        try:
            opc= int(input("SELECCIONA UNA OPCIÓN ENTRE 1 Y 3:"))
            opcionIncorrecta = opc<1 or opc>3
            if opcionIncorrecta:
                print("Las opciones tienen que estar entre 1 y 3") 
        except ValueError:
            print("Debe elegir una opcion numerica entre 1 y 3")
    return opc
def subMenu():     
    print("4º Listar los códigos de referencia de todos los ratones de una población")
    print("5º Añadir un nuevo ratón a una población ya existente, indicando todos sus datos")
    print("6º Añadir un nuevo ratón a una población ya existente indicando su nombre y asignando mediante funciones aleatorias el sexo, el peso entre 50 y 100 gramos, la temperatura entre 36 y 38 grados, y las mutaciones en sus cromosomas con un porcentaje del % de posibilidades de contener mutaciones en cualquier de sus cromosomas definidas por un parámetro de la función con valor por defecto de 20%")
    print("7º Eliminar un ratón de una población indicando su código de referencia. Al seleccionar esta opción deben listarse todos los ratones por pantalla")
    print("8º Modificar los datos de un ratón, indicando su código de referencia.")
    print("9º Ver información detallada de un ratón, habiendo especificado previamente su código de referencia")
    print("10º Generar Familia Ratones")    
    print("12º Guardar")
    print("13º Guardar como")
    print("14º Salir")
    opcionIncorrecta = True
    while opcionIncorrecta:
        try:
            opc= int(input("SELECCIONA UNA OPCIÓN SECUNDARIA:"))
            opcionIncorrecta = opc<1 or opc>14 or opc==11
            if opcionIncorrecta:
                print("Las opciones tienen que estar entre 4 y 14, salvo el 11") 
        except ValueError:
            print("Debe elegir una opcion numerica entre 4 y 14, salvo el 11")
    return opc

#metemos los datos de los ratones en la lista que hemos creado antes que está dentro de la variable p 
#buscamos los códigos de los ratones y los mostramos
def crearListaRatones(poblacion, ratones, nombrePoblacion):
    if len(poblacion.keys()) == 1:
        for r in poblacion[nombrePoblacion][nombresClavesJSON[0]]:
            r = Raton(r[nombresClavesJSON[1]],r[nombresClavesJSON[2]], r[nombresClavesJSON[3]], r[nombresClavesJSON[4]], r[nombresClavesJSON[5]], r[nombresClavesJSON[6]], r[nombresClavesJSON[7]])
            ratones.append(r)
    else:
        for r in poblacion["Ratones"]:
            r = Raton(r[nombresClavesJSON[1]],r[nombresClavesJSON[2]], r[nombresClavesJSON[3]], r[nombresClavesJSON[4]], r[nombresClavesJSON[5]], r[nombresClavesJSON[6]], r[nombresClavesJSON[7]])
            ratones.append(r)

ratones=[]

def generarRatonVirtual(ratones, sexo, mutacion, tipoMutacion, contCodigoRaton):
    raton={}
    raton["codigoRaton"]=contCodigoRaton+1
    raton["FechaNac"]=fechasNacimiento[random.randint(0, len(fechasNacimiento)-1)]
    raton["Peso"]=pesos[random.randint(0, len(pesos)-1)]
    raton["Sexo"]=sexo
    raton["Temperatura"]=temperaturas[random.randint(0, len(temperaturas)-1)]
    raton["Descripcion"]=[descripciones1[random.randint(0, len(descripciones1)-1)], descripciones2[random.randint(0, len(descripciones2)-1)]]
    if not mutacion:
        if sexo=="M":        
            raton["Cromosomas"]=cromosomasSinMutacionMacho
        else:
            raton["Cromosomas"]=cromosomasSinMutacionHembra
    else:
        if sexo=="H":
            raton["Cromosomas"]=cromosomasMutacionHembra
        else:
            if tipoMutacion==tiposMutaciones[0]:
                raton["Cromosomas"]=cromosomasMachoEsteril
            else:
                raton["Cromosomas"]=cromosomasMachoPoligamia

    ratones.append(raton)
    contCodigoRaton=contCodigoRaton+1
    return contCodigoRaton

def generarPoblacionVirtual(tamPoblacion, porcentajeMachos, porcentajeMutaciones):
    contCodigoRaton=0
    cantidadMachos=int((tamPoblacion*porcentajeMachos)/100)
    cantidadHembras=int(tamPoblacion-cantidadMachos) 
    cantidadMutacionesMachos=int((((tamPoblacion*porcentajeMutaciones)/100)*porcentajeMachos)/100)
    cantidadMutacionesHembras=int(((tamPoblacion*porcentajeMutaciones)/100)-cantidadMutacionesMachos) 
    porcentajeMachosEsteriles=random.randint(1, 100)
    cantidadMachosEsteriles=int(cantidadMutacionesMachos*porcentajeMachosEsteriles/100)
    cantidadMachosPoligamos=cantidadMutacionesMachos-cantidadMachosEsteriles

    poblacion={}
    poblacion["Nombre"]="Poblacion Virtual Ejercicio 2"
    poblacion["Responsable"]="Elena Santamaria"
    #Genera un numero aleatorio entre 1 y 269 ambos inclusive, garantizamos que sea mayor que 0 y menor que 270
    poblacion["nDias"] = random.randint(1, 269)
    poblacion["Ratones"]=[]
    #Generamos todas las hembras sin mutacion
    i=0
    while i < (cantidadHembras-cantidadMutacionesHembras):
        contCodigoRaton = generarRatonVirtual(poblacion["Ratones"], "H", False, "Ninguna", contCodigoRaton)
        i+=1
    i=0
    #Generamos todos los machos sin mutacion
    while i <(cantidadMachos-cantidadMutacionesMachos):
        contCodigoRaton = generarRatonVirtual(poblacion["Ratones"], "M", False, "Ninguna", contCodigoRaton)
        i+=1
    i=0
    #Generamos todos las hembras con mutacion
    while i <cantidadMutacionesHembras:    
        contCodigoRaton = generarRatonVirtual(poblacion["Ratones"], "H", True, "Esteril", contCodigoRaton)
        i+=1
    i=0
    #Generamos todos los machos esteriles
    while i < cantidadMachosEsteriles:    
        contCodigoRaton = generarRatonVirtual(poblacion["Ratones"], "M", True, "Esteril", contCodigoRaton)
        i+=1
    #Generamos todos los machos poligamos
    i=0
    while i < cantidadMachosPoligamos:    
        contCodigoRaton = generarRatonVirtual(poblacion["Ratones"], "M", True, "Poligamo", contCodigoRaton)
        i+=1
    #print(poblacion)
    #print(len(poblacion["Ratones"]))
    return poblacion

#4
def mostrarCodigosRatones(poblacion):
    for r in poblacion.getRatones():
        print(r.getCodigo())
#5
def cromosomaValido(sexo, cromosoma, pos):
    if sexo=="H" or (sexo=="M" and pos == 1):
        return cromosoma=="X" or cromosoma=="XM"
    else:
        if sexo=="M" and pos==2:
            return cromosoma=="Y" or cromosoma=="YM"

def diaValido(dia, mes):
    if mes==2:
        return dia>=1 and dia<=28
    else:
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            return dia>=1 and dia<=30
        else:
            return dia>=1 and dia<=31

def mesValido(mes):
    return mes>=1 and mes<=12

def anioValido(anio):
    return anio>2000

def fechaValida(fecha):
    #Formato de la fecha valida: dd/mm/aaaa
    if len(fecha)!=10:
        return False
    else:
        if fecha[2]!="/" or fecha[5]!="/":
            return False
        else:
            return anioValido(int(fecha[6:10])) and mesValido(int(fecha[3:5])) and diaValido(int(fecha[0:2]), int(fecha[3:5]))             
    
    return True



def leerRaton(poblacion):
    repetido = True
    while repetido:
        try: 
            codigo = int(input("Inserte el codigo del raton: "))
            repetido = buscarCodigoRaton(poblacion, codigo)
            if repetido:
                print("Ya existe un raton con ese codigo en la poblacion, inserte un codigo no repetido")
        except ValueError:
            print("El codigo del raton debe ser un entero")

    fechaInvalida = True
    while fechaInvalida:
        fechaNac = input("Inserte la fecha de nacimiento del raton: ")
        fechaInvalida=not fechaValida(fechaNac)
        print("fechaInvalida:", fechaInvalida)
        if fechaInvalida:
            print("El formato de la fecha es dd/mm/aaaa y los datos deben conformar una fecha valida a partir del año 2000")    
    
    pesoInvalido = True
    while pesoInvalido:
        try:
            peso = float(input("Inserte el peso del raton: "))
            pesoInvalido = False
        except:
            print("El peso debe ser un numero")
            pesoInvalido = True
    
    
    sexoInvalido = True
    while sexoInvalido:
        sexo = input("Inserte el sexo del raton: ")
        if len(sexo)>1 or (sexo!="M" and sexo!="H"):
             print("Debe elegir M o H")
        else:
            sexoInvalido = False
    tempInvalido = True
    while tempInvalido:
        try:
            temperatura = float(input("Inserte la temperatura del raton: "))
            tempInvalido = False
        except:
            print("La temperatura debe ser un numero")
            tempInvalido = True
    
    descripciones=[]
    descripcion1 = input("Inserte la descripcion 1 del raton: ")
    descripcion2 = input("Inserte la descripcion 2 del raton: ")
    descripciones.append(descripcion1)
    descripciones.append(descripcion2)
    cromosomas=[]
    cromInvalido = True
    while cromInvalido:
        cromosoma1 = input("Inserte el primer cromosoma del raton: ")
        cronInvalido=not cromosomaValido(sexo, cromosoma1, 1)
        if cronInvalido:
            print("El primer cromosoma de un raton solo puede valer X o XM")    
    cromInvalido = True
    while cromInvalido:
        cromosoma2 = input("Inserte el segundo cromosoma del raton: ")
        cronInvalido=not cromosomaValido(sexo, cromosoma2, 2)
        if cronInvalido:
            if sexo=="H":
                print("El primer cromosoma de un raton hembra solo puede valer X o XM")
            else:
                print("El primer cromosoma de un raton hembra solo puede valer Y o YM")    

    cromosomas.append(cromosoma1)
    cromosomas.append(cromosoma2)
    raton= Raton(codigo, fechaNac, peso, sexo, temperatura, descripciones, cromosomas)
    poblacion.getRatones().append(raton)

#Ejercicio 6
def generarRatonAleatorio(ratones, mutacion, codRaton):
    raton={}
    raton["Codigo"]=codRaton
    raton["FechaNac"]=fechasNacimiento[random.randint(0, len(fechasNacimiento)-1)]
    raton["Peso"]=random.uniform(50, 100)
    s = random.randint(0,1)
    if s==0:
        raton["Sexo"]="M"
    else:
        raton["Sexo"]="H"
    raton["Temperatura"]=random.uniform(36,38)
    raton["Descripcion"]=[descripciones1[random.randint(0, len(descripciones1)-1)], descripciones2[random.randint(0, len(descripciones2)-1)]]
    if not mutacion:
        if raton["Sexo"]=="M":        
            raton["Cromosomas"]=cromosomasSinMutacionMacho
        else:
            raton["Cromosomas"]=cromosomasSinMutacionHembra
    else:
        if raton["Sexo"]=="H":
            raton["Cromosomas"]=cromosomasMutacionHembra
        else:
            tipoMutacion = random.randint(0,1)
            if tipoMutacion==0:
                raton["Cromosomas"]=cromosomasMachoEsteril
            else:
                raton["Cromosomas"]=cromosomasMachoPoligamia

    ratones.append(raton)

#Busqueda ejercicios 7, 8 y 9
def buscarRaton(poblacion, codRaton):
    for r in poblacion.getRatones():
        if r.getCodigo() == codRaton:
            return r


#Ejercicio 8
def modificarRaton(raton):
    raton.setFechaNac(input("Inserte la fecha de nacimiento del raton: "))
    raton.setPeso(float(input("Inserte el peso del raton: ")))
    raton.setSexo(input("Inserte el sexo del raton: "))
    raton.setTemperatura(float(input("Inserte la temperatura del raton: ")))
    descripciones = []
    descripcion1 = input("Inserte la descripcion 1 del raton: ")
    descripcion2 = input("Inserte la descripcion 2 del raton: ")
    descripciones.append(descripcion1)
    descripciones.append(descripcion2)
    raton.setDescripciones(descripciones)
    cromosomas = []
    cromosoma1 = input("Inserte el primer cromosoma del raton: ")
    cromosoma2 = input("Inserte el segundo cromosoma del raton: ")
    cromosomas.append(cromosoma1)
    cromosomas.append(cromosoma2)
    raton.setCromosomas(cromosomas)

#Busqueda codigo raton para validar codigos no repetidos
def buscarCodigoRaton(poblacion, codRaton):
    for r in poblacion.getRatones():
        if r.getCodigo() == codRaton:
            return True
    return False

#Ejercicio 10
def machoMutacion(raton):
    if raton.getCromosomas()[0] =="X" and raton.getCromosomas()[1] =="Y":
        print("False")
        return False
    else:
        if raton.getCromosomas()[0] =="XM":
            print("Esteril")
            return "Esteril"
        if raton.getCromosomas()[1] =="YM":
            print("Poligamo")
            return "Poligamo"

def hembraMutacion(raton):
    return raton.getCromosomas()[0] =="XM" and raton.getCromosomas()[1] =="XM"

def ejercicio4(p):
    print("CÓDIGOS DE TODOS LOS RATONES DE LA POBLACIÓN: \n")
    mostrarCodigosRatones(p)
def ejercicio5(p):
    print("DATOS DEL RATON: \n")
    leerRaton(p)
    print("DATOS DE LA POBLACION: \n")    
    print(p)
def ejercicio6(p):
    codRaton = int(input("Inserte el codigo del raton: "))
    while codRaton in range(1,6):
        print("Este código ya existe")
        codRaton = int(input("Inserte el codigo del raton: "))
    mutacion = False
    try:
        probMutacion = int(input("Inserte el porcentaje de probabilidad de mutacion: "))
    except ValueError:
        probMutacion = 20
    numMutacion = random.randint(1, 10)
    if numMutacion <= (probMutacion/10):
        mutacion = True    
    generarRatonAleatorio(p.getRatones(), mutacion, codRaton)
    print("DATOS DE LA POBLACION: \n")    
    print(p)
def ejercicio7(p):
    print("CÓDIGOS DE TODOS LOS RATONES DE LA POBLACIÓN: \n")
    mostrarCodigosRatones(p)
    codRaton = int(input("Inserte el codigo del raton: "))
    raton = buscarRaton(p, codRaton)
    p.getRatones().remove(raton)
    print("DATOS DE LA POBLACION: \n")    
    print(p)
def ejercicio8(p):
    print("CÓDIGOS DE TODOS LOS RATONES DE LA POBLACIÓN: \n")
    mostrarCodigosRatones(p)
    codRaton = int(input("Inserte el codigo del raton: "))
    raton = buscarRaton(p, codRaton)
    modificarRaton(raton)
    print("DATOS DE LA POBLACION: \n")    
    print(p)
def ejercicio9(p):
    print("CÓDIGOS DE TODOS LOS RATONES DE LA POBLACIÓN: \n")
    mostrarCodigosRatones(p)
    codRaton = int(input("Inserte el codigo del raton: "))
    raton = buscarRaton(p, codRaton)
    print("DATOS DEL RATON: \n")
    print(raton)

def ejercicio10(p):
    ratonesFamilia = []
    hembra = True
    posRaton = 0
    while hembra:
        posRaton = random.randint(0, len(p.getRatones())-1)
        if p.getRatones()[posRaton].getSexo()=="M":
            hembra = False
    ratonMacho = p.getRatones()[posRaton]
    machoMut = machoMutacion(ratonMacho)
    ratonesFamilia.append(ratonMacho)
    if p.poblacionFamilia():
        print("machoMut: ", machoMut)
        p.getRatones().remove(p.getRatones()[posRaton])
        if type(machoMut) == str and machoMut!="Poligamo" or not machoMut:
            macho = True
            posRaton = 0
            while macho:
                posRaton = random.randint(0, len(p.getRatones())-1)
                if p.getRatones()[posRaton].getSexo()=="H":
                    macho = False
            ratonHembra = p.getRatones()[posRaton]
            ratonesFamilia.append(ratonHembra)
            print(ratonesFamilia)
            f = Familia("Normal", ratonesFamilia)
            print(f)
            p.getRatones().remove(p.getRatones()[posRaton])
        else:
            if type(machoMut) == str and machoMut=="Poligamo":
                numero = random.randint(0,9)
                if numero<5:
                    print("Numero menor que 5")
                    macho = True
                    posRaton = 0
                    while macho:
                        posRaton = random.randint(0, len(p.getRatones())-1)
                        if p.getRatones()[posRaton].getSexo()=="H":
                            macho = False
                    ratonHembra = p.getRatones()[posRaton]
                    ratonesFamilia.append(ratonHembra)
                    print(ratonesFamilia)
                    f = Familia("Poligamica", ratonesFamilia)
                    print(f)
                    p.getRatones().remove(p.getRatones()[posRaton])
                else:
                    print("Numero mayor que 5")
                    puedoHacerFamilia = p.poblacionFamilia()
                    while(puedoHacerFamilia):
                        macho = True
                        posRaton = 0
                        while macho:
                            posRaton = random.randint(0, len(p.getRatones())-1)
                            if p.getRatones()[posRaton].getSexo()=="H":
                                macho = False
                        ratonHembra = p.getRatones()[posRaton]
                        ratonesFamilia.append(ratonHembra)
                        p.getRatones().remove(p.getRatones()[posRaton])
                        puedoHacerFamilia = p.poblacionFamilia()
                        print(ratonesFamilia)
                        f = Familia("Poligamica", ratonesFamilia)    
                        print(f)
    else:               
        print("Quedan ratones desparejados y no se puede formar una familia")
def ejercicio12(p):
    poblacionEscribir ={}
    poblacion1 = p.poblacionADiccionario()
    poblacionEscribir["Poblacion"] = poblacion1
    with open('poblacionEjercicio1.json', 'w') as file:
        json.dump(poblacionEscribir, file, indent=4)

def ejercicio13(p):
    poblacionEscribir ={}
    poblacion1 = p.poblacionADiccionario()
    poblacionEscribir["Poblacion"] = poblacion1
    nombreFich = input("Inserte el nombre del fichero para guardar la poblacion: ")
    with open(nombreFich+'.json', 'w') as file:
        json.dump(poblacionEscribir, file, indent=4)
def main():
    opc = menuPrincipal()

    if opc == 1:
        rutaInvalida = True
        while rutaInvalida:
            try:
                nombre = input("Inserte el nombre del fichero de la poblacion:  \n")
                rutaCompleta = 'C:\\Users\\elesa\\Desktop\\CEU\\PracticaFinal\\'+ nombre +'.json'
            
                with open(rutaCompleta) as file:
                    poblacionJSON = json.load(file)

                data_string = json.dumps(poblacionJSON)
                print ('JSON:', data_string)
                ratones=[]
                crearListaRatones(poblacionJSON, ratones, "Poblacion")
                p = Poblacion(poblacionJSON["Poblacion"]["Nombre"],poblacionJSON["Poblacion"]["Responsable"], poblacionJSON["Poblacion"]["nDias"], ratones)
                rutaInvalida = False
            except FileNotFoundError:
                print("Nombre del fichero no valido, vuelva a intentarlo") 

        opc2 = subMenu()
        while(opc2!=14):    
            if opc2 == 4:
                ejercicio4(p)
                input()
            if opc2 == 5:
                ejercicio5(p)
                input()
            if opc2 == 6:
                ejercicio6(p)
                input()
            if opc2 == 7:
                ejercicio7(p)
                input()
            if opc2 == 8:
                ejercicio8(p)
                input()
            if opc2 == 9:
                ejercicio9(p)
                input()        
            if opc2==10:
                ejercicio10(p)
                input()
            if opc2 == 12:
                ejercicio12(p)
                input()
            if opc2 == 13:
                ejercicio13(p)
                input()
            opc2 = subMenu()
        if opc2 == 14:
            print("Hasta pronto...")
    if opc == 2:
        tamPoblacion = int(input("¿Cuántos ratones quieres incluir en tu poblacion virtual?: "))
        porcentajeMachos=int(input("Introduce el porcentaje de machos que quieres 0-100: "))
        porcentajeMutaciones=int(input("Introduce el porcentaje de mtaciones que quieres que haya: ")) #aleatorio
        poblacion = generarPoblacionVirtual(tamPoblacion, porcentajeMachos, porcentajeMutaciones)
        ratones=[]
        crearListaRatones(poblacion, ratones, "")
        p2 = Poblacion(poblacion["Nombre"],poblacion["Responsable"], poblacion["nDias"], ratones)
        print("DATOS DE LA POBLACION VIRTUAL GENERADA")
        print(p2)
        opc2 = subMenu()
        while(opc2 != 14): 
            if opc2 == 4:
                ejercicio4(p2)
                input()
            if opc2 == 5:
                ejercicio5(p2)
                input()
            if opc2 == 6:
                ejercicio6(p2)
                input()
            if opc2 == 7:
                ejercicio7(p2)
                input()
            if opc2 == 8:
                ejercicio8(p2)
                input()
            if opc2 == 9:
                ejercicio9(p2)
                input()
            if opc2==10:
                ejercicio10(p2)
                input()
            if opc2 == 12:
                ejercicio12(p2)
                input()
            if opc2 == 13:
                ejercicio13(p2)
                input()
            opc2 = subMenu()
        if opc2==14:
                print("Hasta pronto...")
    if opc == 3:
        ratones=[]
        p3 = Poblacion("Poblacion Ejercicio 3","Responsable Ejercicio 3", 210, ratones )
        nRatones = int(input("Inserte el número de ratones de la población: "))
        i=0
        while i <nRatones:
            print("DATOS DEL RATON: \n")
            leerRaton(p3)
            i+=1
        print("DATOS DE LA POBLACION: \n")
        print(p3)
        opc2 = subMenu()
        while(opc2!=14): 
            if opc2 == 4:
                ejercicio4(p3)
                input()
            if opc2 == 5:
                ejercicio5(p3)
                input()
            if opc2 == 6:
                ejercicio6(p3)
                input()
            if opc2 == 7:
                ejercicio7(p3)
                input()
            if opc2 == 8:
                ejercicio8(p3)
                input()
            if opc2 == 9:
                ejercicio9(p3)
                input()
            if opc2==10:
                ejercicio10(p3)
                input()
            if opc2 == 12:
                ejercicio12(p3)
                input()
            if opc2 == 13:
                ejercicio13(p3)
                input()
            opc2 = subMenu()
        if opc2==14:
            print("Hasta pronto...")
if __name__=="__main__":
    main()
