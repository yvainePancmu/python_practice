def binary_search(sorted_sequence,target):
    left = 0
    right = len(sorted_sequence)-1
    while(left<=right):
        mid = (left+right)//2
        current_point = sorted_sequence[mid]
        if current_point == target:
            return mid
        elif target < current_point:
            right = mid - 1
        else:
            left = mid + 1
    return None

if __name__ == "__main__":
    sorted_sequence = [i for i in range(1,999,2)]
    res = binary_search(sorted_sequence,521)
    print(res)
