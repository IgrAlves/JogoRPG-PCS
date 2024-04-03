from atributos import Atributos

class Personagem:

    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def escolher_raca(self):
        match self.raca:
            case 1:
                return "Dwarf"
            case 2:
                return "Elf"
            case 3:
                return "Barbaro"
            case 4:
                return "Human"
            case 5:
                return "DragonBorn"
            case 6:
                return "Gnome"
            case 7:
                return "Tiefling"
            case _:
                return "Valor inválido"