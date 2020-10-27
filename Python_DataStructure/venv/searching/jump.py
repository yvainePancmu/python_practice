import math

def jumpsearch(sequence,target):
    n = len(sequence)
    step = int(math.floor(math.sqrt(n)))
    prev = 0
    while sequence[min(step,n)-1] < target:
        prev = step
        step = step + int(math.floor(math.sqrt(n)))
        if prev > n:
            return None
    while sequence[prev] < target:
        prev = prev + 1
        if prev == min(step,n):
            return None
    if sequence[prev] == target:
        return prev
    else:
        return None

if __name__ == "__main__":
    sequence = [i for i in range(1,10001,2)]
    res = jumpsearch(sequence,521)
    print(res)
