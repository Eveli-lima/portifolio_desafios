# 1. Algoritmo de Comparação de Idade
# Crie um programa que leia a idade do usuário e informe se ele é maior ou menor de idade.
# Utilize uma estrutura condicional if-else para fazer a verificação.
# Dica: Utilize input() para capturar a idade do usuário, e a função int() para converter a entrada para um número inteiro.

#idade = int(input('Idade: '))
def comparar_idade(idade):
    if idade >= 18:
        return f'A pessoa com {idade} é maior de idade.'
    else:
        return f'A pessoa com {idade} é menor de idade.'