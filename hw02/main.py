def bsearch(data, target):
    first = 0
    last = len(data) - 1
    while first <= last:
        mid = (first + last) // 2
        if data[mid] == target:
            return mid
        elif mid < target:
            first = mid + 1           
        else:
            last = mid - 1
    return None
#example
print(bsearch([1,2,3,4,5], 4))
