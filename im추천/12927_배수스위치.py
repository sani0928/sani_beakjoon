import sys;sys.stdin=open('12927_input.txt')    


def switch_edison(edison):
    n = len(edison)
    count = 0

    for i in range(n):
        if edison[i] == 'Y':
            count += 1
            for j in range(i,n,i+1):
                if edison[j] == 'Y':
                    edison[j] = 'N'
                else:
                    edison[j] = 'Y'
    for k in edison:
        if k == 'Y':
            return -1
    return count 
edison = list(input())
result = switch_edison(edison)
print(result)

