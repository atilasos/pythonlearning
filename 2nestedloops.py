i = 0
j = 0
lst = [2, 5, 3, 8, 11, 5]
counter = 0
for i in range(0, len(lst)):
    counter += 1
    for j in range(0, len(lst)):
        counter += 1
        if i != j and lst[i] == lst[j]:
            print 'index', i, lst[i], 'index', j, lst[j]
        else:
            print 'nada'
print counter
