list_ = [1, 2, 3, 4]


def _func(x):
    print(x)
    return x+1


new_list = []

for i in list_:
    new_list.append(_func(i))

# res = list(map(_func, list_))

print(new_list)
