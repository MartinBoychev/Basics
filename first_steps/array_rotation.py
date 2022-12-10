def rotate(L, d, n):
    k = L.index(d)
    new_lis = []
    new_lis = L[k + 1:] + L[0:k + 1]
    return new_lis


if __name__ == '__main__':
    arr = [2, 3, 4, 5, 6]
    d = int(input("How many rotations would you like?\n")) + 1
    N = len(arr)

    # Function call
    arr = rotate(arr, d, N)
    for i in arr:
        print(i, end=" ")