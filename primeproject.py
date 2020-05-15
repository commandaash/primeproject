#var input
input_set = range(1,101)
degree = 2

#removing 0 and 1 from input_set
set = [i for i in input_set if i !=0 and i !=1]

#finds numbers prime in respect to their specific set
def prime_maker(set):
    set_np1 = []
    for i in set:
        for j in range(2, i):
            if j in set:
                if i>1:
                    if i % j == 0:
                        set_np1.append(i)
                        break
    set_p1 = [i for i in set if i not in set_np1]
    return set_p1, set_np1

# if degree > 1:


print(prime_maker(set)[0])
