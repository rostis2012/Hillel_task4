# Tuple
# task1
tuple_a = (1, 2, 3, 4, 5)
tuple_b = (4, 5, 6, 7, 8)
tuple_c = (4, 5, 6, 7, 8, 9, 10, 11)
tuple_d = tuple_a + tuple_b + tuple_c
print('Tuple_Task #1\n', 'tuple_d = ', tuple_d)

# task2
res = []
for item in tuple_d:
    count = tuple_d.count(item)
    if count > 1:
        _temp_t = (item, count)
        res.append(_temp_t)
res = tuple(res)
print('Tuple_Task #2\n', 'res = ', res)

# task3
res = []
_temp_item_list = []
for item in tuple_d:
    count = tuple_d.count(item)
    if count > 1 and _temp_item_list.count(item) < 1:
        _temp_item_list.append(item)
        _temp_index = []
        for index1, item1 in enumerate(tuple_d, 0):
            if item1 == item:
                _temp_index.append(index1)
        _temp_index_tuple = tuple(_temp_index)
        _temp_result = (item, _temp_index_tuple)
        res.append(_temp_result)
res_tuple = tuple(res)
print('Tuple_Task #3\n', 'res = ', res_tuple)

# List
# task1
list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_c = list_a + list_b
print('List_Task #1\n', 'list_c = ', list_c)

# task2
list_c2 = []
count = len(list_a)
r = list(range(count))
for index, item in enumerate(r, 0):
    list_c2.append(list_a[index])
    list_c2.append(list_b[index])
print('List_Task #2\n', 'list_c2 = ', list_c2)

# task3
list_c_a = []
list_c_b = []
for index, item in enumerate(r, 0):
    if list_a[index] % 2 == 0:
        list_c_a.append(list_a[index])
    if list_b[index] % 2:
        list_c_b.append(list_b[index])
print('List_Task #3\n', 'list_c_a = ', list_c_a, '\n', 'list_c_b = ', list_c_b)

# task4
list_d = list_c[:]
list_d.reverse()
print('List_Task #4\n', 'list_d = ', list_d)

# Task5
res = []
count = len(list_c)
r = list(range(count))
for index, item in enumerate(r, 0):
    res.append(list_c[index] + list_d[index])
print('List_Task #5\n', 'res = ', res)

# Task6
list_f = [9, 3, 4, 1, 8, 6, 5, 2, 0, 7]
res1 = list_f[:]
res2 = list_f[:]
res1.sort()
res2.sort(reverse=True)
print('List_Task #6\n', 'res1 = ', res1, '\n', 'res2 = ', res2)

# Task7
res = []
count = len(list_c)
r = list(range(count))
for index, item in enumerate(r, 0):
    _temp_tuple = (list_c[index], list_d[index])
    res.append(_temp_tuple)
print('List_Task #7\n', 'res = ', res)
