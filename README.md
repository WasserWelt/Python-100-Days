# My Learning Log

> 这是一个学习日志，记录每次学习的主要信息和感受。
>
> 对大部分重要或遗漏知识加粗了。
>
> 大致浏览一下后，发现基础阶段的进度确实很快，难度曲线不是很平滑，所以结合了一下作者的另一个repo的内容。
>
> 学代码不能太懒蛋！要自己上手敲，敲不来也要抄。

## Day 1-10

### Day 1 初识Python

补充了Python解释器知识，不止有一种解释器。

### Day2 语言元素

冷知识：Python有复数这种类型。PEP 8要求的Python变量命名是小写和下划线组合。

熟练切片`[:]`对精简代码很重要。`is`和`in`的意义和用法。and 和 or 的短路运算。`print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')`变量替换占位符。

> 作者写的代码都好漂亮，规范全面有条理，mol一下。

### Day3 分支结构

建议不适用tab缩进，而是设置你的代码编辑工具自动将制表键变成4个空格。

Flat is better than nested.减少代码的嵌套。

```python
from getpass import getpass
# 输入口令的时候终端中没有回显
password = getpass.getpass('请输入口令: ')
```

> 分支结构还是比较简单的，也没有讲switch。

### Day4 循环结构

`range(a,b)`相当于$[a,b)$。`range(a,b,[step])`。可以利用`for~in~range()`的方式节省很多资源。

> 差不多该做练习了，debug过程中还是有不少知识点的。

《关于找最大公约数每次都要搜一遍辗转相除法怎么做这回事》

```python
for i in range(row):
    for _ in range(i + 1):
        # 这里的'_'是什么写法，头一次见
        print('*', end='')
    print()
```

### Day5 构造程序逻辑

相对而言是比较基础的

### Day6 函数和模块的使用

#### 函数

函数的定义、返回值

{% noteblock :: Python的内置函数%}

- 数学相关: abs / divmod / pow / round / min / max / sum
- 序列相关: len / range / next / filter / map / sorted / slice / reversed
- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
- 数据结构: dict / list / set / tuple
- 其他函数: all / any / id / input / open / print / type

{% endnoteblock %}

#### 函数的参数

- 位置参数
- 可变参数`*args`
- 关键字参数
- 命名关键字参数
- 默认值

{% folding ::实例代码 %}

```python

# 参数默认值
def f1(a, b=5, c=10):
    return a + b * 2 + c * 3


print(f1(1, 2, 3))
print(f1(100, 200))
print(f1(100))
print(f1(c=2, b=3, a=1))


# 可变参数
def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(f2(1, 2, 3))
print(f2(1, 2, 3, 4, 5))
print(f2())


# 关键字参数
def f3(**kw):
    if 'name' in kw:
        print('欢迎你%s!' % kw['name'])
    elif 'tel' in kw:
        print('你的联系电话是: %s!' % kw['tel'])
    else:
        print('没找到你的个人信息!')


param = {'name': '骆昊', 'age': 38}
f3(**param)
f3(name='骆昊', age=38, tel='13866778899')
f3(user='骆昊', age=38, tel='13866778899')
f3(user='骆昊', age=38, mobile='13866778899')
```

{% endfolding %}

#### 模块

用模块管理函数（同名函数）

{% noteblock :: Python常用模块%}

- 运行时服务相关模块: copy / pickle / sys / ...
- 数学相关模块: decimal / math / random / ...
- 字符串处理模块: codecs / re / ...
- 文件处理相关模块: shutil / gzip / ...
- 操作系统服务相关模块: datetime / os / time / logging / io / ...
- 进程和线程相关模块: multiprocessing / threading / queue
- 网络应用相关模块: ftplib / http / smtplib / urllib / ...
- Web编程相关模块: cgi / webbrowser
- 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...

{% endnoteblock %}

使用`__name__`管理可执行代码

### 变量作用域

> “局部作用域”---》“嵌套作用域”---》“全局作用域”---》“内置作用域”
>
> `global` `nonlocal`关键字 闭包

```python
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
```

{% folding ::实例代码 %}

```python
# 局部作用域
def foo1():
    a = 5


foo1()
# print(a)  # NameError

# 全局作用域
b = 10


def foo2():
    print(b)


foo2()  # 10


def foo3():
    b = 100  # 局部变量
    print(b)


foo3()  # 100
print(b)  # 10


def foo4():
    global b
    b = 200  # 全局变量
    print(b)


foo4()  # 200
print(b)  # 200
```

{% endfolding %}

### Day7 字符串和常用数据结构

{% note todo:要自己写一遍程序，学习大佬写法 %}

#### 字符

`\`+`八进制or十六进制orUnicode`表示字符

`r'Char'`不表示转译

字符串拼接、重复、成员运算、切片运算

各种方法和函数

格式化字符的三种写法

#### 列表

定义、运算、遍历

添加移除合并

切片（完整切片以复制，反向切片以倒转）

排序

**列表生成式**：Python的神奇之处

`yield`关键字构造**生成器函数**

#### 元组

元组不可修改，适合一些环境（eg多线程，一个方法返回多个值）。元组在创建时间和占用的空间上面都优于列表。

#### 集合

创建、添加、删除、交并差、对称差

#### 字典

创建（`zip函数`）、获取、遍历、修改、删除、清空

### Day8 面向对象编程基础

- 基本概念
  - 继承
  - 封装
  - 多态
- 私有属性和方法

### Day9 面向对象进阶

#### @property 装饰器
  
  目的是可以让类的属性访问比较清晰

  {% note warning::那么实际解释的时候有什么意义，以及使用时有何帮助呢？%}

  {%noteblock quot::[知乎]python 装饰器详解%}

  装饰器就是一个闭包，装饰器是闭包的一种应用。什么是装饰器呢，简言之，python装饰器就是用于拓展原来函数功能的一种函数，这个函数的特殊之处在于它的返回值也是一个函数，使用python装饰器的好处就是在不用更改原函数的代码前提下给函数增加新的功能。

  装饰器中可以传入参数，先形成一个完整的装饰器，然后再来装饰函数，当然函数如果需要传入参数也是可以的，用不定长参数符号就可以接收，例子中传入了三个参数。

  [python 装饰器详解](https://zhuanlan.zhihu.com/p/87353829)

  {% endnoteblock %}

#### `__slots__`的用处

```python
class Person(object):

  # 限定Person对象只能绑定_name, _age和_gender属性
  __slots__ = ('_name', '_age', '_gender')

  def __init__(self, name, age):
      self._name = name
      self._age = age

```

#### 静态方法
  
  属于类但不属于对象，用`@staticmethod`装饰器。

```python
class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b


def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
```

#### 类方法
  
  **类方法的第一个参数约定名为`cls`**，它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的`元数据对象`），通过这个参数我们可以**获取和类相关的信息**并且可以**创建出类的对象**

```python
class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
```

#### 类之间的关系

- `is-a`——`继承`或`泛化`
- `has-a`——`关联`
- `use-a`——`依赖`

UML语言和面向对象建模

#### 继承和多态

- 继承

  在已有类（父类）的基础上创建新类，叫做子类。子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法。
  
- 里氏替换原则
  
  用子类对象去替换掉一个父类对象

- 重写（override）
  
  子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本

- 多态（poly-morphism）
  
  让父类的同一个行为在子类中拥有不同的实现版本，不同的子类对象会表现出不同的行为

```python
class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass
```

{% note warning::metaclass是什么？ %}

> 在上面的代码中，我们将`Pet`类处理成了一个抽象类，所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。Python从语法层面并没有像Java或C#那样提供对抽象类的支持，但是我们可以通过`abc`模块的`ABCMeta`元类和`abstractmethod`包装器来达到抽象类的效果。如果一个类中**存在**抽象方法那么这个类就不能够实例化（创建对象）。上面的代码中，`Dog`和`Cat`两个子类分别对`Pet`类中的`make_voice`抽象方法进行了重写并给出了不同的实现版本，当我们在`main`函数中调用该方法时，这个方法就表现出了多态行为（同样的方法做了不同的事情）。

### Day10 图形用户界面（GUI）和游戏开发

#### 基于tkinter模块的GUI

Python GUI模块：`tkinker`, `wxPython`,`PyQt`,`PyGTK`

使用tkinter开发GUI应用的5个基本步骤：

1. 导入tkinter模块中我们需要的东西。
2. 创建一个`顶层窗口对象`并用它来承载整个GUI应用。
3. 在`顶层窗口对象`上添加GUI组件。
4. 通过代码将这些GUI组件的功能组织起来。
5. 进入主事件循环(main loop)。

{% folding::使用tkinter的简单GUI %}

```Python
import tkinter
import tkinter.messagebox


def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag # nonlocal关键字见Day6
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('240x160')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()
```

{% endfolding %}

**GUI应用通常是事件驱动式的**，之所以要进入主事件循环就是要监听鼠标、键盘等各种事件的发生并执行对应的代码对事件进行处理，因为事件会持续的发生，所以需要这样的一个循环一直运行着等待下一个事件的发生。

**布局管理器**，通过布局管理器可以对控件进行定位，这三种布局管理器分别是：Placer（开发者提供控件的大小和摆放位置）、Packer（自动将控件填充到合适的位置）和Grid（基于网格坐标来摆放控件）

#### 使用Pygame进行游戏开发

移步原仓库，动手编写代码，体会逐步完善程序的过程。为了本笔记完整性，这里直接复制过来了。

{% folding::Pytgame大球吃小球 %}

```Python
from enum import Enum, unique
from math import sqrt
from random import randint

import pygame


@unique
class Color(Enum):
    """颜色"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """获得随机颜色"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):
    """球"""

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        """初始化方法"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """移动"""
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """吃其他球"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
               	self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)


def main():
    # 定义用来装所有球的容器
    balls = []
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    print(screen.get_width())
    print(screen.get_height())
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    # 定义变量来表示小球在屏幕上的位置
    x, y = 50, 50
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                ball = Ball(x, y, radius, sx, sy, color)
                balls.append(ball)
        screen.fill((255, 255, 255))
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()
```

{% endfolding %}

### Day1-10总结

学的不是很扎实，少写很多码，最近实在是太忙了，又想着要推进度。本来觉得100天很快就能学掉了，结果1-10的内容挺多的，需要多复盘。
