import datetime

#Função que adquire o horário atual
#Utilizado em grande parte dos cálculos
dia = datetime.datetime.now()

#Tradução do ano (python adquire as informções em inglês)
traducao_ano = {
    "Sunday" : "Domingo",
    "Monday" : "Segunda",
    "Tuesday" : "Terça",
    "Wednesday" : "Quarta",
    "Thursday" : "Quinta",
    "Friday" : "Sexta",
    "Saturday" : "Sábado"
}

#Tradução do mês (python adquire as informções em inglês)
traducao_mes = {
    "January" : "Janeiro",
    "February" : "Fevereiro",
    "March" : "Março",
    "April" : "Abril",
    "May" : "Maio",
    "June" : "Junho",
    "July" : "Julho",
    "August" : "Agosto",
    "September" : "Setembro",
    "October" : "Outubro",
    "November" : "Novembro",
    "December" : "Dezembro"
}

#Tradução da hora (python adquire as informções em inglês)
traducao_hora = {
    "AM" : "da manhã",
    "PM" : "da tarde"
}

#Linha usada para demilitar
def linha():
    print("="*90)

#Menu
def menu():
    print('''
[1] - Mostra todas as informações dia atual
[2] - Mostra o dia do ano (total) 
[3] - Mostra o século
[4] - Mostra a hora       
''')
    
#Função que mostra as informações do dia atual
def horarioatual():
    dia_semana = dia.strftime("%A")
    print(f"Hoje é dia {dia.strftime("%d")}, {traducao_ano[dia_semana]} | Ano: {dia.strftime("%Y")} | Mês: {traducao_mes[dia.strftime("%B")]}({dia.strftime("%m")})  ")
    linha()
    
#Função que mostra o total de dias já corridos e quantos faltam para o final do ano
def dia_total():
    print(f"O dia de hoje é o dia número {str(dia.strftime("%j"))}. Faltam {365 - int(dia.strftime("%j")) } dias até o final do ano") 
    linha()
    
#Função que mostra o século atual    
def seculo():
    print(f"O século atual é {str(dia.strftime("%C"))}")    
    linha()
    
#Função que mostra o horário atual, pode ser escolhido entre o sistema norte-americano e o brasileiro
def horas():
    a = input("Qual forma você deseja ver o horário atual? \nENG ou PTBR?: ")
    linha()
    hora = a.upper()
    if hora == "ENG":
        print(f"O horário atual no formato norte-americano é: {str(dia.strftime("%H"))}:{str(dia.strftime("%I"))} {str(dia.strftime("%p"))}")
        linha()
    elif hora == "PTBR":
        print(f"O horário atual no formato brasileiro é: {str(dia.strftime("%H"))}:{str(dia.strftime("%I"))} {traducao_hora[str(dia.strftime("%p"))]}")
        linha()
    else:
        print("Essa não é uma das opções")
        linha()

while True:
    menu()
    escolha = input("Escolha uma das opções: ")
    if escolha == "1":
        linha()
        horarioatual()
    elif escolha == "2":
        linha()
        dia_total()
    elif escolha == "3":
        linha()
        seculo()
    elif escolha == "4":
        linha()
        horas()
    else:
        print("Essa não é uma opção válida")
        
#Funções não utilizadas:
# %a = dia da semana com nome abreviado (monday = mon)
# %w = dia da semana com número (domingo é 0, sábado é 6)
# %b = mês do ano abreviado (december = dec)
# %y = ano abreviado (2024 = 24)
# %M = minutos
# %S = segundos
# %f = milisegundos
# %Z = fuso horário
