# 练习1：在屏幕上显示跑马灯文字。

import os
import time


def running_letter(*args):
    while True:
        for letter in args:
            # 清理屏幕上的输出
            os.system("cls")  # os.system('clear')
            print(letter)
            time.sleep(0.2)
            for _ in range(len(letter)):
                os.system("cls")
                print(letter)
                time.sleep(1)
                letter = letter[1:] + letter[0]  # 从第二个字开始的+第一个字


def example():
    content = "北京欢迎你为你开天辟地…………"
    while True:
        # 清理屏幕上的输出
        os.system("cls")  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == "__main__":
    running_letter("ABCDEFG", "abcdefg")
    example()
