print("10%-3=",10%-3 )
print("-10%3=",-10%3 )
print("3//-10=", 3 // -10)
print("-10//3=",-10 // 3)
print("3/-10=",3 / -10)
print("-10/3=",-10 / 3 )
#(a+b)mod n = [(a mod n)+(b mod n)]mod n
#-5%4 = (-2*4 + 3) % 4 = 3
#-3 % 7 = ( -1*7 + 4 ) % 7 = 4 
#-5 % 2 = (-3*2 + 1) % 2 = 1
'''
this is because Python’s modulo operator (%) always returns a number having the same sign as the denominator. What
happens behind the scene is that Python applies the distribute law of Modulo operator which is 
However, if one of the operands is negative, the result will be floored as well (i.e. rounded away from
0 towards negative infinity), returning the largest integer less than or equal to x. For example:
'''