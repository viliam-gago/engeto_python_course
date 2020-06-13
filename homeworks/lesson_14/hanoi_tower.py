def move(f,t):
    print('Move disc from {} to {}!'.format(f,t))

move('A', 'C')

def moveVIA(f,v,t):
    move(f,v)
    move(v,t)

#n number of discs
#f from position
#h helper position
#t target position

def hanoi(n,f,h,t):
    if n==0:
        pass
    else:

        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

hanoi(4, "A", "B", "C")