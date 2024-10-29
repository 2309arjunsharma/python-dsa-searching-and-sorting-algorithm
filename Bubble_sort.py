def bubble_sort(lst):
    # Your code goes here
    n=len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
    
sorted_list=[64,34,25,12,22,11]
result=bubble_sort(sorted_list)
print(result)
unsorted_list=[12,24,11,34,90,22]
