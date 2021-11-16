# N과 M(3) (15651)

N, M = map(int, input().split())
seq = []

def seq_generate():
    if len(seq) == M:
        print(' '.join(map(str, seq)))
        return
    
    for n in range(1, N+1):
        seq.append(n)
        seq_generate()
        seq.pop()

seq_generate()