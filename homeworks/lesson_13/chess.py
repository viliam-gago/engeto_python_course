def chess(size):
    return '\n'.join([''.join(['#' if (r+p)%2 == 0 else ' 'for p in range(size)]) for r in range(size)])

print(chess(7))