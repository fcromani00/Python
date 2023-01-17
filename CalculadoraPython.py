#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

novaoperacao=1
while novaoperacao == 1:
    print("=====CALCULADORA======\n Coloque os dois números para fazer a operação matemática")
    N1 = float(input("Digite um número: \n"))

    print("Digite a Operação que você deseja fazer ")
    print("[+] Soma \n")
    print("[-] Subtração \n") 
    print("[/] Divisão \n")
    print("[*] Multiplicação \n ")
    operacao = input("Insira apenas um destes sinais \n\n")
    N2 = float(input("Digite o segundo número: \n"))
    if operacao == "+":
      resultado = N1+N2
    elif operacao == "-":
      resultado = N1-N2
    elif operacao == "*":
      resultado = N1*N2
    elif operacao == "/":
      resultado = N1/N2
    else: 
      print("Você não inseriu um operador válido: \n\n")
    print(N1, operacao, N2 ,"=", resultado,"\n\n\nDeseja fazer outra operação?")
    novaoperacao = int(input("Nova operação [1]\nSair da Calculadora [0]\n"))

