nlinha = 20
ncoluna = 20
matriz = [""] * nlinha
linha_l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
coluna_l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']

for linha in range (20):
    matriz[linha] = [' '] * ncoluna
for linha in range(nlinha):
    for coluna in range (ncoluna):
        if coluna == 0:
            print(f'{linha_l[linha]} [{matriz[linha][coluna]}]', end='')
        elif (coluna == 19):
            print(f'[{matriz[linha][coluna]}]')
        else:
            print(f'[{matriz[linha][coluna]}]', end='')
    print()

cont_de_pontos = 0
porta_aviao = 4
cruzador = 3
fragata = 2
naufrago = " "

