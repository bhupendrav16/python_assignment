def single_digit(n):
    if n== 0:
        return 0 
    if n % 9 == 0:
        return 9 
    else:
        return ( n % 9)

    # s = 0
    # while ( n  > 0 or s > 9):
    #     if n == 0 :
    #         n = s 
    #         s = 0
    #     s += n% 10 
    #     n = n//10
    # return s
n = int(input())
print(single_digit(n))


