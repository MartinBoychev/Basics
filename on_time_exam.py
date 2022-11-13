exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

minutes_of_exam = (exam_hour * 60) + exam_min
minutes_arrival = (arrival_hour * 60) + arrival_min
diff = abs(minutes_of_exam - minutes_arrival)
hour = diff // 60
minutes = diff % 60

if minutes_of_exam < minutes_arrival:
    print("Late")
elif minutes_of_exam == minutes_arrival or diff <= 30:
    print("On time")
else:
    print("Early")

if minutes_of_exam > minutes_arrival and hour == 0:
    print(f"{minutes} minutes before the start")
elif minutes_of_exam > minutes_arrival:
    print(f"{hour}:{minutes:02d} hours before the start")
elif minutes_of_exam > minutes_arrival > 0 and hour == 0:
    print(f"{minutes} minutes before the start")
elif minutes_of_exam < minutes_arrival and minutes_arrival > 0 and hour > 0:
    print(f"{hour}:{minutes:02d} hours after the start")
elif minutes_of_exam < minutes_arrival:
    print(f"{minutes} minutes after the start")