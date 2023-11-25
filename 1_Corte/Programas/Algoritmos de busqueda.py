def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def search_element(sorted_arr, n, element):
    i = 0
    start = 0
    end = n - 1
    while i < n:
        middle = (start + end) // 2
        if sorted_arr[middle] == element:
            return True
        elif sorted_arr[middle] < element:
            start = middle + 1
        else:
            end = middle - 1
        i += 1
    return False

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(arr)
    element_to_be_searched = 11
    if search_element(arr, n, element_to_be_searched):
        print(element_to_be_searched, "is found")
    else:
        print(element_to_be_searched, "is not found")