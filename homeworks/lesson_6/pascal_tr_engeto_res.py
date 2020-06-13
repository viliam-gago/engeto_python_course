def print_pascal(triangle):
    longest = longest_row(triangle)
    width = max_row_length(longest)

    result = ""
    for row in triangle:
        for c, num in enumerate(row):
            row[c] = str(num)
        result += ' '.join(row).center(width + len(triangle) - 1) + '\n'
    return result


def longest_row(sequence):
    longest = (0, sequence[0])
    for i, row in enumerate(sequence[1:]):
        if len(longest[1]) < len(row):
            longest = (i+1,row)
    return longest[1]


def max_row_length(sequence):
    width = 0
    for item in sequence:
        width += len(str(item))
    return width

##################################################################

def pascal(num_rows):
    triangle = []

    for row in range(num_rows):
        triangle.append([])

        for colum in range(row + 1):
            if colum == 0 or colum == len(triangle[row - 1]):
                triangle[row].append(1)
            else:
                previous = triangle[row - 1]
                triangle[row].append(previous[colum] + previous[colum - 1])
    # return triangle

    print(print_pascal(triangle))
###################################################################

pascal(15)

