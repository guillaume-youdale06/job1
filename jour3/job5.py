for i in range(2, 1001) :
    condition = True
    for y in range(2, i) :
        if i % y == 0 :
            condition = False
    if condition :
        print(i)