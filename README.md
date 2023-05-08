# My Learning Log

> 这是一个学习日志，记录每次学习的主要信息和感受。
>
> 对大部分重要或遗漏知识加粗了。
>
> 大致浏览一下后，发现基础阶段的进度确实很快，难度曲线不是很平滑，所以结合了一下作者的另一个repo的内容。

## Day 1-10

- [x] Day 1 初识Python

  补充了Python解释器知识，不止有一种解释器。

- [x] Day2 语言元素

  冷知识：Python有复数这种类型。PEP 8要求的Python变量命名是小写和下划线组合。

  熟练切片`[:]`对精简代码很重要。`is`和`in`的意义和用法。and 和 or 的短路运算。`print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')`变量替换占位符。
  
  > 作者写的代码都好漂亮，规范全面有条理，mol一下。
  
- [x] Day3 分支结构

  建议不适用tab缩进，而是设置你的代码编辑工具自动将制表键变成4个空格。

  Flat is better than nested.减少代码的嵌套。

  ```python
  from getpass import getpass
  # 输入口令的时候终端中没有回显
  password = getpass.getpass('请输入口令: ')
  ```
  
  > 分支结构还是比较简单的，也没有讲switch。
  
- [x] Day4 循环结构

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

- [x] Day5 构造程序逻辑
  相对而言是比较基础的

- [x] Day6 函数和模块的使用

  函数的定义、返回值

  函数的参数

  - 默认值
  - 可变参数`*args`

  用模块管理函数（同名函数）

  使用`__name__`管理可执行代码

  变量作用域

  >  “局部作用域”---》“嵌套作用域”---》“全局作用域”---》“内置作用域”
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

  
