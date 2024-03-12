name_s = input("enter name of the station: ")
day = input("enter day of the week: ")

schedule_list = []
n = int(input("no. of shows on that day: "))
while n>0:
    show_name = input("Enter name of show: ")
    start_time = input("Enter starting time(HH:MM:SS AM/PM): ")
    end_time = input("Enter ending time(HH:MM:SS AM/PM): ")
    schedule_list.append([show_name,start_time,end_time])
    n-=1

print("TV Schedule for {} on {}:".format(name_s,day))
print("{:<20} {:<15} {:<15}".format('Show Name', 'Start Time', 'Stop Time'))
for ele in schedule_list:
    print("{:<20} {:<15} {:<15}".format(ele[0], ele[1], ele[2]))