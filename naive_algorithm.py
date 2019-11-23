def naive_algorithm(n, num):
    product = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                if product < num[i] * num[j]:
                    product = num[i] * num[j]

    return product


def opt_naive_algorithm(n, num):
    product = 0
    for i in range(n):
        for j in range(i+1, n):
            product = max(product, num[i] * num[j])

    return product


def fast_naive_algorithm(n):
    index1 = 0
    for i in range(1, len(n)):
        if n[i] > n[index1]:
            index1 = i
    if index1 == 0:
        index2 = 1
    else:
        index2 = 0

    for j in range(1, len(n)):
        if n[j] > n[index2] and j != i:
            index2 = j

    return n[index1] * n[index2]

print(fast_naive_algorithm([2,1]))
