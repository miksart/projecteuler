result = []
def prime(number):
    check =0
    for i in range(1, number+1):
        if number % i == 0:
            check= check+1
    if check == 2:
        return True
    else:
        return False

def factor(n):
    for i in range(2, int(n**0.5)):
        if n % i == 0 and prime(i):
            result.append(i)
    return result

print (factor(600851475143))

#July 19, 2019
#MIKSA