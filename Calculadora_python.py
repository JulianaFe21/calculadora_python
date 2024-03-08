def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y
 
def divide(x,y):
    return x / y
    
print("\n Selecione a opção desejada: \n") # \n => quebra de linha
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

#função input para o usuario digitar a opção
escolha = input("\n Digite a opção desejada: (1/2/3/4): ")

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))

#adicione as condicionais para cada escolha
if escolha == '1':
    print("\n")
    print(num1, "+", num2 , "=", add(num1, num2))
    print("\n")
    
elif escolha == "2":
    print("\n")
    print(num1, "-", num2, "=", subtract(num1, num2)) 
    print("\n")

elif escolha == "3":
    print("\n")
    print(num1, "*", num2, "=", multiply(num1, num2)) 
    print("\n")
    
elif escolha == "4":
    print("\n")
    print(num1, "/", num2, "=", divide(num1, num2)) 
    print("\n")
    
else:
    print("Opção inválida. Tente novamente.")       
    