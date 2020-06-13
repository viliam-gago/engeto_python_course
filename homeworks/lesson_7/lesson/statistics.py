def my_sum(sequence):
    total = 0
    for number in sequence:
        total += number
    return total


def my_count(sequence):
    count = 0
    searched = input('Please enter a number you want to find: ')
    for number in sequence:
        if number == int(searched):
            count += 1
    return count, searched


def my_mean(sequence):
    total = my_sum(sequence)
    length = len(sequence)
    return total/length


def modus(sequence):
    counts = {}
    b_key = 0
    for number in sequence:
        counts[number] = counts.setdefault(number, 0) + 1

    for key, value in counts.items():
        if value > b_key:
            b_key = key
    return b_key


def median(sequence):
    s_sequence = sorted(sequence)
    if len(sequence) % 2 == 0:
        middle_mean = (s_sequence[len(s_sequence) // 2] + s_sequence[len(s_sequence) // 2 - 1]) / 2
        print(s_sequence[len(s_sequence) // 2])
        print(s_sequence[len(s_sequence) // 2 - 1])
        return middle_mean
    else:
        return s_sequence[len(s_sequence) // 2]




def statistics(sequence):
    print('What you want to calculate (select an operation or "q" to quit)?')
    print('| SUM | COUNT | MEAN | MODUS| MEDIAN |')
    choice = input().lower()

    if choice == 'sum':
        total = my_sum(sequence)
        print('The sum of typed sequence is', total)

    elif choice == 'count':
        answer = my_count(sequence)
        print('Number', str(answer[1]), 'occurs', str(answer[0]) + 'x in given sequnece.')

    elif choice == 'mean':
        mean = my_mean(sequence)
        print('Mean of given sequence is', mean)

    elif choice == 'modus':
        m = modus(sequence)
        print('Modus of given sequence is', m)

    elif choice == 'median':
        m = median(sequence)
        print('Median of given sequence is', m)
    elif choice == 'q':
        quit()

statistics([1,2,3,4])