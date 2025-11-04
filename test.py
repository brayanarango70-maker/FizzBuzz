from fizzbuzz import fizzbuzz

def test_fizzbuzz():
    resultado = []
    for i in range(1, 16):
        if i % 3 == 0 and i % 5 == 0:
            resultado.append("FizzBuzz")
        elif i % 3 == 0:
            resultado.append("Fizz")
        elif i % 5 == 0:
            resultado.append("Buzz")
        else:
            resultado.append(str(i))
    
    # Llamamos a tu función
    # Pero vamos a modificarla para que devuelva una lista (ver siguiente paso)
    assert resultado == fizzbuzz(15)
