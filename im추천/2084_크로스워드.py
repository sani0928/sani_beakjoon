import sys; sys.stdin = open('2084_input.txt')





# a 가만히 놔두고 b 왼쪽부터 오른쪽 끝까지
# 두 글자가 같아지는 곳에서 정지하고 출력
a,b = input().split()

n=len(a)
m=len(b)

for i in range(n):
    for j in range(m):

        if a[i] == b[j]:
    
            arr = [['.' for _ in range(n)] for _ in range(m)]

            arr[j][:n] = list(a)

            for r in range(m):
               arr[r][i] = b[r]

            for c in arr:
                print(''.join(c))
            sys.exit()


            
         


            
        
        

        