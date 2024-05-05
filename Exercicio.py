#Neste código podemos ver em prática as estruturas condicionais if, else e elif.

#1 - Complete a estrutura condicional para que o usuário possa acessar todas as operações.
#2 - Existe um erro neste código, analise o código novamente para encontrar este erro.

print("Bem-vindo à calculadora!")
print("Operações disponíveis:")
print("1. Adição (+)")
print("2. Subtração (-)")
print("3. Multiplicação (x)")
print("4. Divisão (/)")

escolha = input("Escolha a operação (1/2/3/4): ")

if escolha in ('1', '2', '3', '4'):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = num1 + num2
        print("Resultado da soma é:", resultado)

####################################################################
 
    elif escolha == '4':
        resultado = num1 / num2
        print("Resultadoda divisão é:", resultado)
        
else:
    print("Escolha inválida. Por favor, escolha uma operação válida.")
