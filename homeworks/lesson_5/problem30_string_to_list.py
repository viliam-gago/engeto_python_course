answer = input('Hello, please write your numbers and press enter to confirm: ')
answer = answer.split(',')
new_list = [int(number.strip(' ')) for number in answer]

print(new_list)
