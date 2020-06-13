classes = {'Biology' : ['Adam','Chelsea','Marcus','Oliver','Alex','Sandra','Ann'],
            'Math' : ['Marcus','Alex','Glenn','Samuel','Clara','Chelsea'],
            'PE'  : ['Adam','Tyler', 'Alex','Clara'],
            'Social Sciences': ['Abraham','Marcus','Alex','Glenn','Clara'],
            'Chemistry' : ['Alfred', 'Curt','Oliver','Alex','Tyler','Ann']}

a = []




print(set(classes['Biology'])&set(classes['Math'])&set(classes['PE'])&set(classes['Social Sciences'])&set(classes['Chemistry']))