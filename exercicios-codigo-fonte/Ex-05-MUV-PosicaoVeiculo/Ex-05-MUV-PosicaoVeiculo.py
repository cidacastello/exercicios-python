import math

# variáveis
tempo = 60

print("*****Posicao do veiculo em M.U.V. *****\n\n")
print("*****Informe os dados abaixo: *****\n\n")

# entrada de dados
posicaoInicial = float(input("Posicao Inicial: "))

velocidadeInicial = float(input("Velocidade Inicial: "))

aceleracao = float(input("Aceleracao: "))

# processamento
posicaoFinal = posicaoInicial + \
    (velocidadeInicial*tempo) + (aceleracao/2)*math.pow(tempo, 2)

# saída de dados

print("\nPosicao final: ", posicaoFinal)
