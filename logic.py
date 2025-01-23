# 1. Algoritmo de Comparação de Idade
# Crie um programa que leia a idade do usuário e informe se ele é maior ou menor de idade.
# Utilize uma estrutura condicional if-else para fazer a verificação.
# Dica: Utilize input() para capturar a idade do usuário, e a função int() para converter a entrada para um número inteiro.

# idade = int(input('Idade: '))
# def comparar_idade(idade):
#     if idade >= 18:
#         return f'A pessoa com {idade} é maior de idade.'
#     else:
#         return f'A pessoa com {idade} é menor de idade.'
#------------------------------------------------------

#------------------------------------------------
#
# # Recebendo dados pessoais
#
# while True:
#     nome = input("Seu nome: ").strip()
#
#     if any(char.isdigit() for char in nome): # Verifica se há algum digito no nome.
#         print("O nome não pode conter números. Tente novamente.")
#         continue  # Volta ao início do loop para pedir o nome novamente.
#
#     try:
#         idade = int(input("Sua idade: "))
#         if idade <= 0:
#             print("Idade Inválida, tente novamente.")
#         else:
#             print(f"Meu nome é: {nome} e minha idade é: {idade}")
#             break
#     except ValueError: # Captura o erro caso a conversão para inteiro falhe.
#         print("Entrada Inválida! Por favor, digite um número inteiro para idade.")
# #---------------------------------------------------------
#
# # calculadora simples:
#
# while True:
#     try:
#         n1 = float(input("Digite um número: "))
#         n2 = float(input("Digite outro número: "))
#
#         if n2 == 0:
#             print("Nenhum número pode ser divisível por zero, tente novamente.")
#             continue # Volta ao início do loop para pedir outro número.
#
#             # Realiza os cálculos somente de n2 for válido.
#             soma = n1 + n2
#             subt = n1 - n2
#             mult = n1 * n2
#             divi = n1 / n2
#             print(f"{n1} + {n2} = {soma} \n"
#                   f"{n1} - {n2} = {subt} \n"
#                   f"{n1} * {n2} = {mult} \n"
#                   f"{n1} / {n2} = {divi}")
#             break
#     except ValueError:
#         print("Entrada inválida. Digite apenas números.")
#
# #--------------------------------------------------------
#
# # Conversor de temperatura
#
# while True:
#     try:
#         temp_celsius = float(input("Digite a temperatura em Celsios: "))
#
#         temp_fahrenheit = ((temp_celsius * 9) / 5) + 32
#         print(f"Celsius = {temp_celsius} \nFahrenheit = {temp_fahrenheit}")
#         break
#     except ValueError:
#         print("Entrada inválida, digite novamente a temperatura.")
#
#
# #-------------------------------------------------------
#
# # Validador de idade
#
# while True:
#     try:
#         idade = int(input("Digite sua idade: "))
#         if idade < 0:
#             print("Idade inválida!")
#         elif idade > 0:
#             print("Idade válida")
#             break
#     except ValueError:
#         print("Entrada inválida. Por favor, digite um número inteiro.")

#----------------------------------------------------

# 2 Guardando informações:

# Crie um programa que: Consulte o nome e a idade do usuário.
# Mostre uma mensagem como:
# "Olá, [nome]! Você tem [idade] anos."


# nome = str(input("Qual o seu nome? "))
# idade = int(input("Qual a sua idade? "))
# print(f"Olá, {nome}! Você tem {idade} anos.")
#---------------------------------------------------
#Soma de números
# Peça ao usuário dois números (use input()).
# Alguns desses números são mostrados o resultado.
# Dica: Converta os números usando int()ou float().

# n1 = int(input("Digite um número: "))
# n2 = int(input("Digite outro número: "))
# soma = n1 + n2
# print(f"A soma é: {soma}")
#------------------------------------------------------
# Comparação de idade
# Crie um programa que:
# Pergunte a idade de duas pessoas.
# Mostre quem é mais velho ou se tem a mesma idade.
# Exemplo:
# "Pessoa 1 é mais velha." ou"As duas têm a mesma idade."

# pessoa1 = int(input("Pessoa 1: Digite a sua idade: "))
# pessoa2 = int(input("Pessoa 2: Digite a sua idade: "))
#
# #verificação de entradas inválidas
# if pessoa1 <= 0 or pessoa2 <= 0:
#     print("Idade inválida! As idades devem ser maiores que 0.")
# else:
# #comparação de idades válidas
    # if pessoa1 > pessoa2:
    #     print(f"Pessoa 1 idade: {pessoa1} é mais velha.")
    # elif pessoa1 < pessoa2:
    #     print(f"Pessoa 2 idade: {pessoa2} é mais velha.")
    # else:
    #     print("As duas tem a mesma idade!")
#-----------------------------------------------------------------------
# Verificação de maioridade
# Peça a idade do usuário.
# Mostrar:
# "Você é maior de idade."(se a idade for 18 ou mais).
# "Você é menor de idade."(se for menor que 18).
# while True:
#     idade = int(input("Qual a sua idade? "))
#
#     # verificar dados inválidos:
#     if idade <= 0:
#         print("Idade inválida tente denovo.")
#     elif idade >= 100:
#         print(f"Você tem {idade}: Uau! Vc já deveria estar morto e enterrado! kkk tente denovo.")
#     else:
#
#         # dados válidos
#         if idade >= 18:
#             print(f"Você tem {idade}: Você é maior de idade")
#         else:
#             print(f"Você tem {idade}: Você é menor de idade")
#         break
#------------------------------------------------------------
# Calculadora simples
# Pergunte dois números ao usuário.
# Consulte a operação desejada: soma (+), subtração (-), multiplicação (*) ou divisão (/).
# Mostre o resultado da operação.

# while True:
#     n1 = float(input("Digite um número: "))
#     n2 = float(input("Digite outro número: "))
#     print("Escolha a operação: 1 para SOMA, 2 para SUBTRAÇÃO, 3 para MULTIPLICAÇÃO, 4 para DIVISÃO")
#     opção = int(input("Qual opção você quer? "))
#
#     soma = n1 + n2
#     subtração = n1 - n2
#     multiplicação = n1 * n2
#     divisão = n1 / n2
#
#     if opção == 1:
#         print(f"{n1} + {n2} = {soma}")
#     elif opção == 2:
#         print(f"{n1} - {n2} = {subtração}")
#     elif opção == 3:
#         print(f"{n1} * {n2} = {multiplicação}")
#     elif opção == 4:
#         if n2 == 0:
#             print("Erro! Não é possível dividir por zero.")
#         else:
#             print(f"{n1} / {n2} = {divisão}")
#     else:
#             print("Opção inválida! Escolha entre 1, 2, 3 ou 4.")
#
#     continuar = input("Deseja fazer outro cálculo? (s/n): ").strip().lower()
#     if continuar != "s":
#         print("Encerrando a calculadora. Até logo!")
#         break
#-------------------------------------------------------------
# Operadores Aritméticos

# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# // Divisão inteira
# % Módulo (resto)
# ** Exponenciação

# Tarefa : Crie dois números (variáveis a e b) e calcule:
# Soma, subtração, multiplicação, divisão, resto (módulo), divisão inteira e exponenciação.

# a = 1
# b = 2
#
# print("Adição (a + b):", a + b)
# print("Subtração (a - b):", a - b)
# print("Multiplicação (a * b):", a * b)
# print("Divisão (a / b):", a / b)
# print("Divisão inteira (a // b):", a // b)
# print("Resto (a % b):", a % b)
# print("Exponenciação (a ** b):", a ** b)

#------------------------------------------

# # Operadores de Comparação
#
# # == Igual a
# # != Diferente de
# # > Maior que
# # < Menor que
# # >= Maior ou igual a
# # <= Menor ou igual a
#
# # Tarefa : Crie duas variáveis, x e y. Depois:
# # Verifique se x é igual a y, maior, menor, etc.
#
# x = 10
# y = 5
#
# a = x == y
# print(a)
# b = x != y
# print(b)
# c = x > y
# print(c)
# d = x < y
# print(d)
# e = x >= y
# print(e)
# f = x <= y
# print(f)
#
# #---------------------------------------------------------
#
# # Operadores Lógicos
#
# # and (E) -> ambos verdadeiros
# # or (Ou)) -> um verdadeiro
# # not (Não) -> inverte
#
# # Exercício: Controle de Acesso a um Sistema
# # Imagine que você está criando um sistema de controle de acesso para um site. O acesso será permitido apenas se as seguintes condições forem atendidas:
# #
# # O usuário é maior de 18 anos (idade >= 18).
# # O usuário é um membro premium ou possui uma senha correta .
# # Você também deve exibir mensagens para as seguintes situações:
# #
# # Caso o usuário seja menor de 18 anos, exiba: "Acesso negado: menor de idade."
# # Caso o usuário seja maior de 18, mas não cumpra as outras condições, exiba: "Acesso negado: permissões insuficientes."
# # Se todas as condições forem atendidas, exiba: "Acesso subsídio!"
#
# idade = 22
# membro_premium = True
# senha_correta = False
#
# if idade < 18:
#     print("Acesso negado!")
# elif membro_premium or senha_correta:
#     print("Acesso concedido!")
# else:
#     print("Acesso negado: permissões insuficientes.")
#
# #-----------------------------------------------------------
#
# # Operadores de Atribuição
# #
# # = Atribuição simples
# # += Incremento
# # -= Decremento
# # *= Multiplicação
# # /= Divisão
# # **= Exponenciação
# # %= Módulo
# #
# # Tarefa : Simular uma conta bancária.
# # Comece com um saldo inicial e
# # faça operações como depósito, saque e cálculo de juros.
#
# saldo = 1000
# print("Saldo inicial: R$", saldo)
# saldo += 200 # Incremento
# print("Depósito R$ 200: R$", saldo)
# saldo -= 100 # Decremento
# print("Saque de R$ 100: R$", saldo)
# saldo *= 1.05 # Juros de 5%
# print("Juros de 5%: R$", saldo)
#
# saldo /= 2 # Divisão
# print("Divisão: R$", saldo)
# saldo %= 100 # Módulo
# print("Módulo: R$", saldo)
# saldo **= 2 # exponenciação
# print("Exponênciação: R$", saldo)
#
# #-----------------------------------------------------------------
#
# # Operadores de Identidade
#
# # is -> É o mesmo objeto?
# # is not -> Não é o mesmo objeto?
#
# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a
#
# print("a é b?", a is b) # False, objetos diferentes
# print("a é c?", a is c) # True, mesmo objeto
# print("a não é b?", a is not b)
#
# #----------------------------------------------------------
#
# # Operadores de Pertinência
# #
# # in	Está presente?
# # not in	Não está presente?
# #
# # Tarefa : Verifique se os elementos estão em uma lista ou string.
#
# frutas = ["maçã", "banana", "laranja"]
# palavra = "praia"
#
# print("Banana está na lista?", "banana" in frutas)
# print("Uva não está na lista?", "uva" not in frutas)
# print("A letra p está na palavra?", "p" in palavra)
# print("A letra z não está na palavra?", "z" not in palavra)
#
# # -----------------------------------------------------

# ESTRUTURA DE DECISÃO

#Escreva um programa que receba uma temperatura e diga se está frio (< 15°C),
#agradável (15°C a 25°C) ou quente (> 25°C).

# temp = int(input("Qual é a temperatura atual? "))
# if temp < 15:
#     print(f"hoje está fazendo {temp}°C. Pegue o agasalho, hoje está frio!")
# elif temp > 15 and temp < 25:
#     print(f"Hoje está fazendo {temp}°C. O clima está agradável, aproveite!")
# elif temp > 25:
#     print(f"Hoje está fazendo {temp}°C. O clima está quente, beba água!")

#-----------------------------------------------------

# Crie um programa que receba duas notas e informe se o aluno foi aprovado
# recuperado ou reprovado (use os critérios do exemplo 3).

# nota1 = float(input("Primeira nota: "))
# nota2 = float(input("Segunda nota: "))
#
# media = (nota1 * nota2) / 2
#
# if media >= 7:
#     print("Aluno aprovado!")
# elif media >= 5:
#     print("Aluno em recuperação!")
# else:
#     print("Aluno reprovado!")

#------------------------------------------------------------

# Faça um programa que pergunte ao usuário sua idade e ele tenha CNH.
# Informe se ele pode dirigir ou não.

idade = int(input("Qual a sua idade? "))
cnh = str(input("Voce tem CNH? Responda: s ou n "))

if idade >= 18 and cnh == s:
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir!")

