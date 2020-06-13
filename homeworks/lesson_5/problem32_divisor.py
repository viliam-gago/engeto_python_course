start = int(input('START: '))
stop = int(input('STOP: '))
divisor = int(input('DIVISOR: '))

if divisor == 0:
    print('Cannot divide by zero')
    quit()

numbers = range(start, stop + 1)
answer = []

# for number in numbers:
for number in numbers:
    if number % divisor == 0:
        answer.append(number)

print('Numbers in', numbers, 'divisible by', divisor,':')
print(answer)