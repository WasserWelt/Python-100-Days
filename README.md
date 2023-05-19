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

函数的定义、返回值

函数的参数

- 默认值
- 可变参数`*args`

用模块管理函数（同名函数）

使用`__name__`管理可执行代码

变量作用域

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
    print('call bar())
    bar()
```

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
