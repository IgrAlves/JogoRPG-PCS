from personagem import Personagem
from atributos import Atributos

nome_personagem = str(input("Nome de seu Héroi: "))
raca_personagem = int(input('''               
[1] - Dwarf        
[2] - Elf       
[3] - Barbaro
[4] - Human
[5] - Dragonborn
[6] - Gnome
[7] - Tiefling 
Escolha sua Classe: '''))

match raca_personagem:
    case 1:
        forca = 0
        destreza = 0
        constituicao = 2
        sabedoria = 0
        inteligencia = 0
        carisma = 0
    case 2:
        forca = 0
        destreza = 2
        constituicao = 0
        sabedoria = 0
        inteligencia = 0
        carisma = 0
    case 3:
        forca = 0
        destreza = 2
        constituicao = 0
        sabedoria = 0
        inteligencia = 0
        carisma = 0
    case 4:
        forca = 1
        destreza = 1
        constituicao = 1
        sabedoria = 1
        inteligencia = 1
        carisma = 1
    case 5:
        forca = 2
        destreza = 0
        constituicao = 0
        sabedoria = 0
        inteligencia = 0
        carisma = 1
    case 6:
        forca = 0
        destreza = 0
        constituicao = 0
        sabedoria = 0
        inteligencia = 2
        carisma = 0
    case 7:
        forca = 0
        destreza = 0
        constituicao = 0
        sabedoria = 0
        inteligencia = 1
        carisma = 2

personagem1 = Personagem(nome_personagem, raca_personagem)
atributo1 = Atributos(forca, destreza, constituicao, sabedoria, inteligencia, carisma)

    
#apresentação do personagem
print(f"\n\nBem-vindo a Dusserdolf {nome_personagem} da raça {personagem1.escolher_raca()}, ao maior reino existente entre os homens!")
print("\nConheça seus atributos, meu jovem guerreiro...")
print("----------------------------------------")
print("Força: ", atributo1.randomizar_forca())
print("Destreza: ", atributo1.randomizar_destreza())
print("Constituição: ", atributo1.randomizar_constituicao())
print("Sabedoria: ", atributo1.randomizar_sabedoria())
print("Inteligência: ", atributo1.randomizar_inteligencia())
print("Carisma: ", atributo1.randomizar_carisma())
print("----------------------------------------")
