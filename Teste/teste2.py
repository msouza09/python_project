from rich import print 
import os
# CONSTANTES
VOTOS_BOLSONARO = 0
VOTOS_LULA = 0

#roda eternamente
while True:
#apresente os candidatos
    print("*"*20)
    print(f"[on blue]TOTAL BOLSONARO:[/]{VOTOS_BOLSONARO}{os.linesep}[on red]TOTAL LULA:[/]{VOTOS_LULA}")
    print("*"*20)
#permita votar
    try:
        voto = int(input(f"Para quem gostaria de votar?{os.linesep}1- Bolsonaro{os.linesep}2- Lula{os.linesep}seu voto: "))
        if voto == 1:
            VOTOS_BOLSONARO += 1
        elif voto == 2:
            VOTOS_LULA += 1
        else:
            pass
    except:
        print("Digite apenas 1 ou 2")
    os.system("cls")