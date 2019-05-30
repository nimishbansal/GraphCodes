arr = [25, 5, 4, 10, 12, 18, 20, 6]


def partition(arr, i, j):
    value = arr[j]
    # print("value", arr[j])
    ctr = i-1
    # print("ctr", ctr)
    for current_index in range(i, j):
        # print("cmp", arr[current_index], value)
        if arr[current_index] < value:
            ctr += 1
            # print(ctr)
            arr[ctr], arr[current_index] = arr[current_index], arr[ctr]

    arr[ctr + 1], arr[j] = arr[j], arr[ctr + 1]
    return ctr + 1


def quick_sort(arr, i, j):
    if i < j:
        q = partition(arr, i, j)
        print("partition at index", q)
        quick_sort(arr, i, q - 1)
        quick_sort(arr, q + 1, j)


# quick_sort(arr, 0, len(arr) - 1)
# partition(arr, 0, len(arr) - 1)

quick_sort(arr, 0, len(arr) - 1)
