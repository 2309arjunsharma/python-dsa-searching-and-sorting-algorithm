def linear_search(arr, target):
    # TODO: Implement this function
    size=len(arr)
    for index in range(0,size):
        if(arr[index]==target):
            return index
    return -1
print(linear_search([3,7,2,5],2))
print(linear_search([1,1,2,1],1))
print(linear_search([],5))
print(linear_search([4,2,8],6))
