def prime(number):
    check =0
    for i in range(1, number+1):
        if number % i == 0:
            check= check+1
    if check == 2:
        return True
    else:
        return False