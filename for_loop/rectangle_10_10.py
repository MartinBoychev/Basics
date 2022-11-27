n = int(input())
b = str(" -")
c = str("|")
print(f"+{b * (n - 2)} +")
for _ in range(0, n - 2):
    print(f"{c}{b * (n - 2)} {c}")
print(f"+{b * (n - 2)} +")