## my solution
def digit_sum(n):
    workinNumber = n
    summatory = 0
    remainder = 0
    while len(str(workinNumber)) > 1:
        rightMostDigit = workinNumber % 10
        summatory += rightMostDigit
        workinNumber /= 10
    else:
        summatory += workinNumber
    
    return summatory    
## other solution find it
def digit_sum_other_Sol(n):
    add = 0
    
    for dig in str(n):
        add += int(dig)
    
    return add