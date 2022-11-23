hours = int(input())
minutes = int(input())

minutes_above = 15 - (60 - minutes)

if -1 < minutes < 45:
    print(f"{hours}:{minutes + 15}")
elif minutes == 45 and hours == 23:
    print("0:00")
elif 60 > minutes > 55 and hours == 23:
    print(f"0:{minutes_above}")
elif 55 > minutes > 45 and hours == 23:
    print(f"0:0{minutes_above}")
elif minutes == 45:
    print(f"{hours + 1}:00")
elif 51 > minutes > 45:
    print(f"{hours + 1}:0{minutes_above}")
elif hours == 23 and 60 > minutes > 45:
    print(f"0:{minutes_above}")
elif 60 > minutes > 50:
    print(f"{hours + 1}:{minutes_above}")
elif 50 > minutes > 45:
    print(f"{hours + 1}:0{minutes_above}")
else:
    print("Enter valid hour and minutes")
