sentence = input('Type random sentence: ').split(' ')
rep_number = int(input('How many times should I repeat each word in your sentence ?: '))

echo_sen = []
while sentence:
    echo_sen.insert(0, rep_number*(sentence.pop() + ' '))

print(' '.join(echo_sen))