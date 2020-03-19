def merge_sort(unsorted):
    length = len(unsorted)
    if length == 1:
        # A list of one is already sorted
        return unsorted
    half = length / 2
    part_a = unsorted[:half]
    part_b = unsorted[half:]
    sorted_a = merge_sort(part_a)
    sorted_b = merge_sort(part_b)
    return merge(sorted_a, sorted_b)


def merge(part_a, part_b):
    sorted_array = []
    while len(part_a) > 0 and len(part_b) > 0:
        if part_a[0] > part_b[0]:
            sorted_array.append(part_b.pop(0))
        else:
            sorted_array.append(part_a.pop(0))

    while len(part_a) > 0:
        sorted_array.append(part_a.pop(0))

    while len(part_b) > 0:
        sorted_array.append((part_b.pop(0)))
    return sorted_array
