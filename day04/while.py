"""
用while循环实现1~100求和
"""

sum = 0
num = 1
while num <= 100:
    sum += num
    num += 1
print(sum)

"""
用while循环实现1~100之间的偶数求和
"""

sum, num = 0, 2
while num <= 100:
    sum += num
    num += 2
print(sum)