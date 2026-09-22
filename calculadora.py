def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b   
 
def divisao(a,b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def calculadora():
    print("===Calculadora===")

    while True:
        print("\nEscolha a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == '5':
            print("Saindo da calculadora...")
            break

        if opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if opcao == '1':
                    resultado = soma(num1, num2)
                    print(f"Resultado: {resultado}")
                elif opcao == '2':
                    resultado = subtracao(num1, num2)
                    print(f"Resultado: {resultado}")
                elif opcao == '3':  
                    resultado = multiplicacao(num1, num2)
                    print(f"Resultado: {resultado}")
                elif opcao == '4':  
                    resultado = divisao(num1, num2)
                    print(f"Resultado: {resultado}")
            except ValueError:
                print("Erro: Por favor, digite um número válido.")
        else:
            print("Opção inválida. Tente novamente.")

#Execute a Calculadora
if __name__ == "__main__":
    calculadora()
