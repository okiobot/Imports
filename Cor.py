from colorama import *

#Cores usadas para colorir a palavra
cores_palavra = {"Amarelo" : Fore.YELLOW,
                "Azul" : Fore.BLUE,
                "Branco" : Fore.WHITE,
                "Ciano" : Fore.CYAN,
                "Magenta" : Fore.MAGENTA,
                "Preto" : Fore.BLACK,
                "Verde" : Fore.GREEN,
                "Vermelho" : Fore.RED
}

#Cores usadas para colorir o fundo
cores_fundo = {"Amarelo" : Back.YELLOW,
                "Azul" : Back.BLUE,
                "Branco" : Back.WHITE,
                "Ciano" : Back.CYAN,
                "Magenta" : Back.MAGENTA,
                "Preto" : Back.BLACK,
                "Verde" : Back.GREEN,
                "Vermelho" : Back.RED
}

#Linha usada para delimitar
def linha():
    print("="*90)

while True:
    try:
        #Usuário escolhe a palavra
        frase = input("Digite uma palavra: ")
        linha()
        
        print("Cores:")
        #Mostra todas as cores disponíveis
        for key in cores_palavra:
            print(key)
            
        linha()
        cor = str(input("De qual cor você deseja que a palavra seja colorida: "))
        linha()
        
        fundo = str(input("De qual cor você deseja que o fundo seja colorido?: "))
        linha()
        
        #Colore a palavra com a cor selecionada
        palavra = (cores_palavra[cor] + frase)
        
        #Colore o fundo com a cor escolhida
        print(f"{cores_fundo[fundo] + palavra}\033[0m")
    
    #Caso o usuário digite um valor inválido
    except KeyError:
        print("Por favor escolha uma cor válida")