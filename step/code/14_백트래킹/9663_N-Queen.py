# N-Queen (9663)

N = int(input())

queen = []
ans = 0

def N_queen():
    global ans
    if len(queen) == N:
        ans += 1
        return 
    
    for x in range(1, N+1):
        cnt = 0
        if x in queen:
            continue

        for i in range(len(queen)):
            if len(queen)-i == abs(x-queen[i]):
                cnt += 1
                break
        if cnt > 0:
            continue

        queen.append(x)
        N_queen()
        queen.pop()

N_queen()

print(ans)