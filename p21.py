def mergeTwoLists(list1:list, list2:list):
    list1.extend(list2)
    list1.sort()
    return list1

print(mergeTwoLists([1,2,3,7,8,10],[2,3,6,7,8]))