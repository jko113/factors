from factors import factorify

while True:
    num = input('What\'s your number? ')
    try:
        num = int(num)
        break
    except:
        print('Invalid input. Please enter an integer.')

factorify(num)