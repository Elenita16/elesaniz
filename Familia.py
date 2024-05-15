class Familia:
    def __init__(self, tipo, ratones):
        self._tipo = tipo
        self._ratones = ratones
    
    def getTipo(self):
        return self._tipo
    def getRatones(self):
        return self._ratones
    def setTipo(self, tipo):
        self._tipo = tipo
    def setRatones(self, ratones):
        self._ratones = ratones

    def __str__(self):
        resultado="Tipo: " + self._tipo + "\n"
        for r in self._ratones:
            resultado += r.__str__()+"\n" 

        return resultado
