from random import *


def naive_algorithm( num):
    product = 0
    n = len(num)
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
    for i in range(len(n)):
        if n[i] > n[index1]:
            index1 = i
    if index1 == 0:
        index2 = 1
    else:
        index2 = 0

    for j in range( len(n)):
        if n[j] > n[index2] and j != index1:
            index2 = j
    print(index1, index2)

    return n[index1] * n[index2]


def stress_test(x, y):
    ok = True
    while ok:
        n = randint(2, x)
        array = []

        for i in range(n):
            array.append(randint(0, y))
        print(array[0:])

        result_1 = naive_algorithm(array)
        result_2 = fast_naive_algorithm(array)

        if result_1 == result_2:
            print('OK')
        else:
            print("Wrong answer", result_1, result_2)
            ok = False
    return




if __name__ == "__main__":
    print(stress_test(2, 1))
