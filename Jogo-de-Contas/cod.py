import random

print("Bem-vindo ao jogo de contas!")
nome = input("Qual seu nome? ")
quantidade_perguntas = random.randint(1, 10)
print(f"\nVocê terá {quantidade_perguntas} desafios. Boa sorte!\n")

for _ in range(quantidade_perguntas):
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    print(f"{a} + {b} = ?")
    resposta = int(input("Digite o resultado: "))

    while resposta != a + b:
        print("Resposta errada! Tente novamente.")
        resposta = int(input("Digite o resultado: "))

print("\nTodas as respostas estão corretas!")
print(f"Você venceu! Parabéns {nome:=^20}")
