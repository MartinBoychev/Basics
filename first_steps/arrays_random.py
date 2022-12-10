def rotate(array, d, n):
    p = 1
    while p <= d:
        last = array[0]
        for i in range(n - 1):
            array[i] = array[i + 1]
        array[n - 1] = last
        p = p + 1


def print_array(array, size):
    for i in range(size):
        print(array[i], end=" ")


arr = list(map(int, input("\nEnter the numbers: ").strip().split()))
N = len(arr)
d = int(input("\nHow many rotations would you like? "))

rotate(arr, d, N)
print_array(arr, N)
