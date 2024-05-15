class Poblacion:
    def __init__(self, nombre, responsable, nDias, ratones):
        self._nombre = nombre
        self._responsable = responsable
        self._nDias = nDias
        self._ratones = ratones
    
    def getNombre(self):
        return self._nombre
    def getResponsable(self):
        return self._responsable
    def getNDias(self):
        return self._nDias
    def getRatones(self):
        return self._ratones

    def setNombre(self, nombre):
        self._nombre = nombre
    def setResponsable(self, responsable):
        self._responsable = responsable
    def setNDias(self, nDias):
        self._nDias = nDias
    def setRatones(self, ratones):
        self._ratones = ratones

    def __str__(self):
        resultado="Nombre: " + self._nombre + "\n"
        resultado += "Responsable: "+ self._responsable + "\n"
        resultado += "Numero de dias: "+ str(self._nDias) + "\n"
        resultado += "Ratones: " + "\n"
        for r in self._ratones:
            resultado += r.__str__()+"\n" 

        return resultado
    
    def soloMachos(self):
        cont = 0
        for r in self._ratones:
            if r.getSexo() == "M":
                cont+=1
        return cont == len(self._ratones)

    def soloHembras(self):
        cont = 0
        for r in self._ratones:
            if r.getSexo() == "H":
                cont+=1

        return cont == len(self._ratones)
        
    def poblacionFamilia(self):
        '''print("len(self._ratones): ", len(self._ratones))
        print("self.soloMachos(): ", self.soloMachos())
        print("self.soloHembras()",self.soloHembras())
        print("len(self._ratones)>1 and not self.soloMachos() and not not self.soloHembras() : ", len(self._ratones)>1 and not self.soloMachos() and not self.soloHembras() )'''
        return len(self._ratones)>1 and not self.soloMachos() and not self.soloHembras() 
    
    def poblacionADiccionario(self):
        p={
            "Nombre": self._nombre,
            "Responsable":self._responsable,
            "nDias": self._nDias,
            "Ratones":[]
        }
        for r in self._ratones:
            p["Ratones"].append(r.ratonADiccionario())
        return p