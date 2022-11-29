money = float(input())

total_sum = money
coins = 0

while total_sum != 0:
    if 2 <= total_sum:
        coins += 1
        total_sum -= 2
        total_sum = round(total_sum, 2)
    else:
        if 1 <= total_sum:
            coins += 1
            total_sum -= 1
            total_sum = round(total_sum, 2)
        else:
            if 0.5 <= total_sum:
                coins += 1
                total_sum -= 0.5
                total_sum = round(total_sum, 2)
            else:
                if 0.2 <= total_sum:
                    coins += 1
                    total_sum -= 0.2
                    total_sum = round(total_sum, 2)
                else:
                    if 0.1 <= total_sum:
                        coins += 1
                        total_sum -= 0.1
                        total_sum = round(total_sum, 2)
                    else:
                        if 0.05 <= total_sum:
                            coins += 1
                            total_sum -= 0.05
                            total_sum = round(total_sum, 2)
                        else:
                            if 0.02 <= total_sum:
                                coins += 1
                                total_sum -= 0.02
                                total_sum = round(total_sum, 2)
                            else:
                                if 0.01 <= total_sum:
                                    coins += 1
                                    total_sum -= 0.01
                                    total_sum = round(total_sum, 2)
                            if total_sum == 0:
                                break
print(coins)