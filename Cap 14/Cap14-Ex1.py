def merge_list_with_both_elements(xs, ys):
    """ Create a list with both elements from lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            return result

        if xs[xi] == ys[yi]:
            result.append(xs[xi])
            xi +=1
            yi += 1
        elif xs[xi] > ys[yi]:
            yi +=1
        else:
            xi+=1


def elements_only_from_the_first_list(xs, ys):
    """ Take elements only from the fisrt list """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.append(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] == ys[yi]:
            yi += 1
            xi += 1
        elif xs[xi] < ys[yi]:
            if result.count(xs[xi]) == 0:
                result.append(xs[xi])
            xi += 1
        else:
            yi+=1


def elements_only_from_the_second_list(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if yi >= len(xs):
            return result          # And we're done.

        if xi >= len(ys):
            result.append(ys[yi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] == ys[yi]:
            yi+=1
            xi += 1
        elif xs[xi] > ys[yi]:
            if result.count(ys[yi]) == 0:
                result.append(ys[yi])
            yi+=1
        else:
            xi+=1


def either_in_list(xs, ys):
    """Create a list with elements of either list 1 or list 2"""
    result = []
    aux = []
    aux.extend(xs)
    aux.extend(ys)
    aux.sort()
    last_word = ""
    for i in range(len(aux)):
        if last_word != aux[i]:
            result.append(aux[i])
            last_word = aux[i]
    return result


def bagdiff(xs, ys):
    """Make a bagdiff"""
    result = xs
    for x in ys:
        if result.count(x)>0:
            result.remove(x)
    return result




list1 = ["now","is", "t", "time","a", "b"]
list2 = ["now","is","magic", "time", "c", "t"]
list3 = [5,7,11,11,11,12,13]
list4 = [7,8,11]


list1.sort()
list2.sort()

print(list1, list2)

print(merge_list_with_both_elements(list1, list2))
print(elements_only_from_the_first_list(list1, list2))
print(elements_only_from_the_second_list(list1, list2))
print(either_in_list(list1, list2))
print(bagdiff(list3, list4))