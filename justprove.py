
to_test = 1

def even(number):
    if number % 2 == 0:
        return True
    else:
        return False

while True:

    num = to_test

    while True:

        if num == 4:
            if to_test % 1000 == 0:
                print(f"{to_test / 1000}K")
            to_test += 1
            break

        if even(num):

            num /= 2

        else:

            num = (3 * num) + 1
