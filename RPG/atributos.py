import random
class Atributos:

    def __init__(self, forca, destreza, constituicao, sabedoria, inteligencia, carisma):
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.sabedoria = sabedoria
        self.inteligencia = inteligencia
        self.carisma = carisma

    def randomizar_forca(self):
        self.forca += random.randint(0, 22)
        if self.forca == 0:
            return "Incorpóreo (0)"
        elif self.forca >= 1 and self.forca <= 5:
            return f"Incapaz ({self.forca})"
        elif self.forca >= 6 and self.forca <= 9:
            return f"Fraco ({self.forca})"
        elif self.forca >= 10 and self.forca <= 11:
            return f"Mediano ({self.forca})"
        elif self.forca >= 12 and self.forca <= 15:
            return f"Forte ({self.forca})"
        elif self.forca >= 16 and self.forca <= 20:
            return f"Super Poderoso ({self.forca})"
        elif self.forca >= 21:
            return f"Imbatível ({self.forca})"
        
    def randomizar_destreza(self):
        self.destreza += random.randint(0, 22)
        if self.destreza == 0:
            return f"Desacordado ({self.destreza})"
        elif self.destreza >= 1 and self.destreza <= 5:
            return f"Abatido ({self.destreza})"
        elif self.destreza >= 6 and self.destreza <= 9:
            return f"Desajeitado ({self.destreza})"
        elif self.destreza >= 10 and self.destreza <= 11:
            return f"Regular ({self.destreza})"
        elif self.destreza >= 12 and self.destreza <= 15:
            return f"Ágil ({self.destreza})"
        elif self.destreza >= 16 and self.destreza <= 20:
            return f"Ninja ({self.destreza})"
        elif self.destreza >= 21:
            return f"Imperceptível ({self.destreza})"
        
    def randomizar_constituicao(self):
        self.constituicao += random.randint(0, 22)
        if self.constituicao == 0:
            return "Espectro (0)"
        elif self.constituicao >= 1 and self.constituicao <= 5:
            return f"Enfermo ({self.constituicao})"
        elif self.constituicao >= 6 and self.constituicao <= 9:
            return f"Frágil ({self.constituicao})"
        elif self.constituicao >= 10 and self.constituicao <= 11:
            return f"Saudável ({self.constituicao})"
        elif self.constituicao >= 12 and self.constituicao <= 15:
            return f"Durão ({self.constituicao})"
        elif self.constituicao >= 16 and self.constituicao <= 20:
            return f"Super Resistente ({self.constituicao})"
        elif self.constituicao >= 21:
            return f"Imortal ({self.constituicao})"

    def randomizar_sabedoria(self):
        self.sabedoria += random.randint(0, 22)
        if self.sabedoria == 0:
            return "Inconsciente (0)"
        elif self.sabedoria >= 1 and self.sabedoria <= 5:
            return f"Irracional ({self.sabedoria})"
        elif self.sabedoria >= 6 and self.sabedoria <= 9:
            return f"Desatento ({self.sabedoria})"
        elif self.sabedoria >= 10 and self.sabedoria <= 11:
            return f"Simples ({self.sabedoria})"
        elif self.sabedoria >= 12 and self.sabedoria <= 15:
            return f"Perspicaz ({self.sabedoria})"
        elif self.sabedoria >= 16 and self.sabedoria <= 20:
            return f"Filósofo ({self.sabedoria})"
        elif self.sabedoria >= 21:
            return f"Iluminado ({self.sabedoria})" 

    def randomizar_inteligencia(self):
        self.inteligencia += random.randint(0, 22)
        if self.inteligencia == 0:
            return "Inanimado (0)"
        elif self.inteligencia >= 1 and self.inteligencia <= 5:
            return f"incivilizado ({self.inteligencia})"
        elif self.inteligencia >= 6 and self.inteligencia <= 9:
            return f"Parvo ({self.inteligencia})"
        elif self.inteligencia >= 10 and self.inteligencia <= 11:
            return f"Medíocre ({self.inteligencia})"
        elif self.inteligencia >= 12 and self.inteligencia <= 15:
            return f"Estudado ({self.inteligencia})"
        elif self.inteligencia >= 16 and self.inteligencia <= 20:
            return f"Gênio ({self.inteligencia})"
        elif self.inteligencia >= 21:
            return f"Onisciente ({self.inteligencia})"

    def randomizar_carisma(self):
        self.carisma += random.randint(0, 22)
        if self.carisma == 0:
            return "Aberração (0)"
        elif self.carisma >= 1 and self.carisma <= 5:
            return f"Inexpressivo ({self.carisma})"
        elif self.carisma >= 6 and self.carisma <= 9:
            return f"Rude ({self.carisma})"
        elif self.carisma >= 10 and self.carisma <= 11:
            return f"Sociável ({self.carisma})"
        elif self.carisma >= 12 and self.carisma <= 15:
            return f"Persuasivo ({self.carisma})"
        elif self.carisma >= 16 and self.carisma <= 20:
            return f"Influente ({self.carisma})"
        elif self.carisma >= 21:
            return f"Ídolo ({self.carisma})"    