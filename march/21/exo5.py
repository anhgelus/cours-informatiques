def fonction(l1: list[int], l2: list[int]):
    maxLen = l1 if len(l1) >= len(l2) else l2
    minLen = l1 if len(l1) <= len(l2) else l2
    l = []
    for i in range(len(minLen)):
        l.append(maxLen[i]+minLen[i])
    if len(maxLen) == len(minLen):
        return l
    return l + [maxLen[i] for i in range(len(minLen)-1,len(maxLen))]
