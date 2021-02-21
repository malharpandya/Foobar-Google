def solution(n):

    n = int(n)
    count = 0
    
    while n!= 1:
        if n%2==0:
            n /= 2
            count += 1
        else:
            # Choosing multiple of 4 is always better/equal except when n == 3
            # 3 -> 4 -> 2 -> 1 (4) >>>>>> 3 -> 2 -> 1 (3)
            if n == 3:
                return count + 2
            if (n-1)%4==0:
                n = (n-1)/4
            else:
                n = (n+1)/4
            count += 3
    return count
