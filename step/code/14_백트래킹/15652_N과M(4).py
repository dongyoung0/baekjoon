# N과 M(4) (15652)

N, M = map(int, input().split())
seq = []

def seq_generate():
    if len(seq) == M:
        print(' '.join(map(str, seq)))
        return
    
    for n in range(1, N+1):
        if len(seq) > 0 and n < seq[-1]:
            continue
        seq.append(n)
        seq_generate()
        seq.pop()

seq_generate()