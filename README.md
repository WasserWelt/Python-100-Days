# My Learning Log

> 这是一个学习日志，记录每次学习的主要信息和感受。
>
> 对大部分重要或遗漏知识加粗了。

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
- [x] Day4 循环结构
