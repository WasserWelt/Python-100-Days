"""
字典的常用操作

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    stu = {"name": "骆昊", "age": 38, "gender": True}
    print(stu)
    print(stu.keys())  # dict_keys(['name', 'age', 'gender'])
    print(stu.values())  # dict_values(['骆昊', 38, True])
    print(stu.items())
    # dict_items([('name', '骆昊'), ('age', 38), ('gender', True)])
    for elem in stu.items():
        print(elem)  # ('name', '骆昊')
        print(elem[0], elem[1])  # name 骆昊
    if "age" in stu:
        stu["age"] = 20
    print(stu)  # {'name': '骆昊', 'age': 20, 'gender': True}
    stu.setdefault("score", 60)
    print(stu)
    stu.setdefault("score", 100)
    print(stu)
    stu["score"] = 100
    print(stu)


if __name__ == "__main__":
    main()
