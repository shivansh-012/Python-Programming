light = input("Enter Color of Light: ")
if light.lower()=="green":
    print("Car is allowed to go")
elif light.lower()=="yellow":
    print("Car has to wait")
elif light.lower()=="red":
    print("Car has to stop")
else:
    print("Unrecognized Signal")