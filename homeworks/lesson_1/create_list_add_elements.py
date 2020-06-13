candidates = []
print('Candidates at the beginning:' ,candidates)
employees = ['Francis', 'Ann', 'Jacob', 'Claire']
print('Employees at the beginning:' , employees)
candidates.append('Bruno')
candidates.append('Agnes')
print('New names added to candidates:', candidates)
employees.insert(1,candidates[0])
print('New names added to employees:', employees)
