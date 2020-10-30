def found(x, lst):
    lst.remove(x)
    lf = 0
    rh = len(lst)-1
    while rh - lf > 1:
        mid = (lf + rh) // 2
        if lst[mid] < x:
            lf = mid
        else:
            rh = mid
    if lst[rh] == x:
        return True
    return False


def bubble_sort(lst):
    length = len(lst) - 1
    for i in range(length):
        for j in range(length - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst


source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
sorted_list = source_list.copy()
sorted_list = bubble_sort(sorted_list)
#sorted_list.sort()
res_list = [source_list[i] for i in range(len(source_list)) if not found(source_list[i], sorted_list[:])]
print(res_list)