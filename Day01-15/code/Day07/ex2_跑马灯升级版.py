import os
import time
import threading
import msvcrt

"""
对不起，我之前给出的代码存在问题。感谢您的指出。确实，在使用装饰器的方式中，on_key_press 函数没有实际使用。我在之前的回答中犯了一个错误。

使用装饰器来捕获键盘事件并在按下 ESC 键时退出循环的做法在纯Python中比较困难。因为在标准的Python解释器中，没有直接的方式来非阻塞地监听键盘事件。

如果你希望在按下 ESC 键时能够立即退出循环，那么使用第一个我给出的带有msvcrt模块的解决方案是最简单和可行的方法。
"""


def exit_on_escape(func):
    def wrapper(*args, **kwargs):
        exit_flag = threading.Event()

        def on_key_press(event):
            if event.name == "esc":
                exit_flag.set()

        def check_for_escape():
            while not exit_flag.is_set():
                time.sleep(0.1)

        threading.Thread(target=check_for_escape).start()
        os.system("cls")  # 清理屏幕上的输出
        try:
            func(*args, **kwargs)
        finally:
            exit_flag.set()

    return wrapper


@exit_on_escape
def old_running_letter(*args):
    while True:
        for letter in args:
            os.system("cls")  # 清理屏幕上的输出
            print(letter)
            time.sleep(0.2)
            for _ in range(len(letter)):
                os.system("cls")
                print(letter)
                time.sleep(1)
                letter = letter[1:] + letter[0]  # 从第二个字开始的+第一个字


@exit_on_escape
def old_example():
    content = "北京欢迎你为你开天辟地…………"
    while True:
        os.system("cls")  # 清理屏幕上的输出
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]


def running_letter(*args):
    """
    这里可以再试着盘一下逻辑，把我想要的功能实现！
    """
    while True:
        if msvcrt.kbhit() and msvcrt.getch() == b"\x1b":  # 检测是否按下ESC键
            break

        for letter in args:
            # 清理屏幕上的输出
            os.system("cls")  # os.system('clear')
            print(letter)
            time.sleep(0.2)
            for _ in range(len(letter)):
                os.system("cls")
                print(letter)
                time.sleep(0.2)
                letter = letter[1:] + letter[0]  # 从第二个字开始的+第一个字


def example():
    content = "北京欢迎你为你开天辟地…………"
    while True:
        if msvcrt.kbhit() and msvcrt.getch() == b"\x1b":  # 检测是否按下ESC键
            break
        # 清理屏幕上的输出
        os.system("cls")  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == "__main__":
    running_letter("ABCDEFG", "abcdefg")
    example()
