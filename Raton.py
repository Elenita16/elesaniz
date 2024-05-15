class Raton:
    def __init__(self, codigo, fechaNac, peso, sexo, temperatura, descripciones, cromosomas):
        self._codigo = codigo
        self._fechaNac = fechaNac
        self._peso = peso
        self._sexo = sexo
        self._temperatura = temperatura
        self._descripciones = descripciones
        self._cromosomas = cromosomas
    
    def getCodigo(self):
        return self._codigo

    def getFechaNac(self):
        return self._fechaNac

    def getPeso(self):
        return self._peso

    def getSexo(self):
        return self._sexo 
    
    def getTemperatura(self):
        return self._temperatura 
    
    def getDescripciones(self):
        return self._descripciones
    
    def getCromosomas(self):
        return self._cromosomas
    


    def setCodigo(self, codigo):
        self._codigo = codigo

    def setFechaNac(self, fechaNac):
        self._fechaNac = fechaNac

    def setPeso(self, peso):
        self._peso = peso

    def setSexo(self, sexo):
        self._sexo = sexo
    
    def setTemperatura(self, temperatura):
        self._temperatura = temperatura
    
    def setDescripciones(self, descripciones):
        self._descripciones = descripciones
    
    def setCromosomas(self, cromosomas):
        self._cromosomas = cromosomas
    
    def __str__(self):
        resultado = "Codigo: " + str(self._codigo) + "\n"
        resultado +="Fecha Nacimiento: "+ self._fechaNac + "\n"
        resultado +="Peso: "+ str(self._peso) + "\n"
        resultado +="Sexo: "+ str(self._sexo) +"\n"
        resultado +="Temperatura: " + str(self._temperatura) + "\n"
        resultado +="Descripcion: "+ self._descripciones[0] +" "+ self._descripciones[1]+"\n"
        resultado +="Cromosomas: "+ self._cromosomas[0] +" "+ self._cromosomas[1] + "\n"
        return resultado


    def ratonADiccionario(self):
        r ={
            "codigoRaton": self._codigo,
			"FechaNac":self._fechaNac,
			"Peso": self._peso,
			"Sexo": self._sexo,
			"Temperatura": self._temperatura,
			"Descripcion": self._descripciones,
			"Cromosomas": self._cromosomas
        }
        return r
    
