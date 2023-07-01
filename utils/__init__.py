
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        is_sort = True
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_sort = False
        if is_sort:
            break
    return arr


if __name__ == '__main__':
    x = bubble_sort([3,3,1,3,5,6,2,34,657,23])
    print(x)
