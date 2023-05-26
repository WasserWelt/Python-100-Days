'''
练习3：打印如下所示的三角形图案。
*
**
***
****
*****
    *
   **
  ***
 ****
*****
    *
   ***
  *****
 *******
*********
'''


def print_left_triangle(row, char='*'):
    """
    Args:
        row (int): triangle rows
        char (str, optional): char. Defaults to '*'.
    """
    for i in range(row):
        for _ in range(i + 1):  # 不知道_是什么用
            print(char, end='')  # end=''使得print不换行
        print()


def print_right_triangle(row, char='*'):
    for i in range(row):  # 逐行
        for j in range(row):
            if j < row - i - 1:
                print(' ', end='')
            else:
                print(char, end='')
        print()


def print_middle_triangle(row, char='*'):
    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end='')
        for _ in range(2 * i + 1):
            print(char, end='')
        print()


def main():
    print_left_triangle(5)
    print_right_triangle(10)
    print_middle_triangle(7, char='&')


if __name__ == '__main__':
    main()
