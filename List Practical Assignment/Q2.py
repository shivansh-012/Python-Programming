show_name=input("Enter name of show: ")
start_time=input("Enter starting time(HH:MM:SS AM/PM): ")
end_time=input("Enter ending time(HH:MM:SS AM/PM): ")
a=len(show_name)
print("{:<{}} {:<10} {}".format("NAME",a+3,"START_NAME","END_TIME" ))
print("{:<{}} {:<10} {}".format(show_name, a+3, start_time, end_time))