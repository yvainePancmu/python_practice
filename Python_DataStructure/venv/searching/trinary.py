def ternary_search(sorted_list,target):
    left = 0
    right = len(sorted_list)-1
    while(left<=right):
        third1 = (right-left)//3+left
        third2 = 2*(right-left)//3+left
        if(sorted_list[third1]==target):
            return third1
        elif(sorted_list[third2]==target):
            return third2
        elif(target<sorted_list[third1]):
            right = third1
        elif(target>sorted_list[third2]):
            right = third2+1
        else:
            left = third1+1
            right = third2-1
    return None
