def get_user_input():
    try:
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        operation = input("Elija una operacion (+, -, *, /) o escriba 'exit' para salir: ")
        return num1, num2, operation
    except ValueError:
        print("Input invalido. Por favor ingrese numeros.")
        return get_user_input()

def ejecutar_operacion(callback):
    result = callback()
    print("Resultado:", result)

def calc_operation(operation, num1, num2):
    if operation == '+':
        result = lambda: num1 + num2
    elif operation == '-':
        result = lambda: num1 - num2
    elif operation == '*':
        result = lambda: num1 * num2
    elif operation == '/':
        result = lambda: num1 / num2
    else:
        result = "Operacion invalida"
    return result

def main():
    while True:
        user_input = get_user_input()

        if user_input[2].lower() == 'exit':
            print("Salir.")
            break

        print("\nCalculando...")
        operations = ["+", "-", "*", "/"]
        if user_input[2] in operations:
            ejecutar_operacion(user_input, calc_operation(user_input[2], user_input[0], user_input[1]))
        else:
            print("Operacion invalida. Seleccione (+, -, *, /) o escriba 'exit' para salir.")

if __name__ == "__main__":
    main()


