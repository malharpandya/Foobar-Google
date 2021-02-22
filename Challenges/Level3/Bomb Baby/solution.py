def solution(x, y):
    m, f = long(x), long(y)
    count = 0
    while min(m, f) != 1:
        a = max(m, f)
        b = min(m, f)
        
        if b < 1:
            return 'impossible'
            
        # For this problem the allocation doesn't matter due to symmetry    
        count += a//b
        m, f = a%b, b
        
    return str(count + max(m, f) - 1)
