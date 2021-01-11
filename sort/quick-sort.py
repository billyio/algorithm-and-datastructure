def quick_sort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr

    ref = arr[0] # or ref = random.choice(arr)
    ref_count = 0

    for ele in arr:
        if ele < ref:
            left.append(ele)
        elif ele > ref:
            right.append(ele)
        else:
            ref_count += 1
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right