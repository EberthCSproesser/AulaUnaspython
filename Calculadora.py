# def adicao(a, b):
#     return a + b

# def subtracao(a, b):
#     return a - b

# def multiplicacao(a, b):
#     return a * b

# def divisao(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Erro: Divisão por zero"


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
        print("Resultado:", resultado)
        
    elif escolha == '2':
        resultado = num1 - num2
        print("Resultado:", resultado)
        
    elif escolha == '3':
        resultado = num1 * num2
        print("Resultado:", resultado)
        
    elif escolha == '4':
        resultado = num1 / num2
        print("Resultado:", resultado)
        
else:
    print("Escolha inválida. Por favor, escolha uma operação válida.")

