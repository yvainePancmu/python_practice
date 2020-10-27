#插值搜索
def insert_search(sequence,target):
    left = 0
    right = len(sequence)-1
    while(left<=right):
        #非常非常重要
        midpoint = left + ((target-sequence[left])*(right-left))//(sequence[right]-sequence[left])
        if midpoint<0 or midpoint>=len(sequence):
            return None
        current_item = sequence[midpoint]
        if current_item == target:
            return midpoint
        elif target <current_item:
            right = midpoint - 1
        else:
            left = midpoint+1
    return None
