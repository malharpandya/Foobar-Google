from itertools import combinations
def solution(l):

    # number%3==0 <==> sum_digits(number) %3 == 0.
    # Pick the largest subset of l such that its sum is divisible by 3.
    # Sort the digits in reverse order to get the largest number.
	
    l = sorted(l, reverse = True)
    final_subset = [digit for digit in l if digit%3==0]
    l  = [digit for digit in l if digit%3!=0]

    subset = get_largest_valid_subset(l)
    if subset != -1:
        final_subset += subset
        final_subset = sorted(final_subset, reverse=True)
		
    if not final_subset:
        return 0

    str_final = [str(digit) for digit in final_subset]
    return int(''.join(str_final))
    
# HELPER FUNCTION
def get_largest_valid_subset(l):
    """Given a list of digits (each not dvisble by 3), returns the largest subset whose sum is divisible by 3, and -1 if no such subset exists"""
    
    # Since the input list is in reverse order, the first valid subset reached will also be the largest one.
	# Also, since there is at most 9 digits in l, worst case is 2 ^ 10, which is why this approach is viable.
    for r in range(len(l), 0, -1):
        subsets = list(combinations(l, r))
        for subset in subsets:
            if sum(subset)%3==0: return list(subset)
    return -1
