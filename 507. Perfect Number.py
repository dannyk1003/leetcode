def checkPerfectNumber(num):
    if num <= 1:
        return False
    
    total = 1
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            total += i
            if i != num // i:
                total += num // i
    if total == num:
        return True
    return False


print(checkPerfectNumber(28))
print(checkPerfectNumber(7))
print(checkPerfectNumber(99999993))