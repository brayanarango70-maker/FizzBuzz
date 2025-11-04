def fizzbuzz(n):
    resultado = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            resultado.append("FizzBuzz")
        elif i % 3 == 0:
            resultado.append("Fizz")
        elif i % 5 == 0:
            resultado.append("Buzz")
        else:
            resultado.append(str(i))
    return resultado

# Ejecutar solo si es el programa principal
if __name__ == "__main__":
    for item in fizzbuzz(1000):
        print(item)
