def convertToBase7(num):
    neg = False
    if num == 0:
        return 0
    if num < 0:
        neg = True
        num = abs(num)
    ans = ''
    while num != 0:        
        ans = str(num % 7) + ans
        num = num // 7
    
    if neg:
        ans = '-' + ans
    return ans


print(convertToBase7(100))
print(convertToBase7(-7))
print(convertToBase7(0))
