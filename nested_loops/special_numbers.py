n = int(input())

for i in range(1, 10):
    for u in range(1, 10):
        for y in range(1, 10):
            for t in range(1, 10):
                if n % i == 0 and n % u == 0 and n % y == 0 and n % t == 0:
                    print(f"{i}{u}{y}{t}", end=" ")
