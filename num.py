import random

num = random.randint(0,100)


while True:
    num1 = float(input("Digite um número de 0 a 100:"))
    if num1 > 100:
        print("Número inválido")
    elif num1 > num:
        print('O número que você digitou é maior')
    elif num1 < num:
        print('O número que você digitou é menor')
    else:
        print("Você acertou o número")
        break