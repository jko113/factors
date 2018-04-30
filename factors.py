def factorify(number):

    divisor = 1
    mid = number / 2

    factors = []

    while divisor <= mid:

        if (number % divisor == 0):
            factors.append(divisor)

        divisor += 1

    if number != 1:
        factors.append(number)
    print (factors)
