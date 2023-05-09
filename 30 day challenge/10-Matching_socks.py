
def sockMerchant(ar):
    counts = {}
    for num in ar:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    pairs = 0
    for count in counts.values():
        pairs += count // 2
    return pairs
    
arr = input().split(",")
print(sockMerchant(arr))
