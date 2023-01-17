novocalculo=1
while novocalculo==1:
    print("Programa de cálculo de Equações do Segundo Grau\n\n Uma equação do segundo grau é apresentada nesta forma: \n Ax² + Bx + C\n Portanto você deverá inserir no programa as raízes correspondentes aos números localizados nas letras A, B e C\n Atente se aos sinais positivo ou negativo ;)\n\n")
    A = float(input("Letra A = "))
    if A == 0:
      print("Este valor não corresponde a uma Equação do segundo grau")
    else:
        B = float(input("Letra B = "))
        C = float(input("Letra C = "))
        delta = (B * B) - 4 * A * C
        raizdelta = delta ** 0.5        
        x1 = (-(B) + raizdelta)/ 2 * A
        x2 = (-(B) - raizdelta)/ 2 * A
        print("A resolução da equação é ", x1 ," e ", x2)
        novocalculo=int(input("\n\nDeseja realizar outra operação?\nSIM[1] \nFECHAR PROGRAMA[0]\n"))