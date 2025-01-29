import sys;sys.stdin=open('12891_input.txt')


def bt(idx,temp):

    if len(temp) == P:
        temp_pw.append(temp[:])

    for i in range(idx,S):
        temp.append(DNA[i])
        bt(i+1,temp)
        temp.pop()
    
S, P = map(int,input().split())
DNA = list(input().strip())
min_A, min_C, min_G, min_T = map(int,input().split())

temp_pw = []
cnt_lst = []
bt(0,[])

for j in range(len(temp_pw)):

    if temp_pw:
        new_temp_pw = ''.join(temp_pw[j])
        
        A_cnt = new_temp_pw.count('A')
        C_cnt = new_temp_pw.count('C')
        G_cnt = new_temp_pw.count('G')
        T_cnt = new_temp_pw.count('T')

        if A_cnt>=min_A and C_cnt>=min_C and G_cnt>=min_G and T_cnt>=min_T:
            cnt_lst.append(0)

print(len(cnt_lst))