inicio = int(input("ingresa el numero de inicio: "))
fin = int(input("ingresa el numero final: "))

def fizzbuzz():
    for i in range(inicio, fin +1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    
fizzbuzz()
