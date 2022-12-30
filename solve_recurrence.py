from math import log
import re

def solve_recurrence(a, b, k, P):
    '''
    Format: T(n) = aT(n/b)+ f(n)
    where f(n) = O(n^k * log(n)^p)
    Case #1 : if log(a,b) > k, then T(n) = O(n^log(a,b))
    Case #2 : if lag(a,b) == k, then if p>-1, T(n) = O(n^k * log(n)^p+1)
                                    if p =-1, T(n) = O(n^k loglog(n))
                                    if p<-1, T(n) = O(n^k)
    Case #3 : if log(a,b) < k, then if p>=0, T(n) = O(n^k * log(n)^p)
                                    if p<0, T(n) = O(n^k)

    '''
    # Case #1
    if log(a, b) > k:
        return f'O(n^{log(a, b)})'
    # Case #2
    elif log(a, b) == k:
        if P > -1:
            return f'O(n^{k} * log(n)^{P + 1})'
        elif P == -1:
            return f'O(n^{k} * loglog(n))'
        else:
            return f'O(n^{k})'
    # Case #3
    else:
        if P >= 0:
            return f'O(n^{k} * log(n)^{P})'
        else:
            return f'O(n^{k})'



def extract_coefficients(s):
    match = re.match(r"T\(n\) = (\d+)T\(n/(\d+)\) \+ O\(n(?:\^(\d+))?(?: \* log\(n\)\^(\d+))?", s)
    if match:
        a = int(match.group(1))
        b = int(match.group(2))
        if match.group(3) is not None:
            k = int(match.group(3))
        else:
            k = 1
        if match.group(4) is not None:
            p = int(match.group(4))
        else:
            p = 0
        return (a, b, k, p)
    else:
        return None
if __name__ == "__main__":
    print('Input formula like this: ')
    print('formula format: T(n) = aT(n/b) + O(n^k * log(n)^p)')
    s = input("Enter recurrence: \n")
    coefficients = extract_coefficients(s)
    if coefficients is None:
        print("Invalid input")
    else:
        print(f'Solution = {solve_recurrence(*coefficients)}')
        
