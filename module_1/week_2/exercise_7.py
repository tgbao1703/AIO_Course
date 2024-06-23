from typing import List


def exercise7(x: List, y: List):
    # Use extend to concatenate y into x
    x.extend(y)
    return x

if __name__ == "__main__":
    list_num1 = [1, 2]
    list_num2 = [3, 4]
    list_num3 = [0, 0]

    print(exercise7(list_num1, exercise7(list_num2, list_num3)))

