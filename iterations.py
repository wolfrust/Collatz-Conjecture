from sys import exit as die
from sys import argv

to_test = int(argv[1])
alliters = {}

def even(number):
    if number % 2 == 0:
        return True
    else:
        return False

while True:

    try:
        num = to_test
        iters = 0

        while True:

            if num == 1:
                if to_test % 1000 == 0:
                    print(to_test)
                try:
                    alliters[str(iters)] += 1
                except KeyError:
                    alliters[str(iters)] = 1
                if to_test == int(argv[2]):
                    raise KeyboardInterrupt
                to_test += 1
                break

            if even(num):

                num /= 2

            else:

                num = (3 * num) + 1

            iters += 1
    except KeyboardInterrupt:
        print(f"Stopping at {to_test}")
        open('iterations.dict', 'w').write(str(alliters))
        die()
