# --------------MAIN FUNCTION-------------------
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
def pascal(n):
    pyramid = list()

    for sequence in range(abs(n)):
        pyramid.insert(abs(n), [])

        for i in range(sequence + 1):
            if i == 0 or i == sequence:
                pyramid[sequence].append(1)
            else:
                pyramid[sequence].append(pyramid[sequence - 1][i - 1] + pyramid[sequence - 1][i])
    if n < 0:
        pyramid = list(reversed(pyramid))

    return print_pascal(pyramid)
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------



#---PRINTING FUNCTION NESTED IN MAIN FCTION-----
#-----------------------------------------------
#-----------------------------------------------

def print_pascal(pyramid):
    longest_seq = longest_row(pyramid)

    width = max_width(longest_seq)

    for row in pyramid:
        print(' '.join(row).center(width))
#-----------------------------------------------
#-----------------------------------------------
#-----------------------------------------------



#-----FUNCTIONS NESTED IN PRINTING FUNCTION-----
#-----------------------------------------------
def max_width(longest_seq):
    width = 0
    for digits in longest_seq:
        width += len(digits)
    width = 2 * width - 1
    return width


def longest_row(pyramid):
    longest_seq = pyramid[0]

    for index, seq in enumerate(pyramid):

        if len(seq) > len(longest_seq):
            longest_seq = pyramid[index]

        int_to_string(seq)
    return longest_seq
#-----------------------------------------------
#-----------------------------------------------



#--- int_to string() NESTED IN longest_row()---
def int_to_string(seq):
    for i, number in enumerate(seq):
        seq[i] = str(number)
    return seq
#-----------------------------------------------


#calling pascal triangle
pascal(-10)
