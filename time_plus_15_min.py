time_in_hours = int(input())
time_in_minutes = int(input())

minutes_above = 15 - (60 - time_in_minutes)

if -1 < time_in_minutes < 45:
    print(f"{time_in_hours}:{time_in_minutes + 15}")
elif time_in_minutes == 45 and time_in_hours == 23:
    print("0:00")
elif 60 > time_in_minutes > 55 and time_in_hours == 23:
    print(f"0:{minutes_above}")
elif 55 > time_in_minutes > 45 and time_in_hours == 23:
    print(f"0:0{minutes_above}")
elif time_in_minutes == 45:
    print(f"{time_in_hours + 1}:00")
elif 51 > time_in_minutes > 45:
    print(f"{time_in_hours + 1}:0{minutes_above}")
elif time_in_hours == 23 and 60 > time_in_minutes > 45:
    print(f"0:{minutes_above}")
elif 60 > time_in_minutes > 50:
    print(f"{time_in_hours + 1}:{minutes_above}")
elif 50 > time_in_minutes > 45:
    print(f"{time_in_hours + 1}:0{minutes_above}")
else:
    print("Enter valid hour and minutes")






# if time_in_minutes < 45:
#     print(f"{time_in_hours}:{time_in_minutes + 15}")
# elif time_in_hours == 23 and time_in_minutes == 45:
#     print(f"0:0{minutes_above}")
# elif time_in_hours == 23 and time_in_minutes > 45:
#     print(f"0:{minutes_above}")
# elif 15 > minutes_above > 10:
#     print(f"{time_in_hours + 1}:{minutes_above}")
# elif time_in_minutes < 60:
#     print(f"{time_in_hours + 1}:{minutes_above}")
# else:
#     print("Enter valid integer number")