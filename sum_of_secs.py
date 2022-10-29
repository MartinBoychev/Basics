import  math

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes = math.floor(total_time / 60)
seconds = total_time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
elif total_time < 60:
    print(f"0:{total_time}")
else:
    print(f'{minutes}:{seconds}')
