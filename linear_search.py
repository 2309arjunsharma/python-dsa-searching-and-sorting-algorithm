def linear_search(arr,target):
    size=len(arr)
    for index in range(0,size):
        if(arr[index]==target):
            return index
    return -1
lst=[10,23,45,70,111]
target=700
result=linear_search(lst,target)
print(result)
