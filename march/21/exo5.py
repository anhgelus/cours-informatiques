def fonction(l1: list[int], l2: list[int]):
    max_len = l1 if len(l1) >= len(l2) else l2
    min_len = l1 if len(l1) <= len(l2) else l2
    l = []
    for i in range(len(min_len)):
        l.append(max_len[i]+min_len[i])
    if len(max_len) == len(min_len):
        return l
    return l + [max_len[i] for i in range(len(min_len)-1,len(max_len))]
