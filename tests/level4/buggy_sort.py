"""Custom sorting implementations with bugs."""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Bug: should extend with remaining elements, not just one
    if i < len(left):
        result.append(left[i])
    if j < len(right):
        result.append(right[j])

    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    test_data = [38, 27, 43, 3, 9, 82, 10, 55, 1, 44, 99, 7]
    print(f"Original: {test_data}")
    print(f"Merge sort: {merge_sort(test_data)}")
    print(f"Quick sort: {quick_sort(test_data)}")
    print(f"Expected:   {sorted(test_data)}")

    assert merge_sort(test_data) == sorted(test_data), "Merge sort failed!"
    assert quick_sort(test_data) == sorted(test_data), "Quick sort failed!"
    print("All tests passed!")
