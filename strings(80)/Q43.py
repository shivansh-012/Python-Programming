length, breadth = map(int, input("enter l and b: ").split())
print("{:.2f}m\u00b2".format(length*breadth))

radius, height= map(int, input("enter r and h: ").split())
print("{:.2f}m\u00b3".format(3.14*radius*radius*height))