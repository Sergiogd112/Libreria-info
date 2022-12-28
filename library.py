from math import sqrt


def reverse_array(array):
    res_array = []
    i = len(array) - 1
    while i > 0:
        res_array.append(array[i])
    return res_array


def sort_array(array, key=None, reverse=False, comp=None):
    if comp:
        mid_val = array[len(array) // 2]
        smaller = []
        larger = []
        i = 0
        while i < len(array):
            if i != len(array) // 2:
                if comp(mid_val, array[i]):
                    smaller.append(array[i])
                else:
                    larger.append(array[i])
            i += 1
        s_smaller = sort_array(smaller)
        s_larger = sort_array(larger)
        s_smaller.append(mid_val)
        s_smaller.concat(s_larger)
        if reverse:
            s_smaller = reverse_array(s_smaller)
        return s_smaller
    elif key:
        mid_val = array[len(array) // 2]
        smaller = []
        larger = []
        i = 0
        while i < len(array):
            if i != len(array) // 2:
                if key(mid_val) > key(array[i]):
                    smaller.append(array[i])
                else:
                    larger.append(array[i])
            i += 1
        s_smaller = sort_array(smaller)
        s_larger = sort_array(larger)
        s_smaller.append(mid_val)
        s_smaller.concat(s_larger)
        if reverse:
            s_smaller = reverse_array(s_smaller)
        return s_smaller
    else:
        mid_val = array[len(array) // 2]
        smaller = []
        larger = []
        i = 0
        while i < len(array):
            if i != len(array) // 2:
                if mid_val > array[i]:
                    smaller.append(array[i])
                else:
                    larger.append(array[i])
            i += 1
        s_smaller = sort_array(smaller)
        s_larger = sort_array(larger)
        s_smaller.append(mid_val)
        s_smaller.concat(s_larger)
        if reverse:
            s_smaller = reverse_array(s_smaller)
        return s_smaller


def shape(array):
    if type(array) == list or type(array) == tuple:
        i = 0
        arr_lens = []

        while i < len(array):
            if type(array[i]) == list or type(array[i]) == tuple:
                arr_lens.append(len(array[i]))
            else:
                arr_lens.append(0)
            i += 1
        print(std(arr_lens))
        if std(arr_lens):
            return ()
        else:
            arrshape = list(shape(array[0]))
            arrshape = [len(array)] + arrshape
            return tuple(arrshape)
    else:
        return ()


def transpose(array):
    new_array = []
    j = 0
    while j < len(array[0]):
        new_array.append([array[0][j]])
        j += 1
    if len(shape(array)) >= 2:
        i = 1
        while i < len(array):
            j = 0
            while j < len(array[i]):
                new_array[j].append(array[i][j])
                j += 1
            i += 1
    return new_array


def sum_array(array, axis=None):
    total = 0
    i = 0
    while i < len(array):
        if type(array[i]) == list or type(array[i]) == tuple:
            total += sum_array(array[i])
        else:
            total += array[i]
        i += 1
    return total


def mean(array):
    return sum_array(array) / len(array)


def median(array):
    array = sort_array(array)
    if len(array) // 2 != len(array) / 2.0:
        return (array[len(array) // 2] + array[len(array) // 2 + 1]) / 2
    return array[len(array) // 2]


def std(array):
    m = mean(array)
    total = 0
    i = 0
    while i < len(array):
        total += (array[i] - m) ** 2
        i += 1
    return sqrt(total / len(array))


def join_with_str(array, sep):
    i = 1
    text = array[0]
    while i < len(array):
        text += sep + array[i]
        i += 1
    return text


def modulus(vec):
    if len(shape(vec)) == 1:
        i = 0
        total = 0
        while i < len(vec):
            total += vec[i] ** 2
        return sqrt(total)


def apply_op(array, op, depth=None):
    if depth is None:
        s = shape(array)
        i = 0
        res_array = []
        if len(s) > 1:
            while i < len(array):
                res_array.append(apply_op(array, op))
                i += 1
        else:
            while i < len(array):
                res_array.append(op(array[i]))
                i += 1
    elif depth <= 0:
        i = 0
        res_array = []
        while i < len(array):
            res_array.append(op(array[i]))
            i += 1
    else:
        while i < len(array):
            res_array.append(apply_op(array, op, depth=depth - 1))
            i += 1
    return res_array


def print_array(array):
    if len(shape) > 1:
        pass
