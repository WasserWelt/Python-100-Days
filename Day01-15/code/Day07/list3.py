"""
生成列表
- 用range创建数字列表
- 生成表达式
- 生成器

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


# 生成Fibonacci序列的生成器
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        # 通过yield关键字将一个普通函数改造成生成器函数
        yield a


def main():
    # 用range创建数值列表
    list1 = list(range(1, 11))
    print(list1)
    # 生成表达式
    list2 = [x * x for x in range(1, 11)]
    print(list2)
    list3 = [m + n for m in "ABCDEFG" for n in "12345"]
    print(list3)
    print(len(list3))
    # 生成器(节省空间但生成下一个元素时需要花费时间)
    gen = (m + n for m in "ABCDEFG" for n in "12345")
    print(gen)
    # <generator object main.<locals>.<genexpr> at 0x000001F3647FE3C0>
    for elem in gen:
        print(elem, end=" ")
    print()
    # A1 A2 A3 A4 A5 B1 B2 B3 B4 B5 C1 C2 C3 C4 C5 D1 D2 D3 D4 D5 E1 E2 E3 E4 E5 F1 F2 F3 F4 F5 G1 G2 G3 G4 G5
    gen = fib(20)
    print(gen)
    # <generator object fib at 0x000001F364890C10>
    for elem in gen:
        print(elem, end=" ")
    print()
    # 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765


if __name__ == "__main__":
    main()
