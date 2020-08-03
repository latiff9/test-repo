def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzbuz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    return input


number = input('Enter number :')
print(f'{number} is {fizz_buzz(int(number))}')
