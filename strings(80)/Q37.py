number = 42
num = str(number)
# Left aligned
# left_aligned = "{:<10}".format(number)
# print(f"Left aligned: {left_aligned}")
print(num.ljust(10," "))

# Right aligned
# right_aligned = "{:>10}".format(number)
# print(f"Right aligned: {right_aligned}")
print(num.rjust(10," "))

# Center aligned
# center_aligned = "{:^10}".format(number)
# print(f"Center aligned: {center_aligned}")
print(num.center(10," "))