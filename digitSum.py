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