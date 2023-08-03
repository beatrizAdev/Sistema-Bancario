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

limite_dep_universitaria = 700

while True:
    if conta == "1" and operacao == "1":
        depositar = ''' ====== Depósito ======'''
        print(depositar)
        deposito = float(input("Deposite o valor que deseja: "))
        print(f"O valor de R${deposito:,.2f} foi depositado na sua Conta Corrente!")
        break
    if conta == "2" and operacao == "1":
        depositar_1 = ''' ====== Depósito ======'''
        print(depositar_1)
        deposito_1 = float(input("Deposite o valor que deseja: "))
        if deposito_1 <= limite_dep_universitaria:
            print(f"O valor de R${deposito_1:,.2f} foi depositado na sua Conta Universitária!")
            break
        else:
            print(f"O valor de R${deposito_1:,.2f} excedeu o limite de R${limite_dep_universitaria} da sua Conta "
                  f"Universitária! \nTente com outro valor.")
            break
