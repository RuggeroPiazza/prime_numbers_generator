"""
The program asks for an integer, takes a numeric interval from 0
to the given number and yields the primes number included in the interval.
"""


def primes(n):
    """INPUT: integer n;
       OUTPUT: yield the prime numbers."""
    for num in range(n + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num


def activate_generator(inp):
    """INPUT: string from the user;
       OUTPUT: integer."""
    primes_generator = primes(inp)
    print("Press ENTER to generate a prime number, 'q' followed by ENTER to quit.")
    while True:
        command = input("")
        if command != 'q':
            try:
                print(primes_generator.__next__())
            except StopIteration:
                print("You've reach the end of the range.")
                break
        else:
            break


def start():
    """INPUT: no input;
       OUTPUT: call next function."""
    print("Choose the end of your interval.")
    while True:
        number = int(input("Type a number > "))
        try:
            activate_generator(number)
        except ValueError:
            print("Input not valid")
        else:
            break


if __name__ == "__main__":
    start()
