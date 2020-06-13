friendships = [('A','B'),
               ('B','C'),
               ('A','C'),
               ('C','D'),
               ('B','F'),
               ('D','E'),
               ('F','E'),
               ('F','J'),
               ('E','H'),
               ('E','G'),
               ('G','H'),
               ('H','I'),
               ('I','J'),
               ('I','L'),
               ('L','M'),
               ('M','N'),
               ('N','O')]

def are_friends(a,b):
    return any(list(map(lambda x: x == (a, b), friendships)))


def common(a,b):
    #list of list - nested represent pairs containing value 'a' or 'b'
    pairs = [list(filter(lambda x: x if person in x and x != (a, b) else '', friendships)) for person in (a,b)]

    friends_of_each = []
    for index in range(len(pairs)):
        # lists containing friends only of values 'a' 'b'
        friends = [friend if friend != a and friend != b else '' for pair in pairs[index] for friend in pair]
        #creating nested list
        friends_of_each.append(friends)

    #returns friends, that are common for both choices 'a' 'b'
    return [b_friend for a_friend in friends_of_each[0] for b_friend in friends_of_each[1] if (a_friend == b_friend != '')]


print(common('L','H'))