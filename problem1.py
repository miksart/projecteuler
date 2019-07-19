def check(n):
    if n % 3 == 0 or n % 5==0:
        return True
    else:
        return False
ansewr=[]
for i in range(1,1000):
    if check(i):
        ansewr.append(i)
print (sum(ansewr))

#July 19, 2019