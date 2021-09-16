from sys import argv
from sys import exit as die

to_test = int(argv[1])
out = open(argv[3], 'w')

def even(number):
    if number % 2 == 0:
        return True
    else:
        return False

while True:

    try:

        path = []
        num = to_test

        while True:

            path.append(num)

            if num == 1:

                out.write(str(path) + '\n')

                if to_test % 500 == 0:
                    print(to_test)

                if to_test == int(argv[2]):
                    raise KeyboardInterrupt

                to_test += 1
                break

            if even(num):

                num /= 2

            else:

                num = (3 * num) + 1

    except KeyboardInterrupt:
        print(f"Stopping @ {to_test}")
        print(f"Data written to {argv[3]}")
        out.close()
        die()
