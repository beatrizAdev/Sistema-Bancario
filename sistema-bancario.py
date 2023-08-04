menu = '''
========= Sistema Bancário ========
[1]Conta Corrente \n[2]Conta Universitária \n[3]Sair '''
print(menu)
conta = str(input("Digite a opção da sua conta: "))

menu_1 = ''' 
========= Escolha a operação =========
[1]Depósito \n[2]Saque \n[3]Extrato \n[4]Cancelar operação'''
print(menu_1)
operacao = str(input("Digite a operação que deseja: "))

saldo = 0
limite_universitaria = 700

while True:
    if conta == "1" and operacao == "1":
        depositar = ''' ====== Depósito ======'''
        print(depositar)
        deposito = float(input("Deposite o valor que deseja: \n"))
        print(f"O valor de R${deposito:,.2f} foi depositado na sua Conta Corrente!")
    break
while True:
    if conta == "2" and operacao == "1":
        depositar_1 = ''' ====== Depósito ======'''
        print(depositar_1)
        deposito_1 = float(input("Deposite o valor que deseja: \n"))
        if deposito_1 <= limite_universitaria:
            print(f"O valor de R${deposito_1:,.2f} foi depositado na sua Conta Universitária!")
        else:
            print(f"O valor de R${deposito_1:,.2f} excedeu o limite de R${limite_universitaria} da sua Conta "
                  f"Universitária! \nTente com outro valor.")

    if conta == "2" and operacao == "2":
        sacar = ''' ====== Saque ======'''
        print(sacar)
        saque = float(input("Qual o valor que deseja sacar? \n"))
        if saque <= limite_universitaria:
            print(f"Sacando o valor de R${saque:,.2f} \n..............................\nOperação realizada com sucesso.")
        elif saque > limite_universitaria:
            print("Operação inválida. Você não tem saldo suficiente.")

            print(sacar)
            saque_2 = float(input("Tente com outro valor: "))

            if saque_2 > limite_universitaria:
                print("Erro na Operação. Você não tem saldo suficiente. \nPor ter muitas tentativas de saque, "
                      "Volte ao Menu Principal.")
            else:
                print(f"Sacando o valor de R${saque_2:,.2f} \n.........................\nOperação realizada com sucesso.")
    break
