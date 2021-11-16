# N과 M(1) (15649)

N, M = map(int, input().split())
seq = []

def seq_generate():
    if len(seq) == M:
        print(' '.join(map(str, seq)))
        return
    
    for n in range(1, N+1):
        if n in seq:
            continue
        seq.append(n)
        seq_generate()
        seq.pop()

seq_generate()