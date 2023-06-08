"""
定义和使用字典

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    scores = {"骆昊": 95, "白元芳": 78, "狄仁杰": 82}
    print(scores["骆昊"])
    print(scores["狄仁杰"])
    for elem in scores:
        print("%s\t--->\t%d" % (elem, scores[elem]))
    # 更新
    scores["白元芳"] = 65
    scores["诸葛王朗"] = 71
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    # {'骆昊': 95, '白元芳': 65, '狄仁杰': 82, '诸葛王朗': 71, '冷面': 67, '方启鹤': 85}
    if "武则天" in scores:
        # 没有被执行
        print(scores["武则天"])
        print("hihi")
    print(scores.get("武则天"))  # None
    print(scores.get("武则天", 60))  # 如果没有在dict里，返回第二个参数_default
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop("骆昊", 100))
    scores.clear()
    print(scores)


if __name__ == "__main__":
    main()
