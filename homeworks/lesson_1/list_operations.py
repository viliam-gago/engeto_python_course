candidates = ['Bruno', 'Agnes']
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire']

#removed Bruno
candidates.remove('Bruno')
print('Bruno removed from candidates:', candidates)

#Agnes multiply
candidates = candidates*3
print('Repetition of Agnes in the candidate list:', candidates)

#joining lists
employees.extend(candidates)
print('Joined candidates and employees:', employees)

#indexes
print('On index 2 is:', employees[2])
print('On index',len(employees) - 1,'is:',employees[-1])

