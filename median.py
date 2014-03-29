def median(lst):
    median = 0.0
    list_len = len(lst) 
    
    if list_len == 1:
        median = lst[0]
        return median
    
    temp = sorted(lst)
    index = list_len / 2
    
    if list_len % 2 != 0:
        median = temp[index]
    else:
        ##indices of the middle two elements
        median = (temp[index] + temp[index - 1]) / 2.0
    
    return median