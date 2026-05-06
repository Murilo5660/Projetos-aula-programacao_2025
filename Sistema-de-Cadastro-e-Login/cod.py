banco = {
    "A": "123",
    "B": "456",
    "C": "789"
}

while True:
    print("\n=== Sistema de Cadastro e Login ===")
    usuario = input("Digite seu nome de usuário: ").strip()
    senha = input("Digite sua senha: ").strip()

    if usuario in banco:
        if banco[usuario] == senha:
            print(f"Bem-vindo de volta, {usuario}!")
            break
        else:
            print("Senha incorreta. Tente novamente.")
    else:
        banco[usuario] = senha
        print(f"Usuário '{usuario}' cadastrado com sucesso!")
        print(f"Bem-vindo, {usuario}!")
        break
