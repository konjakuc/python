def binary_search(list_sort, size, target):
    start = 0
    end= size-1
    while start <= end:
        mid = (start+end)//2
        if target < list_sort[mid]:
            end = mid-1
        elif target > list_sort[mid]:
            start = mid+1
        else:
            return mid
    else:
        return  -1
print(binary_search([1,2,3,4,5,6],6,7))