def check(n):
    if n % 2 == 0:
        return True
    else:
        return False

answer = []
first = 1
secend = 2
while secend < 4000000:
    if check(secend):
        answer.append(secend)
    new = first+secend
    first = secend
    secend = new

print (sum(answer))

#July 19, 2019