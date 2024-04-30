import textwrap


def menu():
  menu = """
  ============= MENU =============>>

[1] Sacar
[2] Depositar
[3] Extrato
[4] Nova conta
[5] Novo usuário
[6] Listar contas
[S] Sair
   
Obrigado(a) por usar nosso serviços, \n tenha um bom dia!
Dúvidas ou sugestões entre em contato com nosso SAC,\n será um prazer atendê-lo(a)!
  ============= FIM! ===============>>        
=> """
  return input(textwrap.dedent(menu))


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n XXX Ops! Este CPF já se encontra em nosso banco de dados!XXX")
        return

    nome = input("Insira seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Insira seu endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=#=#=Usuário foi criado com sucesso!=#=#=")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n#=#=# Conta criada com sucesso! #=#=#")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nXXX Ops falhou, usuário não encontrado!XXX")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
  
def saque(*, valor, saldo, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor> saldo
    excedeu_limite = valor> limite
    excedeu_saque = numero_saques > limite_saques
    if excedeu_saldo:
       print('XXX Ops! Infelizmente você não tem saldo suficiente.XXX')

    elif excedeu_limite:
       print('XXX Ops! Infelizmente você não tem limite suficiente.XXX')
      
    elif excedeu_saque:
       print('XXX Ops! Infelizmente seu número de saques de hoje excedeu.XXX')
 
    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print('#=#=# Saque realizado com sucesso! Seu dinheiro está disponível.#=#=#')
    else:
            print("XXX Ops Falhou! Por favor informe um número válido.XXX")


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depositou:\tR$ {valor:.2f}\n"
        print("\n#=#=#Sucesso! Seu depósito já está rendendo!\nTenha um bom dia.#=#=#")
    else:
        print("\nXXX Falha! Infelizmente o valor informado é inválido.XXX")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n=*=*=*=*=*=*=* EXTRATO =*=*=*=*=*=*=*")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("\n=*=*=*=*=*=*=*=* FIM! =*=*=*=*=*=*=*=*")


def sistem():
    agencia = "0001"
    usuarios = []
    contas = []
    numero_saques = 0
    limite_saques = 3
    saldo = 0
    limite = 500
    extrato = ""
    
    while True:
        opcao = menu()

        if opcao == "2":
            valor = float(input("Informe o valor que você deseja depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "1":
            valor = float(input("Informe o valor do saque: "))


            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques,
            )
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "5":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "s":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


sistem()