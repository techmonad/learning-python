if __name__ == '__main__':
    # Hello Python from Python
    print("Hello from Python")

    # Loops

    for name in ["Rob", "Bob", "Joy"]:
        print(name)

    for n in range(1, 10):
        print(n)

    # Loops with if/else clause
    for n in range(1, 10):
        if n % 2 == 0:
            print("Even " + str(n))
        else:
            print("odd " + str(n))

    even_numbers = [n for n in range(1, 10) if (n % 2 == 0)]
    print(even_numbers)

    # While loop
    number = 1
    while number <= 10:
        print("While loop: " + str(number))
        number += 1

    # While loop with break
    number2 = 1
    while True:
        print("While loop with break   : " + str(number2))
        if number2 > 10:
            break
        number2 += 1
