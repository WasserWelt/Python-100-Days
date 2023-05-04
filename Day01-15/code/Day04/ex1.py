# 练习1：输入一个正整数判断是不是素数。
# 提示：素数指的是只能被1和自身整除的大于1的整数。
'''
判断素数

Verison: 0.1
Author: WasserWelt
'''
from math import sqrt

num = int(input("请输入一个正整数"))
is_prime = True
if num <= 0:
    print("请检查输入，需要为正整数")
else:
    for x in range(2, int(sqrt(num))+1):
        if num % x == 0:
            # 能被整除
            is_prime = False
            break
    if is_prime and num != 1:
        print(f"{num:d}是素数") # 注意是print(f"{var:format}")
    else:
        print(f"{num:d}不是素数")
