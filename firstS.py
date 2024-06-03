# The solution is type conversion

# Two types of conversion-
# 1. Implicit: program understands automatically
# print(5+8.3)
# print(type(5), type(8.3))

# 2. Explicit
# int(5)
# print(type(5))

fnum = input("enter num1: ")
snum = input("enter num2: ")

ans=int(fnum)+int(snum) # type converted :)
print(ans)

print(type(fnum)) #fnum has not changed, a new obj. is created and that is used
# type conversion doesn't chnages the orignal data, it creates a new value and uses