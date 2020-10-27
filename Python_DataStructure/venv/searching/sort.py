

def sequencesearch(sequence,target):
    for i in range(len(sequence)):
        if target == sequence[i]:
            return i
    return None


if __name__ == "__main__":
    res = sequencesearch([99,12,33,74,521,13,14],521)
    print(res)
