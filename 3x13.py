
# 3x+1 = 3(x+(1/3))

to_test = 1

def even(number):
    if number % 2 == 0:
        return True
    else:
        return False

while True:

    num = to_test

    while True:

        if num == 1:
            print(to_test)
            to_test += 1
            break

        if even(num):

            num /= 2

        else:

            num = 3 * (num + (1/3))
