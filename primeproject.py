#var input
input_set = range(1,101)
degree = 3

#removing 0 and 1 from input_set
set = [i for i in input_set if i !=0 and i !=1]

#temp set for loop
work_set = ([], set)

#finds numbers prime in respect to their specific set
def prime_maker(x):
    set_np1 = []
    m = list(x[1])
    for i in m:
        for j in range(m[0],i):
            if j in m[0:-1]:
                if i>1:
                    if i % j == 0:
                        set_np1.append(i)
                        break
    mesh_up = set_np1 + list(x[0])
    set_p1 = [i for i in set if i not in mesh_up]
    x = (set_p1, set_np1)
    return x

def prime_loop(x):
    for k in range(degree):
        x = prime_maker(x)
    return x

print(prime_loop(work_set)[0])
print(prime_loop(work_set)[1])
